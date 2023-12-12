#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
import numpy as np
from AOC import AOC

testing = False
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Right, Up, Left, Down


def parse_input(code_input):
    result = int(code_input[0])
    return result


def part1(data_input):
    point = (0, 0)
    max_x = max_y = 1
    min_x = min_y = -1
    current_dir = 0

    for i in range(data_input - 1):
        point = (point[0] + moves[current_dir][0], point[1] + moves[current_dir][1])

        if point[0] == max_x and current_dir % 2 == 0:
            max_x += 1
            current_dir = current_dir + 1
            if current_dir > 3:
                current_dir -= 4
        elif point[0] == min_x and current_dir % 2 == 0:
            min_x -= 1
            current_dir = current_dir + 1
            if current_dir > 3:
                current_dir -= 4
        elif point[1] == max_y and current_dir % 2 != 0:
            max_y += 1
            current_dir = current_dir + 1
            if current_dir > 3:
                current_dir -= 4
        elif point[1] == min_y and current_dir % 2 != 0:
            min_y -= 1
            current_dir = current_dir + 1
            if current_dir > 3:
                current_dir -= 4

        # print(point, i + 2)
    print(abs(point[0]) + abs(point[1]))


def part2(data_input):
    mid_point = 5
    grid = np.zeros((mid_point * 2 + 1, mid_point * 2 + 1), dtype=int)
    point = (mid_point, mid_point)
    max_x = max_y = mid_point + 1
    min_x = min_y = mid_point - 1
    current_dir = 0
    grid[point] = 1
    while grid[point] < data_input:
        point = (point[0] + moves[current_dir][0], point[1] + moves[current_dir][1])
        value = np.sum(grid[point[0] - 1: point[0] + 2, point[1] - 1: point[1] + 2])
        grid[point] = value

        if point[0] == max_x and current_dir % 2 == 0:
            max_x += 1
            current_dir = current_dir + 1
        elif point[0] == min_x and current_dir % 2 == 0:
            min_x -= 1
            current_dir = current_dir + 1
        elif point[1] == max_y and current_dir % 2 != 0:
            max_y += 1
            current_dir = current_dir + 1
        elif point[1] == min_y and current_dir % 2 != 0:
            min_y -= 1
            current_dir = current_dir + 1

        if current_dir > 3:
            current_dir -= 4

        # print(point, grid[point])
    print(grid[point])


def main():

    # Get the path name and strip to the last 1 or 2 folder paths
    codePath = os.path.dirname(sys.argv[0])
    absCodePath = os.path.abspath(codePath)
    codeDate = int(absCodePath.split("/")[-1][3:])
    codeYear = int(absCodePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    # global data
    code_data = AOC(codeDate, codeYear, test=testing)
    data_input = code_data.read_lines()
    data_input = parse_input(data_input)

    # part1(data_input)
    part2(data_input)


if __name__ == "__main__":
    main()
