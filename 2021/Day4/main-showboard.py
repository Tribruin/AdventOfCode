#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
import numpy as np
from AOC import AOC
from time import sleep
from TerminalColors import *

boards_in_row = 10
board_size = 16
testing = False


class Board:
    def __init__(self, input) -> None:

        self.board = np.zeros((5, 5), dtype=int)
        self.found_numbers = np.full((5, 5), True, dtype=bool)
        self.bingo = False
        self.board_number = 0

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

    def print_board(self):
        indent = board_size * (self.board_number % boards_in_row)
        move_cursor(indent, 0)
        f"{YELLOW} BD# {self.board_number}{ENDCOLOR}"
        if self.bingo:
            print(f"{BRED}", end="")
            title = f"BD#{self.board_number:>3} - BINGO"
        else:
            print(f"{YELLOW}", end="")
            title = f"BD# {self.board_number:>3}"
        print(f"{title:^16}", end="")
        print(f"{ENDCOLOR}")
        y_size, x_size = self.board.shape
        for y in range(y_size):
            move_cursor(indent, 0)
            for x in range(x_size):
                if not self.found_numbers[(y, x)]:
                    print(f"{BGREEN}", end="")
                else:
                    print(f"{RED}", end="")
                print(f"{self.board[(y,x)]:>3}", end="")
            print()
        print(f"{ENDCOLOR}")


def parse_input(data: AOC):
    input = data.read_lines()

    numbers = [int(x) for x in input[0].split(",")]

    i = 2

    boards = list()
    while i < len(input):
        board_numbers = input[i : i + 5]
        board = Board(board_numbers)
        boards.append(board)
        board.board_number = len(boards) - 1
        i += 6

    return numbers, boards


def move_cursor(x, y):
    if x < 0:
        print(f"{CURSORLEFT}" * abs(x), end=y)
    else:
        print(f"{CURSORRIGHT}" * abs(x), end="")
    if y < 0:
        print(f"{CURSORUP}" * abs(y), end="")
    else:
        print(f"{CURSORDOWN}" * abs(y), end="")


def wait_key():
    """ Wait for a key press on the console and return it. """
    result = None
    import termios

    fd = sys.stdin.fileno()
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    try:
        result = sys.stdin.read(1)
    except IOError:
        pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result


def print_boards(boards):
    for board_number, bingo_board in enumerate(boards):
        bingo_board.print_board()
        move_cursor(0, -7)
        if (board_number + 1) % boards_in_row == 0 and board_number != 0:
            move_cursor(0, 6)
            print()


def part1(numbers_called, boards):

    found_bingo = False
    for number in numbers_called:
        print(RESETSCREEN)
        title = f"Calling Number: {number:>3}"
        print(f"{title:^51}\n")
        for bingo_board in boards:
            bingo = bingo_board.check_number(number)
            if bingo:
                uncalled_numbers = bingo_board.board * bingo_board.found_numbers
                found_bingo = True

        print_boards(boards)
        sleep(1)

        if found_bingo:
            result = uncalled_numbers.sum() * number
            print(f"Board #{bingo_board.board_number} - Result: {result}")
            return


def part2(numbers_called, boards):
    last_result = 0
    last_board_number = 0
    for number in numbers_called:
        for bingo_board in boards:
            print(RESETSCREEN)
            title = f"Calling Number: {number:>3}"
            print(f"{title:^51}\n")
            if not bingo_board.bingo:
                bingo = bingo_board.check_number(number)
                if bingo:
                    uncalled_numbers = bingo_board.board * bingo_board.found_numbers
                    last_board_number = bingo_board.board_number
                    last_result = uncalled_numbers.sum() * number

        print_boards(boards)
        sleep(1)

    print(f"Last Board: {last_board_number} - Result: {last_result}")


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=testing)

    numbers_called, boards = parse_input(data)
    part1(numbers_called, boards)

    wait_key()

    numbers_called, boards = parse_input(data)
    part2(numbers_called, boards)


if __name__ == "__main__":
    main()
