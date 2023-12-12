#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
import numpy as np
from timeit import repeat, timeit
from AOC import AOC

testing = False


class Board:
    def __init__(self, input) -> None:

        self.board = np.zeros((5, 5), dtype=int)
        self.found_numbers = np.full((5, 5), True, dtype=bool)
        self.bingo = False

        for i, line in enumerate(input):
            self.board[i] = [int(x) for x in line.split() if x != " "]

    def check_number(self, number):
        temp_x, temp_y = np.where(self.board == number)
        if len(temp_x) == 0:
            return
        coords = (temp_x[0], temp_y[0])

        self.found_numbers[coords] = False

        return self._check_bingo()

    def _check_bingo(self):

        for i in range(5):
            row = self.found_numbers[i, :].sum()
            column = self.found_numbers[:, i].sum()
            if row == 0 or column == 0:
                self.bingo = True
                return True
        return False


def parse_input(data: AOC):
    input = data.read_lines()

    numbers = [int(x) for x in input[0].split(",")]

    i = 2
    boards = list()
    while i < len(input):
        board_numbers = input[i: i + 5]
        board = Board(board_numbers)
        boards.append(board)
        i += 6

    return numbers, boards


def part1(numbers_called, boards):
    for number in numbers_called:
        for bingo_board in boards:
            bingo = bingo_board.check_number(number)
            if bingo:
                uncalled_numbers = bingo_board.board * bingo_board.found_numbers
                print(uncalled_numbers.sum() * number)
                return


def part2(numbers_called, boards):
    last_result = 0
    for number in numbers_called:
        for bingo_board in boards:
            if not bingo_board.bingo:
                bingo = bingo_board.check_number(number)
                if bingo:
                    uncalled_numbers = bingo_board.board * bingo_board.found_numbers
                    last_result = uncalled_numbers.sum() * number

    print(last_result)


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codePath = os.path.dirname(sys.argv[0])
    absCodePath = os.path.abspath(codePath)
    codeDate = int(absCodePath.split("/")[-1][3:])
    codeYear = int(absCodePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=testing)

    numbers_called, boards = parse_input(data)
    part1(numbers_called, boards)

    numbers_called, boards = parse_input(data)
    part2(numbers_called, boards)


if __name__ == "__main__":
    main()
