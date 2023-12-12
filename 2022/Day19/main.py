
from AOC import AOC, getDateYear
from TerminalColors import *

testing = True


def parse_input(codeInput):
    pass
    return result


def part1(dataInput):
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
