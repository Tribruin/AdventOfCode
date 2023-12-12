import re
import numpy as np
from itertools import cycle

from math import prod, lcm
from AOC import AOC, getDateYear
from TerminalColors import *


testing = False
start = "AAA"
end = "ZZZ"


def parse_input(codeInput: AOC):
    data = codeInput.read_lines()
    turns = [x for x in data[0]]
    temp = [re.findall("[1-9A-Z]{3}", x) for x in data[2:]]
    moves = {a: {"L": b, "R": c} for a, b, c in temp}

    # for move in data[2:]:
    #     turns.append(re.findall("[A-Z]{3}", move))
    return (turns, moves)


def factors(num):
    factors = []
    for x in range(2, num // 2 + 1):
        if num % x == 0:
            factors.append(x)
    return factors


def part1(dataInput):
    turns, moves = dataInput
    turns = cycle(turns)
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
    cycles = list()

    # Let's figure out the cycle for each starting location
    for startLoc in startLocs:
        count = 0
        currentLoc = startLoc
        moveHistory = [currentLoc]
        i = 0
        while True:
            if currentLoc in endLocs:
                # j = i + 1
                # if j == len(turns):
                #     j = 0
                nextLoc = moves[newLoc][turns[i]]
                locInHistory = moveHistory.index(nextLoc)
                repeatMove = len(moveHistory)
                print(
                    f"StartLoc: {startLoc} - endLoc: {currentLoc} - nextLoc: {nextLoc} - Next Move: {turns[i]} - {locInHistory}, {repeatMove}"
                )
                moveHistory = list()
                if locInHistory == 0:
                    cycles.append(repeatMove)
                    break

            turn = turns[i]
            count += 1
            newLoc = moves[currentLoc][turn]
            moveHistory.append(newLoc)
            # print(f"{turn} : {currentLoc} -> {newLoc} ({count})")
            currentLoc = newLoc

            i += 1
            if i == len(turns):
                i = 0
            currentLoc = newLoc

    print(cycles)
    cycleFactors = list()
    for cycle in cycles:
        cycleFactors += factors(cycle)
    cycleFactorsSet = set(cycleFactors)
    print(cycleFactorsSet)
    print(prod(cycleFactorsSet))
    print(np.lcm.reduce(np.array(cycles)))


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
