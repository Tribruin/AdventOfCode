#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
import numpy as np
from timeit import timeit

# sys.path.append("/Users/rblount/Scripts/AdventOfCode/tools")

from AOC import AOC

testing = False


def compute_gamma(lines):

    # lines = [list(x) for x in lines]
    # array = np.asanyarray(lines, dtype=int)
    array = np.genfromtxt(lines, dtype=int, delimiter=1)

    ones = np.count_nonzero(array, axis=0)

    gamma = "".join(["1" if digit >= (len(lines) - digit) else "0" for digit in ones])
    epsilon = "".join(["0" if digit == "1" else "1" for digit in gamma])

    return gamma, epsilon


def part1():
    lines = data.read_lines()
    gamma, epsilon = compute_gamma(lines)
    print(int(gamma, 2) * int(epsilon, 2))


def part2():
    lines = data.read_lines()

    o2rating = lines.copy()
    co2rating = lines.copy()
    line_len = len(lines[0])

    for i in range(line_len):
        o2rating_copy = o2rating.copy()

        gamma, _ = compute_gamma(o2rating)
        char = gamma[i]
        for k in range(len(o2rating) - 1, -1, -1):
            if char != o2rating_copy[k][i]:
                o2rating_copy.pop(k)
        o2rating = o2rating_copy
        if len(o2rating) == 1:
            # print(o2rating[0])
            break

    for i in range(line_len):
        co2rating_copy = co2rating.copy()

        _, epsilon = compute_gamma(co2rating)
        char = epsilon[i]
        for k in range(len(co2rating) - 1, -1, -1):
            if char != co2rating_copy[k][i]:
                co2rating_copy.pop(k)
        co2rating = co2rating_copy
        # co2rating = [x for x in co2rating if x[i] != char]
        if len(co2rating) == 1:
            # print(co2rating[0])
            break

    print(int(o2rating[0], 2) * int(co2rating[0], 2))


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
