#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC
from statistics import median, mean
from math import floor, ceil

testing = False


def part1(input):
    med = median(input)
    x = 0
    for y in input:
        x += abs(med - y)
    print(x)


def part2(input):
    def power(count):
        return sum(range(count + 1))

    m1, m2 = floor(mean(input)), ceil(mean(input))

    x1 = 0
    for y in input:
        x1 += power(abs(m1 - y))

    x2 = 0
    for y in input:
        x2 += power(abs(m2 - y))

    print(x1, x2)


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=testing)
    input = data.read_int_in_line()

    part1(input)
    part2(input)


if __name__ == "__main__":
    main()
