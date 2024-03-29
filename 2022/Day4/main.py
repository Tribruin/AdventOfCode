#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC
from TerminalColors import *

testing = False


def parse_input(code_input):
    # result = code_input.split_line_re("[,-]")
    # result = [[int(y) for y in x] for x in result]
    result = code_input.split_line_re_int("[,-]")
    return result


def part1(data_input):
    counter = 0
    for a1, a2, b1, b2 in data_input:
        s1 = [x for x in range(a1, a2 + 1)]
        s2 = [x for x in range(b1, b2 + 1)]
        length = min([len(s1), len(s2)])
        if len(list(set(s1) & set(s2))) == length:
            counter += 1
    print(counter)


def part2(data_input):
    counter = 0
    for a1, a2, b1, b2 in data_input:
        s1 = [x for x in range(a1, a2 + 1)]
        s2 = [x for x in range(b1, b2 + 1)]
        if len(list(set(s1) & set(s2))) > 0:
            counter += 1
    print(counter)


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codePath = os.path.dirname(sys.argv[0])
    absCodePath = os.path.abspath(codePath)
    codeDate = int(absCodePath.split("/")[-1][3:])
    codeYear = int(absCodePath.split("/")[-2])
    print(
        f"Running Advent of Code for Year: {RED}{codeYear}{ENDCOLOR} - Day {RED}{codeDate}{ENDCOLOR}"
    )

    # global data
    code_input = AOC(codeDate, codeYear, test=testing)
    data_input = parse_input(code_input)

    part1(data_input)
    part2(data_input)


if __name__ == "__main__":
    main()
