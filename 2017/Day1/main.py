#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC

testing = False


def parse_input(code_input):
    result = 0
    pass
    return result


def part1(data_input):
    data_input = data_input + data_input[0]
    consect_numbers = list()
    for i in range(0, len(data_input) - 1):
        if data_input[i] == data_input[i+1]:
            consect_numbers.append(int(data_input[i]))
    print(sum(consect_numbers))


def part2(data_input):
    data_len = len(data_input)
    half_data_len = data_len // 2
    data_input = data_input + data_input
    consect_numbers = list()
    for i in range(0, data_len):
        if data_input[i] == data_input[i+half_data_len]:
            consect_numbers.append(int(data_input[i]))
    print(sum(consect_numbers))


def main():

    # Get the path name and strip to the last 1 or 2 folder paths
    codePath = os.path.dirname(sys.argv[0])
    absCodePath = os.path.abspath(codePath)
    codeDate = int(absCodePath.split("/")[-1][3:])
    codeYear = int(absCodePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    # global data
    code_data = AOC(codeDate, codeYear, test=testing)
    data_input = code_data.read_lines()[0]
    # data_input = parse_input(data_input)

    part1(data_input)
    part2(data_input)


if __name__ == "__main__":
    main()
