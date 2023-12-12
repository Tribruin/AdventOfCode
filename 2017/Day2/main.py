#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC

testing = False


def parse_input(code_input):
    result = list()
    for line in code_input:
        new_line = [int(x) for x in line.split()]
        result.append(new_line)
    return result


def part1(data_input):
    checksum = 0
    for line in data_input:
        max_value = max(line)
        min_value = min(line)
        checksum += max_value - min_value
    print(checksum)


def part2(data_input):
    checksum = 0
    for line in data_input:
        line.sort(reverse=True)
        line_len = len(line)
        for i in range(line_len):
            for j in range(i+1, line_len):
                if line[i] % line[j] == 0:
                    checksum += line[i] // line[j]
                    break
    print(checksum)


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

    part1(data_input)
    part2(data_input)


if __name__ == "__main__":
    main()
