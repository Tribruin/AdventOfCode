from AOC import AOC, getDateYear
from os import path
from TerminalColors import *

testing = False


def parse_input(codeInput: AOC):
    lines = codeInput.find_all_ints_in_lines()
    # list1 = [x[0] for x in lines]
    # list2 = [x[1] for x in lines]
    list1, list2 = map(list, zip(*lines))

    return (list1, list2)


def part1(dataInput):
    list1, list2 = dataInput
    list1 = sorted(list1)
    list2 = sorted(list2)
    total = 0
    for i, _ in enumerate(list1):
        total += abs(list2[i] - list1[i])
    print(total)


def part2(dataInput):
    list1, list2 = dataInput
    counts = {x: list2.count(x) for x in list2}
    total = 0
    for x in list1:
        total += x * counts.get(x, 0)
    print(total)


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
