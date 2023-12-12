
from AOC import AOC, getDateYear, addTuples
from TerminalColors import *

testing = True
dirs = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}
myMoves = ((1, 0),  (0, 1), (0, 0), (0, -1), (-1, 0))


def parse_input(codeInput):
    walls = list()
    openSpaces = dict()

    for y, line in enumerate(codeInput.read_lines()):
        for x, space in enumerate(line):
            if space == "#":
                walls.append((x, y))
            elif space == ".":
                openSpaces[(x, y)] = list()
            else:
                openSpaces[(x, y)] = [space]

    result = (walls, openSpaces)
    return result


def printMap(objectMap, walls, currentPos):
    allPoints = walls + list(objectMap.keys())
    yMax = max([i[1] for i in allPoints]) + 1
    xMax = max([i[0] for i in allPoints]) + 1
    # print(f"{CLEAR}")
    for y in range(yMax):
        for x in range(xMax):
            if (x, y) == currentPos:
                print(f"{BOLD}E{ENDCOLOR}", end="")
            elif (x, y) in walls:
                print(f"{BLOCK}", end="")
            elif len(objectMap[(x, y)]) > 1:
                print(f"{BOLD}{len(objectMap[(x,y)])}{ENDCOLOR}", end="")
            elif len(objectMap[(x, y)]) == 0:
                print(".", end="")
            else:
                print(f"{objectMap[(x,y)][0]}", end="")
        print()


def nextMinute(spaces):
    newMap = {point: [] for point in spaces}
    yMax = max([i[1] for i in spaces]) - 1                # Account for the exit
    xMax = max([i[0] for i in spaces])

    for point, moves in spaces.items():
        for move in moves:
            newPoint = addTuples(point, dirs[move])
            if newPoint[0] == 0:
                newPoint = (xMax, newPoint[1])
            elif newPoint[0] == xMax + 1:
                newPoint = (1, newPoint[1])
            elif newPoint[1] == 0:
                newPoint = (newPoint[0], yMax)
            elif newPoint[1] == yMax + 1:
                newPoint = (newPoint[0], 1)
            newMap[newPoint].append(move)
    return newMap


def moveSpace(spaces, currentPoint):
    possibleMoves = list()
    for move in myMoves:
        checkPos = addTuples(currentPoint, move)
        if checkPos in walls:
            pass
        elif checkPos not in list(spaces.keys()):
            pass
        elif len(spaces[checkPos]) == 0:
            possibleMoves.append(checkPos)
    return possibleMoves


def findEnd(currentSpace, currentPoint):

    currentTime = 0
    while currentPoint != endPoint:
        currentTime += 1
        newSpaces = nextMinute(currentSpace)
        currentSpace = newSpaces
        possibleMoves = moveSpace(newSpaces, currentPoint)
        print()
        print(f"Minute {currentTime} - Possible Points {possibleMoves} - New Point {currentPoint}")
        printMap(currentSpace, walls, currentPoint)

        if len(possibleMoves) == 0:
            return float('inf')

        if len(possibleMoves) > 1:
            bestTime = float('inf')
            for nextMove in possibleMoves:
                addTime = findEnd(currentSpace, nextMove)
                if addTime < bestTime:
                    currentPoint = nextMove
                    bestTime = addTime
            currentTime += addTime


def part1(dataInput):
    global walls
    global endPoint

    walls, spaces = dataInput
    yMax = max([i[1] for i in walls]) + 1
    xMax = max([i[0] for i in walls]) + 1
    for x in range(xMax):
        if (x, 0) not in walls:
            startPoint = (x, 0)
            break
    for x in range(xMax):
        if (x, yMax - 1) not in walls:
            endPoint = (x, yMax - 1)
            break

    minMinutes = float('inf')
    currentPoint = startPoint
    print("Inital State")
    printMap(spaces, walls, currentPoint)
    minute = 0
    totalTime = findEnd(spaces, currentPoint)

    print(totalTime)


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
