#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from timeit import timeit
import numpy as np

# sys.path.append("/Users/rblount/Scripts/AdventOfCode/tools")

from AOC import AOC

testing = False
chars = [" ", "#"]


class Display:
    def __init__(self, input: list) -> None:

        self.commands = input
        self.display = np.zeros((6, 50), dtype=int)

    def add_rect(self, x, y) -> None:
        self.display[0:y, 0:x] = 1

    def rotate_row(self, row, shift) -> None:
        self.display[row] = np.roll(self.display[row], shift)

    def rotate_column(self, column, shift) -> None:
        column_array = self.display[:, column]
        self.display[:, column] = np.roll(column_array, shift)

    def process_commads(self):

        for command in self.commands:

            # print(command)
            if command[0:4] == "rect":
                x = int(command[5 : command.find("x")])
                y = int(command[command.find("x") + 1 :])
                self.add_rect(x, y)

            else:

                if command[7] == "r":
                    subcommand = command[11:]
                    row = int(subcommand[2 : subcommand.find(" ")])
                    shift = int(subcommand[subcommand.rfind(" ") :])
                    self.rotate_row(row, shift)

                else:
                    subcommand = command[14:]
                    column = int(subcommand[2 : subcommand.find(" ")])
                    shift = int(subcommand[subcommand.rfind(" ") :])
                    self.rotate_column(column, shift)

            # self.print_array()

    def print_array(self):
        y_size, x_size = self.display.shape
        print("-" * x_size)
        for y in range(y_size):
            for x in range(x_size):
                print(chars[self.display[y][x]], end="")
            print()

    def count_on(self):
        print(np.sum(self.display))


def part1():
    tfa_display.count_on()


def part2():
    tfa_display.print_array()


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=testing)
    global tfa_display
    tfa_display = Display(data.read_lines())
    tfa_display.process_commads()

    print(f"Time for Part One: {timeit(part1, number=1)}")
    print(f"Time for Part Two: {timeit(part2, number=1)}")


if __name__ == "__main__":
    main()
