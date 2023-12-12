#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC

testing = False


def parse_input(code_input):
    instructions = [x.split() for x in code_input]
    registers = {x[0]: 0 for x in instructions}
    return instructions, registers


def change_register(register, operation, value):
    if operation == "inc":
        registers[register] += int(value)
    else:
        registers[register] -= int(value)
    return


def part1(instructions):

    for instuct in instructions:
        reg_to_change, oper, value, _, reg_to_check, check, value_to_check = instuct
        value_to_check = int(value_to_check)
        if check == ">":
            if registers[reg_to_check] > value_to_check:
                change_register(reg_to_change, oper, value)
        elif check == "<":
            if registers[reg_to_check] < value_to_check:
                change_register(reg_to_change, oper, value)
        elif check == ">=":
            if registers[reg_to_check] >= value_to_check:
                change_register(reg_to_change, oper, value)
        elif check == "<=":
            if registers[reg_to_check] <= value_to_check:
                change_register(reg_to_change, oper, value)
        elif check == "==":
            if registers[reg_to_check] == value_to_check:
                change_register(reg_to_change, oper, value)
        elif check == "!=":
            if registers[reg_to_check] != value_to_check:
                change_register(reg_to_change, oper, value)

    print(max(registers.values()))


def part2(instructions):

    max_value = 0
    for instuct in instructions:
        reg_to_change, oper, value, _, reg_to_check, check, value_to_check = instuct
        value_to_check = int(value_to_check)
        if check == ">":
            if registers[reg_to_check] > value_to_check:
                change_register(reg_to_change, oper, value)
        elif check == "<":
            if registers[reg_to_check] < value_to_check:
                change_register(reg_to_change, oper, value)
        elif check == ">=":
            if registers[reg_to_check] >= value_to_check:
                change_register(reg_to_change, oper, value)
        elif check == "<=":
            if registers[reg_to_check] <= value_to_check:
                change_register(reg_to_change, oper, value)
        elif check == "==":
            if registers[reg_to_check] == value_to_check:
                change_register(reg_to_change, oper, value)
        elif check == "!=":
            if registers[reg_to_check] != value_to_check:
                change_register(reg_to_change, oper, value)
        max_current_value = max(registers.values())
        if max_current_value > max_value:
            max_value = max_current_value

    print(max_value)


def main():

    # Get the path name and strip to the last 1 or 2 folder paths
    codePath = os.path.dirname(sys.argv[0])
    absCodePath = os.path.abspath(codePath)
    codeDate = int(absCodePath.split("/")[-1][3:])
    codeYear = int(absCodePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    # global data
    global registers
    code_data = AOC(codeDate, codeYear, test=testing)
    data_input = code_data.read_lines()
    instructions, registers = parse_input(data_input)

    # part1(instructions)

    part2(instructions)


if __name__ == "__main__":
    main()
