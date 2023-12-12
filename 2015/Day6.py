import numpy as np

gridX, gridY = 1000, 1000
inputFile = "Day6-Input.txt"
# inputFile = "/Users/rblount/OneDrive/AdventOfCode/2015/Day6-Input-Test.txt"

def parseInput(file):
    f = open(file, "r")

    actions = []
    for line in f.readlines():
        line = line.rstrip()
        parsedLine = line.split(" ")
        if parsedLine[0] == "turn":
            parsedLine.pop(0)

        start = parsedLine[1].split(",")
        end = parsedLine[3].split(",")

        actions.append([parsedLine[0], start, end])
    return actions


def part1():

    def processAction(action):

        # split the action
        actionMove = action[0]
        startX, startY = action[1]
        endX, endY = action[2]

        for y in range(int(startY), int(endY) + 1):
            for x in range(int(startX), int(endX) + 1):
                if actionMove == "on":
                    grid[y][x] = True
                elif actionMove == "off":
                    grid[y][x] = False
                elif actionMove == "toggle":
                    grid[y][x] = not grid[y][x]


    grid = np.zeros((gridY, gridX), dtype=np.bool)
    actions = parseInput(inputFile)
    for action in actions:
        processAction(action)
        onCount = np.count_nonzero(grid)

    print(np.count_nonzero(grid))

def part2():

    def processAction(action):

        # split the action
        actionMove = action[0]
        startX, startY = action[1]
        endX, endY = action[2]

        for y in range(int(startY), int(endY) + 1):
            for x in range(int(startX), int(endX) + 1):
                if actionMove == "on":
                    grid[y][x] += 1
                elif actionMove == "off" and grid[y][x] > 0:            # Don't let brightness go below 0
                    grid[y][x] -= 1
                elif actionMove == "toggle":
                    grid[y][x] += 2


    grid = np.zeros((gridY, gridX), dtype=np.int)
    actions = parseInput(inputFile)
    for action in actions:
        processAction(action)
        onCount = np.count_nonzero(grid)

    print(np.sum(grid))

part1()
part2()
