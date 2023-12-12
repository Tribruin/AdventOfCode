import sys
import os
import re
from AOC import AOC
from TerminalColors import *

testing = True


def parse_input(code_input):
    result = code_input.read_lines()
    return result


def part1(commands):
    outputs = dict()
    bots = dict()

    for command in commands:
        if command.startswith("value"):
            value, bot = [int(x) for x in list(re.findall("\d+", command))]
            bots[bot] = value

    pass


def part2(data_input):
    pass


def main():

    # Get the path name and strip to the last 1 or 2 folder paths
    codePath = os.path.dirname(sys.argv[0])
    absCodePath = os.path.abspath(codePath)
    codeDate = int(absCodePath.split("/")[-1][3:])
    codeYear = int(absCodePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {RED}{codeYear}{ENDCOLOR} - Day {RED}{codeDate}{ENDCOLOR}")

    # global data
    code_input = AOC(codeDate, codeYear, test=testing)
    data_input = parse_input(code_input)

    part1(data_input)
    part2(data_input)


if __name__ == "__main__":
    main()
