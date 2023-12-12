#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC

testing = False

open_markers = ["(", "[", "{", "<"]
close_markers = [")", "]", "}", ">"]
marker_values = [3, 57, 1197, 25137]
corrupt_values = [1, 2, 3, 4]


def part1(data):

    total_sum = 0
    lines_to_remove = list()

    for x, line in enumerate(data):
        current_open_markers = list()
        for i in line:
            if i in open_markers:
                current_open_markers.append(i)
            else:
                last_char = current_open_markers.pop()
                if not open_markers.index(last_char) == close_markers.index(i):
                    total_sum += marker_values[close_markers.index(i)]
                    # print(x, i)
                    lines_to_remove.append(x)
                    break

    print(total_sum)
    return lines_to_remove


def part2(data, corrupt_lines):

    for i in corrupt_lines[::-1]:
        data.pop(i)

    missing_markers_values = list()

    for line in data:
        missing_markers = list()
        current_open_markers = list()
        for i in line:
            if i in open_markers:
                current_open_markers.append(i)
            else:
                last_char = current_open_markers[-1]
                if open_markers.index(last_char) == close_markers.index(i):
                    current_open_markers.pop()

        for i in current_open_markers[::-1]:
            missing_markers.append(close_markers[open_markers.index(i)])

        total_value = 0
        for i in missing_markers:
            total_value *= 5
            total_value += close_markers.index(i) + 1
        missing_markers_values.append(total_value)
        # print(x, total_value)

    missing_markers_values = sorted(missing_markers_values)
    mid_point = len(missing_markers_values) // 2
    print(missing_markers_values[mid_point])


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    code_data = AOC(codeDate, codeYear, test=testing)
    input_data = code_data.read_lines()
    lines = list()
    for line in input_data:
        lines.append([x for x in line])

    corrupt_lines = part1(lines)
    part2(lines, corrupt_lines)


if __name__ == "__main__":
    main()
