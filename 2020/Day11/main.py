import sys

sys.path.append("/Users/rblount/Scripts/AdventOfCode/2020/tools")

from AOC import AOC
from copy import deepcopy


def print_array(array):
    for row in range(len(array)):
        print("".join(array[row]))
    print("")


def Part1(input):
    # Fill the seats
    seating = [list(x) for x in input]
    rows = len(seating)
    columns = len(seating[0])

    while True:
        current_seating = deepcopy(seating)
        for r in range(rows):
            for c in range(columns):
                if not current_seating[r][c] == ".":
                    count = 0
                    for r1 in range(-1, 2):
                        for c1 in range(-1, 2):
                            if (0 <= (r + r1) < rows) and (0 <= (c + c1) < columns):
                                if current_seating[r + r1][c + c1] == "#":
                                    count += 1
                    if current_seating[r][c] == "#":
                        count -= 1
                    if current_seating[r][c] == "L" and count == 0:
                        seating[r][c] = "#"
                    elif current_seating[r][c] == "#" and count >= 4:
                        seating[r][c] = "L"
        # print_array(seating)
        # print(current_seating == seating)
        if current_seating == seating:
            break
    print(sum([x.count("#") for x in current_seating]))


def Part2(input):

    seating = [list(x) for x in input]
    rows = len(seating)
    columns = len(seating[0])
    # print_array(seating)

    while True:
        current_seating = deepcopy(seating)
        for r in range(rows):
            for c in range(columns):
                if not current_seating[r][c] == ".":
                    count = 0
                    for r1 in range(-1, 2):
                        for c1 in range(-1, 2):
                            if (0 <= (r + r1) < rows) and (0 <= (c + c1) < columns):
                                if current_seating[r + r1][c + c1] == "#":
                                    count += 1
                                if current_seating[r + r1][c + c1] == ".":
                                    # pass
                                    for m in range(2, columns):
                                        if (0 <= (r + r1 * m) < rows) and (
                                            0 <= (c + c1 * m) < columns
                                        ):
                                            if (
                                                current_seating[r + r1 * m][c + c1 * m]
                                                == "#"
                                            ):
                                                count += 1
                                                break
                                            elif (
                                                current_seating[r + r1 * m][c + c1 * m]
                                                == "L"
                                            ):
                                                break

                    if current_seating[r][c] == "#":
                        count -= 1
                    if current_seating[r][c] == "L" and count == 0:
                        seating[r][c] = "#"
                    elif current_seating[r][c] == "#" and count >= 5:
                        seating[r][c] = "L"
        # print_array(seating)
        if current_seating == seating:
            break
    print(sum([x.count("#") for x in current_seating]))


a = AOC(11, False)
input_data = a.read_lines()
Part1(input_data)
# Part2(input_data)
