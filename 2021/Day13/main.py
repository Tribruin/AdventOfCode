#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC
import numpy as np

testing = False


def parse_input(data_input):

    coords = list()
    folds = list()
    length = len(data_input)
    i = 0
    while data_input[i] != "":
        x, y = data_input[i].split(",")
        coords.append((int(y), int(x)))
        i += 1

    i += 1
    while i < length:
        line_split = data_input[i].split("=")
        axis, line = line_split[0][-1], int(line_split[1])
        folds.append((axis, line))
        i += 1
    return coords, folds


def print_paper(paper: np.array):
    y_max, x_max = paper.shape

    for y in range(y_max):
        for x in range(x_max):
            if paper[(y, x)]:
                print("█", end="")
            else:
                print(" ", end="")
        print()
    print()


def generate_paper(coords) -> np.array:
    max_size_x = max([x for _, x in coords])
    max_size_y = max([y for y, _ in coords])

    paper = np.zeros((max_size_y + 1, max_size_x + 1), dtype=bool)
    for coord in coords:
        paper[coord] = True

    return paper


def fold_y(paper, fold_line):
    top = paper[:fold_line, :]
    bottom = np.flip(paper[fold_line+1:, :], axis=0)
    top = top + bottom
    return top


def fold_x(paper, fold_line):
    left = paper[:, :fold_line]
    right = np.flip(paper[:, fold_line+1:], axis=1)
    left = left + right
    return left


def part1(coords, folds):
    paper = generate_paper(coords)
    fold = folds[0]
    if fold[0] == 'y':
        paper = fold_y(paper, folds[0][1])
    else:
        paper = fold_x(paper, folds[0][1])
    print(np.sum(paper))


def part2(coords, folds):
    paper = generate_paper(coords)
    for fold in folds:
        if fold[0] == 'y':
            paper = fold_y(paper, fold[1])
        else:
            paper = fold_x(paper, fold[1])
    print_paper(paper)


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    # global data
    code_data = AOC(codeDate, codeYear, test=testing)
    data_input = code_data.read_lines()
    coords, folds = parse_input(data_input)

    part1(coords, folds)
    part2(coords, folds)


if __name__ == "__main__":
    main()
