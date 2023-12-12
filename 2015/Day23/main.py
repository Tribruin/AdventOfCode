#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC

testing = False


def parse_input(data: AOC):
    lines = data.read_lines()
    commands = list()
    for line in lines:
        full_cmd = list()
        cmd = line[0:3]
        data = line[4:]
        if cmd in ["jio", "jie"]:
            reg = data[0]
            step = int(data[2:])
            full_cmd = [cmd, reg, step]
        elif cmd == "jmp":
            step = int(data)
            full_cmd = [cmd, step]
        else:
            full_cmd = [cmd, data]
        commands.append(full_cmd)
    return commands


def part1(input):
    registers = {"a": 0, "b": 0}
    counter = 0
    while counter < len(input):
        print(counter, end="")
        command_line = input[counter]
        cmd = command_line[0]
        if cmd == "inc":
            registers[command_line[1]] += 1
            counter += 1
        elif cmd == "hlf":
            registers[command_line[1]] //= 2
            counter += 1
        elif cmd == "tpl":
            registers[command_line[1]] *= 3
            counter += 1
        elif cmd == "jie":
            if registers[command_line[1]] % 2 == 0:
                counter += command_line[2]
            else:
                counter += 1
        elif cmd == "jio":
            if registers[command_line[1]] == 1:
                counter += command_line[2]
            else:
                counter += 1
        elif cmd == "jmp":
            counter += command_line[1]
        print(command_line, registers)

    print(registers["b"])


def part2(input):
    registers = {"a": 1, "b": 0}
    counter = 0
    while counter < len(input):
        print(counter, end="")
        command_line = input[counter]
        cmd = command_line[0]
        if cmd == "inc":
            registers[command_line[1]] += 1
            counter += 1
        elif cmd == "hlf":
            registers[command_line[1]] //= 2
            counter += 1
        elif cmd == "tpl":
            registers[command_line[1]] *= 3
            counter += 1
        elif cmd == "jie":
            if registers[command_line[1]] % 2 == 0:
                counter += command_line[2]
            else:
                counter += 1
        elif cmd == "jio":
            if registers[command_line[1]] == 1:
                counter += command_line[2]
            else:
                counter += 1
        elif cmd == "jmp":
            counter += command_line[1]
        print(command_line, registers)

    print(registers["b"])


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=testing)
    input = parse_input(data)

    part1(input)
    part2(input)


if __name__ == "__main__":
    main()
