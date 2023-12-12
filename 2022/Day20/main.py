
from copy import deepcopy
from collections import deque
from AOC import AOC, getDateYear
from TerminalColors import *

testing = True


def parse_input(codeInput):
    result = codeInput.read_lines()
    result = list(map(int, result))
    return result


def part1(dataInput):
    currentList = deepcopy(deque(dataInput))
    source = deepcopy(dataInput)
    for move in source:

    pass


def part2(dataInput):
    pass


def main():

    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    dataInput = parse_input(codeInput)

    part1(dataInput)
    part2(dataInput)


if __name__ == "__main__":
    main()
