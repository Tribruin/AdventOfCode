#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC
import numpy as np
from TerminalColors import *

testing = False


def parse_input(input: AOC):
    data = list()
    for line in input.read_lines():
        x1, _, y1 = line.split()
        start = tuple(map(int, x1.split(",")))
        end = tuple(map(int, y1.split(",")))
        data.append([start, end])
    return data


def print_array(array):
    x_size, y_size = np.shape(array)
    for y in range(y_size):
        for x in range(x_size):
            a = array[y][x]
            if a == 0:
                char = "."
            else:
                char = str(a)
            print(f"{char} ", end="")
        print()
    print()


def part1(data: list):
    max_x = max([i[0][0] if i[0][0] > i[1][0] else i[1][0] for i in data])
    max_y = max([i[0][1] if i[0][1] > i[1][1] else i[1][1] for i in data])

    array = np.zeros((int(max_x) + 1, int(max_y) + 1), dtype=int)

    for line in data:
        x1, y1 = line[0]
        x2, y2 = line[1]
        if x1 == x2:
            if y1 > y2:
                y2, y1 = y1, y2
            array[y1 : y2 + 1, x1 : x1 + 1] += 1
        elif y1 == y2:
            if x1 > x2:
                x2, x1 = x1, x2
            array[y1 : y1 + 1, x1 : x2 + 1] += 1
        else:
            pass
    total = np.sum((array > 1))
    print(total)


def part2(data):
    max_x = max([i[0][0] if i[0][0] > i[1][0] else i[1][0] for i in data])
    max_y = max([i[0][1] if i[0][1] > i[1][1] else i[1][1] for i in data])

    array = np.zeros((int(max_y) + 1, int(max_x) + 1), dtype=int)

    for line in data:
        x1, y1 = line[0]
        x2, y2 = line[1]

        if x1 == x2:
            if y1 > y2:
                y2, y1 = y1, y2
            array[y1 : y2 + 1, x1 : x1 + 1] += 1
        elif y1 == y2:
            if x1 > x2:
                x2, x1 = x1, x2
            array[y1 : y1 + 1, x1 : x2 + 1] += 1
        else:
            x_step = y_step = 1
            if x1 > x2:
                x_step = -1
            if y1 > y2:
                y_step = -1

            for i in range(abs(x2 - x1) + 1):
                array[y1 + i * y_step][x1 + i * x_step] += 1
                # print_array(array)
        # print_array(array)
    total = np.sum(array > 1)
    print(total)


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    data = AOC(codeDate, codeYear, test=testing)
    output = parse_input(data)

    part1(output)
    part2(output)


if __name__ == "__main__":
    main()
