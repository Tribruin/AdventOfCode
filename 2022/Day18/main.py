
import sys
import itertools
from AOC import AOC, getDateYear, addTuples
from TerminalColors import *

testing = False
sidesToCheck = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]


def parse_input(codeInput):
    result = codeInput.find_all_ints_in_lines()
    result = [tuple(x) for x in result]
    return result


def exposedSides(points, point):
    exposedSides = 0
    for check in sidesToCheck:
        pointToCheck = addTuples(point, check)
        if pointToCheck not in points:
            exposedSides += 1
    return exposedSides


def findOpedClosedPoints(pointToCheck, currentPath):
    if pointToCheck in openPoints:
        return True

    if pointToCheck in closedPoints:
        return False

    adjecentPoints = [addTuples(x, pointToCheck) for x in sidesToCheck]
    for point in adjecentPoints:

        if point in currentPath:
            break

        if point in openPoints:
            return True

        if point not in closedPoints and point not in filledPoints:
            currentPath.append(point)
            if findOpedClosedPoints(point, currentPath):
                openPoints.append(point)

    return False


def part1(filledPoints):
    totalExposedSides = 0
    for point in filledPoints:
        totalExposedSides += exposedSides(filledPoints, point)
    print(totalExposedSides)


def part2(data):
    global filledPoints
    filledPoints = data

    maxX = max([x[0] for x in filledPoints])
    minX = min([x[0] for x in filledPoints])
    maxY = max([x[1] for x in filledPoints])
    minY = min([x[1] for x in filledPoints])
    maxZ = max([x[2] for x in filledPoints])
    minZ = min([x[2] for x in filledPoints])

    global emptyPoints
    emptyPoints = list()

    # Create the empty space
    for x in range(-1, maxX + 2):
        for y in range(-1, maxY + 2):
            for z in range(-1, maxZ + 2):
                if (x, y, z) not in emptyPoints:
                    # if (x, y, z) not in filledPoints:
                    emptyPoints.append((x, y, z))

    emptyPoints.sort()
    emptyPoints = list(set(emptyPoints) - set(filledPoints))

    global openPoints
    openPoints = list()

    global closedPoints
    closedPoints = list()

    # Make all the edges as in open spaces
    for y in range(-1, maxY + 2):
        for z in range(-1, maxZ + 2):
            openPoints.append((-1, y, z))
            openPoints.append((maxX+1, y, z))

    for x in range(-1, maxX + 2):
        for z in range(-1, maxZ + 2):
            openPoints.append((x, -1, z))
            openPoints.append((x, maxY + 1, z))
    for x in range(0, maxX + 2):
        for y in range(-1, maxY + 2):
            openPoints.append((x, y, -1))
            openPoints.append((x, y, maxZ + 1))

    openPoints = list(set(openPoints))
    openPoints.sort()
    emptyPoints = list(set(emptyPoints) - set(openPoints))
    emptyPoints.sort()

    # Calculate whether the remaining empty points are open or closed
    for a, point in enumerate(emptyPoints):
        # if a % 50 == 0:
        #     print(f"Checking Point # {a}")
        if findOpedClosedPoints(point, [point]):
            openPoints.append(point)
        else:
            closedPoints.append(point)

    openPoints = list(set(openPoints))
    closedPoints = list(set(closedPoints))

    # Calculate the exposed sides of the filled spaces
    allBadPoints = filledPoints + closedPoints
    totalExposedSides = 0
    for point in filledPoints:
        totalExposedSides += exposedSides(allBadPoints, point)

    print(totalExposedSides)


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
