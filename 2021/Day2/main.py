#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from timeit import timeit

# sys.path.append("/Users/rblount/Scripts/AdventOfCode/tools")

from AOC import AOC

testing = False


def part1():
    horz = 0
    depth = 0
    moves = data.read_lines()
    for move in moves:
        move_parts = move.split()
        if move_parts[0] == "forward":
            horz += int(move_parts[1])
        elif move_parts[0] == "down":
            depth += int(move_parts[1])
        else:
            depth -= int(move_parts[1])
    print(horz * depth)


def part2():
    horz = 0
    depth = 0
    aim = 0
    moves = data.read_lines()
    for move in moves:
        move_parts = move.split()
        if move_parts[0] == "forward":
            horz += int(move_parts[1])
            depth += aim * int(move_parts[1])
        elif move_parts[0] == "down":
            aim += int(move_parts[1])
        else:
            aim -= int(move_parts[1])
    print(horz * depth)


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=testing)

    print(f"Time for Part One: {timeit(part1, number=1)}")
    print(f"Time for Part Two: {timeit(part2, number=1)}")


if __name__ == "__main__":
    main()
