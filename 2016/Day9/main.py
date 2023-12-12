#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from timeit import timeit

# sys.path.append("/Users/rblount/Scripts/AdventOfCode/tools")

from AOC import AOC

testing = False


def part1_alt():
    for line in input_data:
        i = 0
        length_of_uncompress_data = 0
        temp_line = line
        while len(temp_line) > 0:
            if temp_line[0] == "(":
                end_of_marker = temp_line.find(")")
                marker = temp_line[1:end_of_marker]
                x_pos = marker.find("x")
                chars = int(marker[:x_pos])
                reps = int(marker[x_pos + 1 :])
                temp_line = temp_line[end_of_marker + 1 + chars :]
                length_of_uncompress_data += chars * reps

            else:
                length_of_uncompress_data += 1
                temp_line = temp_line[1:]
        print(length_of_uncompress_data)


def part1():
    for line in input_data:
        # length = len(line)
        # i = 0
        temp_line = line
        uncompressed_data = ""
        while len(temp_line) > 0:
            if temp_line[0] == "(":
                end_of_marker = temp_line.find(")")
                marker = temp_line[1:end_of_marker]
                x_pos = marker.find("x")
                chars = int(marker[:x_pos])
                reps = int(marker[x_pos + 1 :])
                temp_line = temp_line[end_of_marker + 1 :]
                chars_to_repeat = temp_line[:chars]
                uncompressed_data += chars_to_repeat * reps
                temp_line = temp_line[chars:]

            else:
                uncompressed_data += temp_line[0]
                temp_line = temp_line[1:]
        print(len(uncompressed_data))


def part2():
    def process_marker(marker_reps, string):
        # i = 0
        length_of_uncompress_data = 0
        temp_line = string
        while len(temp_line) > 0:
            if temp_line[0] == "(":
                end_of_marker = temp_line.find(")")
                marker = temp_line[1:end_of_marker]
                x_pos = marker.find("x")
                chars = int(marker[:x_pos])
                reps = int(marker[x_pos + 1 :])
                length_of_uncompress_data += process_marker(
                    reps, temp_line[end_of_marker + 1 : end_of_marker + chars + 1]
                )
                temp_line = temp_line[end_of_marker + 1 + chars :]

            else:
                length_of_uncompress_data += 1
                temp_line = temp_line[1:]
        return marker_reps * length_of_uncompress_data

    for line in input_data:

        print(process_marker(1, line))


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=testing)
    global input_data
    input_data = data.read_lines()

    # print(f"Time for Part One: {timeit(part1, number=1)}")
    print(f"Time for Part One Alt: {timeit(part1_alt, number=1)}")
    print(f"Time for Part Two: {timeit(part2, number=1)}")


if __name__ == "__main__":
    main()
