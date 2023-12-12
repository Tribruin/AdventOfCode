
import numpy as np
from AOC import AOC, getDateYear, addTuples
from TerminalColors import *

testing = True

width = 7
height = 4
totalShapes = 2022

shapesPoints = [
    [(1, 4), [(0, 0), (0, 1), (0, 2), (0, 3)]],
    [(3, 3), [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)]],
    [(3, 3), [(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)]],
    [(4, 1), [(0, 0), (1, 0), (2, 0), (3, 0)]],
    [(2, 2), [(0, 0), (0, 1), (1, 0), (1, 1)]]
]

shapesMasks = list()
for shape in shapesPoints:
    newShape = np.zeros(shape[0], dtype=bool)
    for point in shape[1]:
        newShape[point] = True
    shapesMasks.append(newShape)

windMoves = {'<': (0, -1), '>': (0, 1)}


def parse_input(codeInput):
    result = str(codeInput.read_file())
    return result


def printShaft(currentShaft, currentBlock):
    for y in range(currentShaft.shape[0]):
        print('|', end="")
        for x in range(currentShaft.shape[1]):
            shapeToPrint = "."
            if currentShaft[(y, x)]:
                shapeToPrint = "#"
            if currentBlock != None:
                if (y, x) in currentBlock:
                    shapeToPrint = "@"
            print(shapeToPrint, end="")
        print("|")
    print(f"+{'-' * width}+")
    print()


def addY(shaft, shape) -> int:
    lowestY = max(point[0] for point in shape[1])
    for y in (lowestY+6):
        if sum(shaft[y]) > 0:
            return 3 + lowestY - y
    return 4


def blowShape(shape, dir, mask):
    possibleMove = windMoves[dir]
    newXs = [x[1] + possibleMove[1] for x in shape]
    if min(newXs) >= 0 and max(newXs) < width:
        shape = [addTuples(x, windMoves[dir]) for x in shape]
    return shape


def checkNextDrop(shaft, pos, mask):
    lowestY = max([point[0] for point in pos])
    if lowestY + 1 < shaft.shape[0]:
        return True
    return False


def part1(winDirs):

    currentWinDir = 0
    currentShaft = np.zeros((height, width), dtype=bool)
    print("Starting Shaft")
    printShaft(currentShaft, None)

    for currentShape in range(0, totalShapes):
        currentPos = (0, 2)
        currentShapePos = shapesPoints[currentShape % len(shapesPoints)][1]
        currentShapePos = [addTuples(currentPos, x) for x in currentShapePos]
        currentShapeMask = shapesMasks[currentShape % len(shapesPoints)]
        printShaft(currentShaft, currentShapePos)
        atBottom = False
        while not atBottom:
            winDir = winDirs[currentWinDir]
            currentShapePos = blowShape(currentShapePos, winDir, currentShapeMask)
            if checkNextDrop(currentShaft, currentShapePos, currentShapeMask):
                currentShapePos = [addTuples((1, 0), point) for point in currentShapePos]
            else:
                atBottom = True
                printShaft(currentShaft, currentShapePos)
                nextShape = ((currentShape + 1) % len(shapesPoints))
                for point in currentShapePos:
                    currentShaft[point] = True
                printShaft(currentShaft, currentShapePos)
                newHeight = addY(currentShaft, shapesPoints[nextShape])
            # print(f"Current Wind Dir {winDir}")

            currentWinDir = currentWinDir + 1 - (currentWinDir // len(winDirs))


def part2(dataInput):
    pass


def main():

    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    dataInput = parse_input(codeInput)

    part1(dataInput)
    part2(dataInput)


if __name__ == "__main__":
    main()
