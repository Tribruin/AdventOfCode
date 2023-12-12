#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC

testing = False


def parse_input(data_input):
    result = [int(x) for x in data_input]
    return result


def part1(data_input):
    code_length = len(data_input)
    current_counter = steps = 0
    while current_counter < code_length:
        jump = data_input[current_counter]
        data_input[current_counter] += 1
        current_counter += jump
        steps += 1
    print(steps)


def part2(data_input):
    code_length = len(data_input)
    current_counter = steps = 0
    while current_counter < code_length:
        jump = data_input[current_counter]
        if jump < 3:
            data_input[current_counter] += 1
        else:
            data_input[current_counter] -= 1
        current_counter += jump
        steps += 1
    print(steps)


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
