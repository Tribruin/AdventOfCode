#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from collections import deque
from timeit import timeit
from AOC import AOC

testing = False


def part1():
    fish = [int(x) for x in data._read_file().split(",")]
    max_day = 80

    fish_count = [0] * 9
    fish_count = deque(fish_count)

    for i in fish:
        fish_count[i] += 1

    for day in range(1, max_day + 1):
        fish_count.rotate(-1)
        fish_count[6] += fish_count[8]
    print(day, sum(fish_count))


def part2():

    fish = [int(x) for x in data._read_file().split(",")]
    max_day = 256

    fish_count = [0] * 9
    fish_count = deque(fish_count)

    for i in fish:
        fish_count[i] += 1

    for day in range(1, max_day + 1):
        fish_count.rotate(-1)
        fish_count[6] += fish_count[8]
    print(day, sum(fish_count))


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=testing)

    print(timeit(part1, number=1))
    print(timeit(part2, number=1))


if __name__ == "__main__":
    main()
