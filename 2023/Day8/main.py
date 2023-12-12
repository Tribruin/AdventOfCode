import re
from itertools import cycle
from AOC import AOC, getDateYear
from TerminalColors import *


testing = False
start = "AAA"
end = "ZZZ"


def parse_input(codeInput: AOC):
    data = codeInput.read_lines()
    turns = cycle([x for x in data[0]])
    temp = [re.findall("[1-9A-Z]{3}", x) for x in data[2:]]
    moves = {a: {"L": b, "R": c} for a, b, c in temp}

    # for move in data[2:]:
    #     turns.append(re.findall("[A-Z]{3}", move))
    return (turns, moves)


def part1(dataInput):
    turns, moves = dataInput
    currentLoc = start
    count = 0
    for turn in turns:
        count += 1
        # print(f"{turn} : {currentLoc} -> {moves[currentLoc][turn]}")
        currentLoc = moves[currentLoc][turn]
        if currentLoc == end:
            break
    print(count)


def part2(dataInput):
    turns, moves = dataInput
    startLocs = [x for x in moves.keys() if x[2] == "A"]
    endLocs = [x for x in moves.keys() if x[2] == "Z"]
    currentLocs = [x for x in startLocs]
    count = 0
    for turn in turns:
        count += 1
        newLocs = list()
        finished = True
        for currentLoc in currentLocs:
            newLoc = moves[currentLoc][turn]
            newLocs.append(newLoc)
            if newLoc not in endLocs:
                finished = False
            # print(f"{turn} : {currentLoc} -> {newLoc}")
        currentLocs = newLocs
        if finished:
            break
    print(count)


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    dataInput = parse_input(codeInput)

    # part1(dataInput)
    part2(dataInput)


if __name__ == "__main__":
    main()
