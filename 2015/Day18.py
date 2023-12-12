from os import system
from time import sleep
import numpy as np

# gridX, gridY = 0,0
# gridX, gridY = 6,6
# steps = 4
steps = 100
# inputFile = "/Users/rblount/OneDrive/AdventOfCode/2015/Day18-Input.txt"
# inputFile = "/Users/rblount/OneDrive/AdventOfCode/2015/Day18-TestInput2.txt"
inputFile = "/Users/rblount/Scripts/AdventOfCode/2015/Day18-Input.txt"


def parseInput(file):
    f = open(file, "r")
    allLines = f.readlines()
    gridY = len(allLines)
    gridX = len(allLines[0].rstrip())

    array = np.zeros((gridY, gridX), dtype=np.bool)

    x, y = 0, 0
    for line in allLines:
        for char in line:
            if char == "#":
                array[y][x] = True
            x += 1
        y += 1
        x = 0

    return array


def printArray(array):

    system("clear")

    gridY, gridX = array.shape

    for y in range(gridY):
        for x in range(gridX):
            if array[y][x]:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()
    return


def processMove(array):
    def getNeighbors(array, x, y):
        # neighbors = 0
        xPos = [x - 1, x, x + 1]
        yPos = [y - 1, y, y + 1]
        lightsToCheck = []
        for yMove in yPos:
            if 0 <= yMove < gridY:
                for xMove in xPos:
                    if 0 <= xMove < gridX:
                        if not (x == xMove and y == yMove):
                            lightsToCheck.append(array[yMove][xMove])
        return sum(lightsToCheck)

    gridY, gridX = array.shape
    newArray = np.zeros((gridX, gridY), dtype=np.bool)
    for y in range(gridY):
        for x in range(gridX):
            numOfNeighbors = getNeighbors(array, x, y)
            if array[y][x]:
                if numOfNeighbors in [2, 3]:
                    newArray[y][x] = True
                else:
                    newArray[y][x] = False
            else:
                if numOfNeighbors == 3:
                    newArray[y][x] = True
                else:
                    newArray[y][x] = False
    return newArray


def part1():
    lightArray = parseInput(inputFile)
    # printArray(lightArray)

    for x in range(steps):
        lightArray = processMove(lightArray)

        printArray(lightArray)
        print(f"Executing Step: {x}")
        sleep(0.5)

    print(np.sum(lightArray))


def part2():
    lightArray = parseInput(inputFile)
    gridY, gridX = lightArray.shape
    # Turn on stuck lights if not already on
    lightArray[0][0] = True
    lightArray[0][gridX - 1] = True
    lightArray[gridY - 1][0] = True
    lightArray[gridY - 1][gridX - 1] = True
    # printArray(lightArray)

    for x in range(steps):
        lightArray = processMove(lightArray)
        # Turn on stuck lights i not alrady on
        lightArray[0][0] = True
        lightArray[0][gridX - 1] = True
        lightArray[gridY - 1][0] = True
        lightArray[gridY - 1][gridX - 1] = True
        printArray(lightArray)
        print(f"Executing Step: {x}")
        sleep(0.5)

    print(np.sum(lightArray))


part1()
part2()
