#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC
from collections import deque
import re

from TerminalColors import CURSORUP

testing = False


class Player:

    def __init__(self, start_pos) -> None:

        self.pos = start_pos
        self.score = 0

    def make_move(self, die_rolls: list) -> None:
        move = sum(die_rolls)
        net_move = move % 10
        self.pos = self.pos + net_move - 10 * (self.pos + net_move > 10)
        self.score += self.pos


def parse_input(data_input):
    result = list()
    for line in data_input:
        result.append(int(re.findall('[0-9]+', line)[-1]))
    return result


def part1(starting_pos):
    P1 = Player(starting_pos[0])
    P2 = Player(starting_pos[1])

    current_die = 1

    while True:
        die_rolls = [current_die, current_die+1, current_die+2]
        P1.make_move(die_rolls)
        if P1.score >= 1000:
            break

        current_die += 3
        die_rolls = [current_die, current_die+1, current_die+2]
        P2.make_move(die_rolls)
        if P2.score >= 1000:
            break

        current_die += 3

    print(f"P1 Score: {P1.score}")
    print(f"P2 Score: {P2.score}")
    print(f"Last Die Roll: {die_rolls[-1]}")
    if P1.score >= 1000:
        print(P2.score * die_rolls[-1])
    else:
        print(P1.score * die_rolls[-1])


def part2(data_input):
    pass


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
    part2(data_input)


if __name__ == "__main__":
    main()
