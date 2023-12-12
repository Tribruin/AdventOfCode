#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from timeit import timeit

# sys.path.append("/Users/rblount/Scripts/AdventOfCode/tools")

from AOC import AOC

testing = True


class Computer:

    commands = ["cpy", "inc", "dec", "jnz"]

    def __init__(self, command_list) -> None:
        self.command_list = command_list
        self.registers = dict()

    def run_program(self):

        for line in self.command_list:

            command = line[:4]
            if command == "cpy":
                



def part1():
    pass


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
    instructions = data.read_lines()

    print(f"Time for Part One: {timeit(part1, number=1)}")
    print(f"Time for Part Two: {timeit(part2, number=1)}")


if __name__ == "__main__":
    main()
