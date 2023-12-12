import sys

sys.path.append("/Users/rblount/Scripts/AdventOfCode/2020/tools")

from AOC import AOC
from copy import deepcopy


def print_array(array):
    for row in range(len(array)):
        print("".join(array[row]))
    print("")


def Part1():
    def check_surrounding_seats(r, c) -> int:
        count = -1 if current_seating[r][c] == "#" else 0
        count += sum(
            [col[c - 1 : c + 2].count("#") for col in current_seating[r - 1 : r + 2]]
        )
        # count += sum([x.count("#") for x in surround])

        if current_seating[r][c] == "L" and count == 0:
            seating[r][c] = "#"
        elif current_seating[r][c] == "#" and count >= 4:
            seating[r][c] = "L"
        return

    # create the seating arrangement and add an floor around the edges
    seating = [list(x) for x in input_data]
    seating = [["."] + x + ["."] for x in seating]
    seating = [["."] * len(seating[0])] + seating + [["."] * len(seating[0])]
    # print_array(seating)

    rows = len(seating)
    columns = len(seating[0])

    while True:
        current_seating = deepcopy(seating)
        for r in range(1, rows - 1):
            for c in range(1, columns - 1):
                if not current_seating[r][c] == ".":
                    check_surrounding_seats(r, c)
        # print_array(seating)
        # print(current_seating == seating)
        if current_seating == seating:
            break
    print(sum([x.count("#") for x in current_seating]))


def Part2():

    seating = [list(x) for x in input_data]
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
Part1()
# Part2()
