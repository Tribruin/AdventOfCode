from AOC import AOC, getDateYear
from TerminalColors import *
import numpy as np

testing = True


def find_lenx_leny(locs: list) -> (tuple, tuple):
    minx = min([x[0] for x in locs])
    miny = min([x[1] for x in locs])
    maxx = max([x[0] for x in locs])
    maxy = max([x[1] for x in locs])
    return (minx, miny), (maxx, maxy)


def printMap(patterns: list):
    for pattern in patterns:
        (minX, minY), (maxX, maxY) = find_lenx_leny(pattern)
        for y in range(minY, maxY + 1):
            for x in range(minX, maxX + 1):
                if (x, y) in pattern:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        print()


def parse_input(codeInput: AOC):
    lines = codeInput.read_lines()
    result = list()
    length = len(lines)
    y = 0
    pattern = list()
    for k in range(length):
        line = lines[k]
        if line == "":
            result.append(pattern)
            y = 0

            pattern = list()
            continue
        for x, pos in enumerate(line):
            if pos == "#":
                pattern.append((x, y))
        y += 1

    # printMap(result)
    return result

def comparePatterns(x, y)

def findMirrorPattern(pattern):
    # https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-3-2/
    # Need to look at this algorythem.

    (_, _), (maxX, maxY) = find_lenx_leny(pattern)
    # maxX += 1
    # maxY += 1

    # Looking at the rows
    maxRows = (maxX + 1) // 2
    for y in range(1, maxY):
        # # Get the maximum rows that can reflect
        # if y <= (maxY - y):
        #     maxRows = y
        # else:
        #     maxRows = maxY - y

        for rows in range(1, maxRows + 1):
            # findAll Columns to compare
            topSide = [pos for pos in pattern if (y - rows) <= pos[1] < y]
            bottomSide = [pos for pos in pattern if y <= pos[1] < (y + rows)]


def part1(patterns):
    total = 0
    for pattern in patterns:
        findMirrorPattern(pattern=pattern)


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
