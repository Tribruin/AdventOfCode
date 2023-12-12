import re
from itertools import combinations
import numpy as np

from AOC import AOC, getDateYear, manhattan_dist
from TerminalColors import *


testing = True
age = 2


def printGalaxies(galaxies):
    yMax, xMax = galaxies.shape
    for y in range(yMax):
        for x in range(xMax):
            if galaxies[y][x]:
                print("#", end="")
            else:
                print(",", end="")
        print()
    print()


def parse_input(codeInput: AOC):
    lines = codeInput.read_lines()
    xMax, yMax = len(lines[0]), len(lines)
    galaxies = np.full((yMax, xMax), False)
    for y, line in enumerate(lines):
        matches = re.finditer("#", line)
        for xmatch in matches:
            x = xmatch.start()
            galaxies[y, x] = True

    # printGalaxies(galaxies)

    return galaxies


def part1(galaxies: np.ndarray):
    def expandGalaxy(galaxies: np.ndarray):
        newGalaxy = np.copy(galaxies)
        yMax, xMax = galaxies.shape
        for y in range(yMax - 1, -1, -1):
            if np.sum(galaxies[y, :]) == 0:
                galaxies = np.insert(galaxies, y, False, axis=0)
            # printGalaxies(galaxies)
        for x in range(xMax - 1, -1, -1):
            if np.sum(galaxies[:, x]) == 0:
                galaxies = np.insert(galaxies, x, False, axis=1)

        return galaxies

    newGalaxies = expandGalaxy(galaxies)
    tempLocs = np.nonzero(newGalaxies)
    galaxyLocs = list()
    for i in range(len(tempLocs[0])):
        galaxyLocs.append((tempLocs[0][i], tempLocs[1][i]))

    routes = list(combinations(galaxyLocs, 2))
    totalLen = 0
    for route in routes:
        totalLen += manhattan_dist(route[0], route[1])

    print(totalLen)


def part2(galaxies):
    def findDist(route, galaxies):
        (yStart, xStart), (yEnd, xEnd) = route
        if xStart > xEnd:
            xEnd, xStart = xStart, xEnd
        if yStart > yEnd:
            yEnd, yStart = yStart, yEnd

        dist = 0
        for y in range(yStart + 1, yEnd + 1):
            dist += 1
            if np.sum(galaxies[y, :]) == 0:
                dist += age - 1
        for x in range(xStart + 1, xEnd + 1):
            dist += 1
            if np.sum(galaxies[:, x]) == 0:
                dist += age - 1

        # print(route, dist)
        return dist

    tempLocs = np.nonzero(galaxies)
    galaxyLocs = list()
    for i in range(len(tempLocs[0])):
        galaxyLocs.append((tempLocs[0][i], tempLocs[1][i]))

    routes = list(combinations(galaxyLocs, 2))
    totalDist = 0
    for route in routes:
        totalDist += findDist(route=route, galaxies=galaxies)

    print(totalDist)


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    dataInput = parse_input(codeInput)

    # part1(dataInput)
    part2(dataInput)


if __name__ == "__main__":
    main()
