#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python
import sys
import os
import numpy as np
from timeit import timeit
from AOC import AOC

keypad = np.array([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])
newKeyPad = np.array(
    [
        ["X", "X", "1", "X", "X"],
        ["X", "2", "3", "4", "X"],
        ["5", "6", "7", "8", "9"],
        ["X", "A", "B", "C", "X"],
        ["X", "X", "D", "X", "X"],
    ]
)

moves = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


def add_tuples_part1(tuple1, tuple2) -> tuple:
    x1, y1 = tuple1
    x2, y2 = tuple2
    if (x1 + x2 < 0) or (x1 + x2 > 2):
        x2 = 0
    if (y1 + y2 < 0) or (y1 + y2 > 2):
        y2 = 0
    return (x1 + x2, y1 + y2)


def add_tuples_part2(tuple1, tuple2) -> tuple:
    x1, y1 = tuple1
    x2, y2 = tuple2
    if (x1 + x2 < 0) or (x1 + x2 > 4):
        x2 = 0
    if (y1 + y2 < 0) or (y1 + y2 > 4):
        y2 = 0
    return (x1 + x2, y1 + y2)


def part1():
    keypad_code = ""
    current_digit = (1, 1)
    for digit in movement:
        for move in digit:
            current_digit = add_tuples_part1(current_digit, moves[move])
            # print(keypad[current_digit])
        # print(f"Digit: {keypad[current_digit]}")
        keypad_code += str(keypad[current_digit])
    print(keypad_code)


def part2():
    keypad_code = ""
    current_digit = (2, 0)
    for digit in movement:
        for move in digit:

            new_digit = add_tuples_part2(current_digit, moves[move])
            if newKeyPad[new_digit] != "X":
                current_digit = new_digit

            print(newKeyPad[current_digit])
        print(f"Digit: {newKeyPad[current_digit]}")
        keypad_code += str(newKeyPad[current_digit])
    print(keypad_code)


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=False)
    global movement
    movement = data.read_lines()

    print(f"Time for Part One: {timeit(part1, number=1)}")
    print(f"Time for Part Two: {timeit(part2, number=1)}")


if __name__ == "__main__":
    main()
