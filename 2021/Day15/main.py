#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
import time
from AOC import AOC


testing = False


def parse_input(data_input):
    riskLevel = list()
    lines = data_input.read_lines()
    for line in lines:
        temp = [int(x) for x in line]
        riskLevel.append(temp)
    return riskLevel


def createGraph(size, values) -> dict:
    graph = dict()
    x_size, y_size = size
    for y in range(0, y_size):
        for x in range(0, x_size):
            graph[(x, y)] = dict()
            graph[(x, y)]['risk'] = values[y][x]
            graph[(x, y)]['score'] = float("inf")
            graph[(x, y)]['neighbors'] = list()
            if x > 0:
                graph[(x, y)]['neighbors'].append((x-1, y))
            if x < x_size - 1:
                graph[(x, y)]['neighbors'].append((x+1, y))
            if y > 0:
                graph[(x, y)]['neighbors'].append((x, y-1))
            if y < y_size - 1:
                graph[(x, y)]['neighbors'].append((x, y+1))
    return graph


def getLowestScorePoint(points: list, graph: dict) -> tuple:
    lowestScore = float("inf")
    lowestPoint = None
    pointsToSort = [x for x in points if graph[x]['score'] < float('inf')]
    for point in pointsToSort:
        if graph[point]["score"] < lowestScore:
            lowestScore = graph[point]["score"]
            lowestPoint = point
    return lowestPoint


def part1(riskLevel):
    x_size, y_size = len(riskLevel[0]), len(riskLevel)
    graph = createGraph((x_size, y_size), riskLevel)
    visited = list()
    unvisited = [x for x in graph.keys()]
    currentPoint = (0, 0)
    graph[currentPoint]['score'] = 0                            # Starting point is not entered, so no score
    while len(unvisited) > 0:
        # print(f"Checking Point: {currentPoint}")
        for point in graph[currentPoint]['neighbors']:
            if graph[currentPoint]['score'] + graph[point]['risk'] < graph[point]['score']:
                graph[point]['score'] = graph[currentPoint]['score'] + graph[point]['risk']
        visited.append(currentPoint)
        unvisited.remove(currentPoint)
        if len(unvisited) > 0:
            currentPoint = getLowestScorePoint(unvisited, graph)
    print(f"Lowest Risk Score: {graph[(x_size-1, y_size-1)]['score']}")


def part2(riskLevel):
    x_size, y_size = len(riskLevel[0]) * 5, len(riskLevel) * 5
    fullRiskLevel = list()
    for y in range(0, 5):
        for y1 in range(0, y_size // 5):
            line = list()
            for x in range(0, 5):
                for x1 in range(0, x_size // 5):
                    newRiskLevel = (riskLevel[y1][x1] + (x + y))
                    if newRiskLevel > 9:
                        newRiskLevel = newRiskLevel % 9
                    line.append(newRiskLevel)
            fullRiskLevel.append(line)

    # for y in range(len(fullRiskLevel)):
    #     for x in range(len(fullRiskLevel[0])):
    #         print(fullRiskLevel[y][x], end="")
    #     print()

    graph = createGraph((x_size, y_size), fullRiskLevel)
    visited = list()
    unvisited = [x for x in graph.keys()]
    currentPoint = (0, 0)
    graph[currentPoint]['score'] = 0                             # Starting point is not entered, so no score
    startTime = time.time()
    while len(unvisited) > 0:
        # print(f"Checking Point: {currentPoint}")
        for point in graph[currentPoint]['neighbors']:
            if graph[currentPoint]['score'] + graph[point]['risk'] < graph[point]['score']:
                graph[point]['score'] = graph[currentPoint]['score'] + graph[point]['risk']
        visited.append(currentPoint)
        unvisited.remove(currentPoint)
        if len(unvisited) % 1000 == 0:
            currentTime = time.time()
            print(f"Visited: {len(unvisited)} Secs Elapsed: {currentTime - startTime}")
            startTime = currentTime
        if len(unvisited) > 0:
            currentPoint = getLowestScorePoint(unvisited, graph)
    print(f"Lowest Risk Score: {graph[(x_size-1, y_size-1)]['score']}")


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    # global data
    code_data = AOC(codeDate, codeYear, test=testing)
    data_input = parse_input(code_data)

    # part1(data_input)
    part2(data_input)


if __name__ == "__main__":
    main()
