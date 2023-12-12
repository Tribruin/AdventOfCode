from AOC import AOC, getDateYear, addTuples
from TerminalColors import *
from time import sleep
import numpy as np

EMPTY = 0
WALL = 1
SAND = 2

OBJECT = [" ", f"{BLUE}█{ENDCOLOR}", f"{RED}o{ENDCOLOR}"]

testing = False
if testing:
    arraySize = (20, 1000)
else:
    arraySize = (400, 1000)


def parse_input2(codeInput):
    rockMap = np.zeros(arraySize, dtype=int)
    lines = codeInput.read_lines()
    for line in lines:
        lineCoords = line.split(" -> ")
        for k in range(len(lineCoords) - 1):
            x1, y1 = [int(j) for j in lineCoords[k].split(",")]
            x2, y2 = [int(j) for j in lineCoords[k + 1].split(",")]
            startX, startY = min([x1, x2]), min([y1, y2])
            endX, endY = max([x1, x2]), max([y1, y2])
            for y in range(startY, endY + 1):
                for x in range(startX, endX + 1):
                    rockMap[y][x] = WALL

    for y in range(rockMap.shape[0] - 1, 0, -1):
        if np.sum(rockMap[y]) != EMPTY:
            yMax = y
            break

    for x in range(rockMap.shape[1] - 1, 0, -1):
        if np.sum(rockMap[:, x]) != EMPTY:
            xMax = x
            break

    for x in range(rockMap.shape[1]):
        rockMap[(yMax + 2, x)] = WALL

    newRockMap = rockMap[0 : yMax + 3, :]

    return newRockMap


def parse_input1(codeInput):
    rockMap = np.zeros(arraySize, dtype=int)
    lines = codeInput.read_lines()
    for line in lines:
        lineCoords = line.split(" -> ")
        for k in range(len(lineCoords) - 1):
            x1, y1 = [int(j) for j in lineCoords[k].split(",")]
            x2, y2 = [int(j) for j in lineCoords[k + 1].split(",")]
            startX, startY = min([x1, x2]), min([y1, y2])
            endX, endY = max([x1, x2]), max([y1, y2])
            for y in range(startY, endY + 1):
                for x in range(startX, endX + 1):
                    rockMap[y][x] = WALL

    # calculate the maxy, and minx,maxx
    for y in range(rockMap.shape[0] - 1, 0, -1):
        if np.sum(rockMap[y]) != EMPTY:
            yMax = y
            break
    for x in range(0, rockMap.shape[1]):
        if np.sum(rockMap[:, x]) != EMPTY:
            xMin = x
            break
    for x in range(rockMap.shape[1] - 1, 0, -1):
        if np.sum(rockMap[:, x]) != EMPTY:
            xMax = x
            break
    offset = xMin
    newRockMap = rockMap[0 : yMax + 2, xMin - 2 : xMax + 2]

    return newRockMap, offset


def printMap(rockMap, currentPos):
    return
    if rockMap.shape[1] > 50:
        if currentPos[1] + 25 < rockMap.shape[1]:
            xMin, xMax = (currentPos[1] - 25, currentPos[1] + 25)
        else:
            xMin, xMax = (
                currentPos - (50 - (rockMap.shape[1] - currentPos[1])),
                rockMap.shape[1],
            )
    else:
        xMin, xMax = (0, rockMap.shape[1])

    if rockMap.shape[0] > 50:
        if currentPos[0] < 25:
            yMin, yMax = 0, 50
        elif currentPos[0] > (rockMap.shape[0] - 25):
            yMin, yMax = rockMap.shape[0] - 50, rockMap[0]
        else:
            yMin, yMax = currentPos[0] - 25, currentPos[0] - 25
    else:
        yMin, yMax = (0, rockMap.shape[0])

    print(f"{CLEAR}")
    for y in range(yMin, yMax):
        for x in range(xMin, xMax):
            print(f"{OBJECT[rockMap[(y, x)]]}", end="")
        print()
    print((xMin, xMax), (yMin, yMax))


def dropSand(rockMap, startPos):
    moves = [(1, 0), (1, -1), (1, 1)]

    currentPos = startPos
    falling = True
    while falling:
        for move in moves:
            falling = False
            newPos = addTuples(currentPos, move)
            if newPos[0] == rockMap.shape[0]:
                falling = True
                return newPos  # Falling in to the Abyss

            if rockMap[newPos] == 0:
                rockMap[currentPos] = 0
                rockMap[newPos] = SAND
                currentPos = newPos
                falling = True
                break
        printMap(rockMap, currentPos)
    return currentPos


def part1(rockMap, offset):
    snowStartPos = (0, 500 - offset + 2)
    rockMap[snowStartPos] = SAND
    printMap(rockMap, snowStartPos)
    inAbyss = False
    snowFallen = 0
    while not inAbyss:
        lastPos = dropSand(rockMap, snowStartPos)
        if lastPos[0] == rockMap.shape[0]:
            inAbyss = True
            print(f"Total Snow Fallen: {snowFallen}")
        else:
            snowFallen += 1
            # print(f"Snow Fallen: {snowFallen}")
            # sleep(1)


def part2(rockMap):
    sandStartPos = (0, 500)
    rockMap[sandStartPos] = SAND
    inAbyss = False
    sandFallen = 0
    while not inAbyss:
        lastPos = dropSand(rockMap, sandStartPos)
        # printMap(rockMap, lastPos)
        if lastPos == (0, 500):
            sandFallen += 1
            inAbyss = True
            rockMap[lastPos] = SAND
        else:
            sandFallen += 1
            # print(f"Sand Fallen: {sandFallen} - Last Pos {lastPos}")
            # sleep(0.25)
    printMap(rockMap, sandStartPos)
    print(f"** Total Sand Fallen: {sandFallen} - Last Pos {lastPos}")


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    dataInput, offset = parse_input1(codeInput)

    part1(dataInput, offset)
    dataInput = parse_input2(codeInput)
    part2(dataInput)


if __name__ == "__main__":
    main()
