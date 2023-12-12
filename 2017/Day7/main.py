#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
import re
from AOC import AOC

testing = False


def parse_input(code_input):

    programs = dict()
    for line in code_input:

        temp_split = line.split(" -> ")
        temp = temp_split[0]
        if len(temp_split) > 1:
            discs = temp_split[1].split(", ")
        else:
            discs = []
        name = temp.split("(")[0][:-1]
        weight = int(temp.split("(")[1][:-1])
        programs[name] = (weight, discs)

    return programs


def part1(data_input):

    working_programs = data_input.copy()

    # First lets eliminate all the top items
    for program, data in data_input.items():
        if len(data[1]) == 0:
            working_programs.pop(program)

    working_programs_copy = working_programs.copy()
    working_programs_copy2 = working_programs.copy()

    for program, data in working_programs_copy.items():
        for _, data2 in working_programs_copy2.items():
            if program in data2[1]:
                working_programs.pop(program)
                break

    bottom_program = list(working_programs.keys())[0]
    print(bottom_program)
    return bottom_program


def part2(data_input, bottom_program):

    def get_weight(sub_tower):
        # print(f"Checking sub-tower {sub_tower}")
        weight = 0
        if len(data_input[sub_tower][1]) == 0:
            return data_input[sub_tower][0]
        else:
            weight = data_input[sub_tower][0]
            for program in data_input[sub_tower][1]:
                weight += get_weight(program)
        return weight

    found = False
    search_tree = data_input[bottom_program]
    while not found:
        weights = list()
        for program in search_tree[1]:
            weight = get_weight(program)
            weights.append(weight)
            print(f"Weight of Tower {program} - {weight}")

        if len(set(weights)) == 1:
            # We found where the programs balance
            found = True
            break
        odd_weight = max(weights)
        weight_diff = max(weights) - min(weights)
        odd_weight_index = weights.index(odd_weight)
        odd_weight_program = search_tree[1][odd_weight_index]
        search_tree = data_input[odd_weight_program]

    # Now we know the element that is odd, lets find the difference in weight
    new_weight = data_input[odd_weight_program][0] - weight_diff
    print(odd_weight_program, new_weight)


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

    bottom = part1(data_input)
    part2(data_input, bottom)


if __name__ == "__main__":
    main()
