#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from timeit import timeit

# sys.path.append("/Users/rblount/Scripts/AdventOfCode/tools")

from AOC import AOC


def part1():
    triangles = list()
    for line in data.lines:
        triangle = list()
        for side in line.split():
            if side != "":
                triangle.append(int(side))
        triangle.sort()
        triangles.append(triangle)
    valid_triangles = 0
    for triangle in triangles:
        if int(triangle[0]) + int(triangle[1]) > int(triangle[2]):
            valid_triangles += 1
    print(valid_triangles)


def part2():
    triangles = list()
    for i in range(0, len(data.lines), 3):
        t = list()
        t.append([int(x) for x in data.lines[i].split()])
        t.append([int(x) for x in data.lines[i + 1].split()])
        t.append([int(x) for x in data.lines[i + 2].split()])
        for k in range(3):
            new_triangle = [t[0][k], t[1][k], t[2][k]]
            new_triangle.sort()
            triangles.append(new_triangle)

    valid_triangles = 0
    for triangle in triangles:
        if int(triangle[0]) + int(triangle[1]) > int(triangle[2]):
            valid_triangles += 1
    print(valid_triangles)


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=False)

    pass
    print(f"Time for Part One: {timeit(part1, number=1)}")
    print(f"Time for Part Two: {timeit(part2, number=1)}")


if __name__ == "__main__":
    main()
