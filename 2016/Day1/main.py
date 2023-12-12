#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from collections import deque
from timeit import timeit

# sys.path.append("/Users/rblount/Scripts/AdventOfCode/tools")

from AOC import AOC

move_delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
move_names = ["N", "E", "S", "W"]


def add_tuples(tuple1, tuple2) -> tuple:
    x1, y1 = tuple1
    x2, y2 = tuple2
    return (x1 + x2, y1 + y2)


def multiple_tuples(tuple1, tuple2) -> tuple:
    x1, y1 = tuple1
    x2, y2 = tuple2
    return (x1 * x2, y1 * y2)


def part1():
    position = (0, 0)
    orientation = 0
    for move in moves:
        turn = move[0]
        dist = int(move[1:])
        if turn == "L":
            orientation -= 1
            if orientation < 0:
                orientation = 3
        else:
            orientation += 1
            if orientation > 3:
                orientation = 0
        move_dist = multiple_tuples((dist, dist), move_delta[orientation])
        position = add_tuples(position, move_dist)
    x, y = position
    print(abs(x) + abs(y))


def part2():
    position = (0, 0)
    visited_positions = [(0, 0)]
    orientation = 0
    for move in moves:
        turn = move[0]
        dist = int(move[1:])
        if turn == "L":
            orientation -= 1
            if orientation < 0:
                orientation = 3
        else:
            orientation += 1
            if orientation > 3:
                orientation = 0
        for i in range(dist):
            position = add_tuples(position, move_delta[orientation])
            if position in visited_positions:
                x, y = position
                print(abs(x) + abs(y))
                return

            visited_positions.append(position)
    return


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=False)
    global moves
    moves = data.split_line()

    print(f"Time for Part One: {timeit(part1, number=1)}")
    print(f"Time for Part Two: {timeit(part2, number=1)}")
    # print(timeit(part1, number=1))
    # print(timeit(part2, number=1))


if __name__ == "__main__":
    main()
