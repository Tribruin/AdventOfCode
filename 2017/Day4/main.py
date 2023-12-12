#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python

import sys
import os
from AOC import AOC

testing = False


def parse_input(code_input):
    result = list()
    for line in code_input:
        result.append(line.split())
    return result


def part1(data_input):
    count = 0
    for line in data_input:
        if len(line) == len(set(line)):
            count += 1
    print(count)


def part2(data_input):
    count = 0
    for line in data_input:
        new_line = list()
        for word in line:
            sorted_word = [x for x in word]
            sorted_word.sort()
            new_line.append(''.join(sorted_word))
        if len(line) == len(set(new_line)):
            count += 1
        #     print("YES", line)
        # else:
        #     print("NO", line)
    print(count)


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
