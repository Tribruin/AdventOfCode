#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
import numpy as np
from time import sleep
from TerminalColors import *
from AOC import AOC


testing = False
days = 100
COLOR_CYCLE = [BWHITE, BGREEN, BYELLOW, BBLUE, BPURPLE, BCYAN, BRED, GREEN, RED, YELLOW]


def parse_input(data_input: list):

    array = np.genfromtxt(data_input, dtype=int, delimiter=1)
    return array


def print_octupuses(array: np.array, cycle: int, count: int):
    _, x_size = array.shape
    print(f"{RESETSCREEN}")
    print(f"Cycle #: {cycle} : Total Count: {count}")
    for (_, x), val in np.ndenumerate(array):
        # if val >= 10:
        #     print(f"{BRED}", end="")
        # elif val == 0:
        #     print(f"{BGREEN}", end="")
        # else:
        #     print
        print(f"{COLOR_CYCLE[val]}{val:>4}{ENDCOLOR}", end="")
        if x == x_size - 1:
            print()
    print()


def process_cycle(array: np.array):
    y_size, x_size = array.shape
    count = 0
    array += 1
    result = np.where(array > 9)
    array_map = list(zip(result[0], result[1]))
    checked_locations = list()
    while len(array_map) > 0:
        for point in array_map:
            y, x = point
            y_min = y - 1 if y > 0 else 0
            y_max = y + 1 if y < y_size - 1 else y_size - 1
            x_min = x - 1 if x > 0 else 0
            x_max = x + 1 if x < x_size - 1 else x_size - 1
            array[y_min:y_max + 1, x_min:x_max + 1] += 1
        count = np.sum(array >= 10)
        checked_locations += array_map
        new_array_map = [(y, x) for y, x in np.argwhere(array > 9)]
        array_map = list(set(new_array_map).difference(set(checked_locations)))
    array = array * (array < 10)

    return array, count


def part1(array: np.array):
    count = 0
    for cycle in range(1, days + 1):
        array, flash_count = process_cycle(array)
        count += flash_count
        print_octupuses(array, cycle, count)
        sleep(0.1)
    print(f"After {cycle} Days: Total Flashes: {count}")


def part2(array: np.array):
    all_syncd = array.shape[0] * array.shape[1]
    count = 0
    cycle = 1
    while count < all_syncd:
        array, count = process_cycle(array)
        cycle += 1
        print_octupuses(array, cycle, count)
        sleep(0.1)
    print(f"After {cycle} Days: Total Flashes: {count}")


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    # global data
    code_data = AOC(codeDate, codeYear, test=testing)
    data_input = code_data.read_lines()
    data_input = parse_input(data_input)

    part1(data_input)
    input("Press <return> to go to Part 2")
    part2(data_input)


if __name__ == "__main__":
    main()
