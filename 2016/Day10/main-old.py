#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from timeit import timeit

# sys.path.append("/Users/rblount/Scripts/AdventOfCode/tools")

from AOC import AOC

testing = True
v1 = 5
v2 = 2


def part1():
    def check_bots(bots):
        for name, chips in bots.items():
            if v1 in chips and v2 in chips:
                print(f"Found bot: {name}")

    bots = dict()

    # Initalize Bots
    left_over_data = list()
    for line in code_data_initial:
        if line.startswith("value"):
            line_stripped = line[6:]
            chip_val = int(line_stripped[: line_stripped.find(" ")])
            bot_num = "B" + line_stripped[line_stripped.rfind(" ") :].strip()
            if not bot_num in bots.keys():
                bots[bot_num] = list()
            bots[bot_num].append(chip_val)
        else:
            left_over_data.append(line)

    code_data = left_over_data

    # Process the exchanges
    for line in code_data:

        # First check if any of the bots have the required two chips

        check_bots(bots)

        if line.startswith("bot"):
            line_stripped = line[4:]
            bot_num = "B" + line_stripped[: line_stripped.find(" ")]
            line_stripped = line_stripped[line_stripped.find(" ") + 14 :]

            # Find the Low Bot/Output
            if line_stripped.startswith("bot"):
                line_stripped = "B" + line_stripped[4:]
                low_bot = line_stripped[: line_stripped.find(" ")]
                # line_stripped = line_stripped[line_stripped.find(" ") + 1 :]
            else:
                line_stripped = line_stripped[7:]
                low_bot = "O" + line_stripped[: line_stripped.find(" ")]

            line_stripped = line_stripped[line_stripped.find(" ") + 13 :]

            # Find the High Bot/Output
            if line_stripped.startswith("bot"):
                line_stripped = line_stripped[4:]
                high_bot = "B" + line_stripped
                # line_stripped = line_stripped[line_stripped.find(" ") + 1 :]
            else:
                line_stripped = line_stripped[7:]
                high_bot = "O" + line_stripped

            # Now lets transfer the values
            values_to_tansfer = sorted(bots[bot_num])
            low_value = values_to_tansfer[0]
            high_value = values_to_tansfer[-1]

            if low_bot not in bots.keys():
                bots[low_bot] = list()
            bots[low_bot].append(low_value)

            if high_bot not in bots.keys():
                bots[high_bot] = list()

            bots[high_bot].append(high_value)
            bots[bot_num] = []

    print(bots)


def part2():
    pass


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=testing)
    global code_data_initial
    code_data_initial = data.read_lines()

    print(f"Time for Part One: {timeit(part1, number=1)}")
    print(f"Time for Part Two: {timeit(part2, number=1)}")


if __name__ == "__main__":
    main()
