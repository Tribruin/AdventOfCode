import re

from AOC import AOC, getDateYear
from TerminalColors import *

testing = False


def parse_input(codeInput: AOC):
    result = codeInput.read_lines()
    return result


def get_vertical_lines(lines: list):
    """Return a list of lines based on the vertical columns
    of a list of strings"""

    vert_lines = list()
    for i in range(len(lines[0])):
        temp_line = str()
        for j in range(len(lines)):
            temp_line += lines[j][i]
        vert_lines.append(temp_line)
    return vert_lines


def get_diag_dn_left(lines: list):
    """Get all the diagnal lines from upper right to lower left"""

    x_len, y_len = len(lines), len(lines[0])
    diag_lines_dn_left = list()
    for y in range(y_len):
        # Get the lines that are formed starting at x(0)
        temp_line = str()
        for i, x in enumerate(range(x_len - 1, y - 1, -1)):
            temp_line += lines[y + i][x]
            # temp_line += lines[y + (x_len - 1 - x)][x - y]
        diag_lines_dn_left.append(temp_line)

    for i, x in enumerate(range(x_len - 2, 0, -1)):
        temp_line = str()
        for y in range(0, y_len - i - 1):
            temp_line += lines[y][x - y]
        diag_lines_dn_left.append(temp_line)

    return diag_lines_dn_left


def get_diag_dn_right(lines: list):
    x_len, y_len = len(lines), len(lines[0])

    diag_lines_dn_right = list()
    for y in range(y_len):
        # Get the lines that are formed starting at x(0)
        temp_line = str()
        for x in range(0, x_len - y):
            temp_line += lines[y + x][x]
        diag_lines_dn_right.append(temp_line)

    for x in range(1, x_len):
        temp_line = str()
        for y in range(0, y_len - x):
            temp_line += lines[y][x + y]
        diag_lines_dn_right.append(temp_line)

    return diag_lines_dn_right


def find_count(all_lines: list, word_match: str):
    """Find the word count both forward and backward in
    a list of lines"""
    total_count = 0
    for whole_line in all_lines:
        # count = whole_line.count(word_match)
        # count += whole_line.count(word_match[::-1])
        found_words = re.findall(word_match, whole_line)
        total_count += len(found_words)
        found_words = re.findall(word_match, whole_line[::-1])
        total_count += len(found_words)
    return total_count


def part1(dataInput):
    lines = dataInput
    word_to_match = r"XMAS"
    total_xmases = 0
    total_xmases = find_count(lines, word_to_match)

    vert_lines = get_vertical_lines(lines)
    total_xmases += find_count(vert_lines, word_to_match)

    diag_lines_dn_right = get_diag_dn_right(lines)
    total_xmases += find_count(diag_lines_dn_right, word_to_match)

    diag_lines_dn_left = get_diag_dn_left(lines)
    total_xmases += find_count(diag_lines_dn_left, word_to_match)

    print(total_xmases)


def part2(dataInput):
    patterns = [("M", "M"), ("S", "M"), ("M", "S"), ("S", "S")]
    match_patterns = [("S", "S"), ("S", "M"), ("M", "S"), ("M", "M")]

    def check_square(line1, line3) -> bool:
        for i, line in enumerate(patterns):
            if line1 == line and line3 == match_patterns[i]:
                return True
        return False

        pass

    lines = dataInput
    x_len, y_len = len(lines[0]), len(lines)
    x_min = y_min = 1
    x_max, y_max = x_len - 1, y_len - 1

    total_xmases = 0
    for y in range(y_min, y_max):
        for x in range(x_min, x_max):
            # Check to see if we are starting on a "A"
            if lines[y][x] == "A":
                line1 = (lines[y - 1][x - 1], lines[y - 1][x + 1])
                line3 = (lines[y + 1][x - 1], lines[y + 1][x + 1])
                if check_square(line1, line3):
                    total_xmases += 1

    print(total_xmases)


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
