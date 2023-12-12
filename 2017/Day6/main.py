#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC

testing = False


def parse_input(code_input):
    result = [int(x) for x in code_input[0].split()]
    return result


def part1(data_input):
    current_state = data_input
    bank_len = len(current_state)
    found_states = list()
    while current_state not in found_states:
        found_states.append(current_state.copy())
        max_val = max(current_state)
        max_bank = current_state.index(max_val)
        counter = max_bank
        current_state[counter] = 0
        for _ in range(max_val):
            counter += 1
            if counter == bank_len:
                counter -= bank_len
            current_state[counter] += 1
    print(len(found_states))

    # Part 2 Starts here
    # The loop length is the difference between the len of found states and the first time state seen
    found_index = found_states.index(current_state)
    print(len(found_states) - found_index)


def part2(data_input):
    pass


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
