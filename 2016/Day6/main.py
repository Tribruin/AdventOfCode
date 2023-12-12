#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
import string
from timeit import timeit

# import numpy as np

# sys.path.append("/Users/rblount/Scripts/AdventOfCode/tools")

from AOC import AOC

testing = False


def find_max_letter_count(word):

    alphabet = string.ascii_lowercase
    dictionary = {}

    for letters in alphabet:
        dictionary[letters] = 0

    for letters in word:
        dictionary[letters] += 1

    dictionary = sorted(dictionary.items(), reverse=True, key=lambda x: x[1])
    x, y = dictionary[0]
    print(x, end="")


def find_min_letter_count(word):

    alphabet = string.ascii_lowercase
    dictionary = {}

    for letters in alphabet:
        dictionary[letters] = 0

    for letters in word:
        dictionary[letters] += 1

    dictionary = sorted(dictionary.items(), reverse=False, key=lambda x: x[1])

    for position in range(0, 26):
        x, y = dictionary[position]
        if not y == 0:
            print(x, end="")
            break


def part1():
    for column in code_array:
        find_max_letter_count(column)
    print()


def part2():
    for column in code_array:
        find_min_letter_count(column)
    print()


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=testing)
    global code_array
    code_array = list()
    lines = data.read_lines()
    for i in range(len(lines[0])):
        temp_array = list()
        for k in range(len(lines)):
            temp_array += lines[k][i]
        code_array.append("".join(temp_array))

    print(f"Time for Part One: {timeit(part1, number=1)}")
    print(f"Time for Part Two: {timeit(part2, number=1)}")


if __name__ == "__main__":
    main()
