from AOC import AOC, getDateYear, increaseCountOfDict
from TerminalColors import *

testing = False


def parse_input(codeInput: AOC):
    result = codeInput.find_all_ints_in_lines()
    return result[0]


# The was my first attempt with a brute force and
# maintainng the line. Yea, it is slow and breaks
# for part 2.
#
# def process_blink(rock_line: list) -> list:
#     new_line = list()
#     for rock in rock_line:
#         str_rock = str(rock)
#         str_rock_len = len(str_rock)
#         if rock == 0:
#             new_line.append(1)
#         elif str_rock_len % 2 == 0:
#             num1 = int(str_rock[: str_rock_len // 2])
#             num2 = int(str_rock[str_rock_len // 2 :])
#             new_line = new_line + [num1, num2]
#         else:
#             new_line.append(rock * 2024)
#     return new_line


def process_blink(rock_line: dict) -> dict:

    new_rock_line = rock_line.copy()
    for value, count in rock_line.items():
        if count == 0:
            continue
        str_rock = str(value)
        str_rock_len = len(str_rock)
        if value == 0:
            increaseCountOfDict(new_rock_line, 1, count)

        elif str_rock_len % 2 == 0:
            num1 = int(str_rock[: str_rock_len // 2])
            num2 = int(str_rock[str_rock_len // 2 :])
            increaseCountOfDict(new_rock_line, num1, count)
            increaseCountOfDict(new_rock_line, num2, count)

        else:
            new_value = value * 2024
            increaseCountOfDict(new_rock_line, new_value, count)
        new_rock_line[value] -= count

    final_rock_line = {x: y for x, y in new_rock_line.items() if y > 0}
    return final_rock_line


def print_list_sum(rock_line):
    for value, count in rock_line.items():
        print(f"{value:>10} : {count}")


def part1(dataInput):
    rock_line = dict()
    for idx in dataInput:
        if idx in rock_line.keys():
            rock_line[idx] = +1
        else:
            rock_line[idx] = 1

    count = sum(rock_line.values())

    for idx in range(25):
        new_line = rock_line.copy()
        rock_line = process_blink(new_line)
        count = sum(rock_line.values())
    print(f"Final: {count}")


def part2(dataInput):
    rock_line = dict()
    for idx in dataInput:
        if idx in rock_line.keys():
            rock_line[idx] = +1
        else:
            rock_line[idx] = 1

    count = sum(rock_line.values())

    for idx in range(75):
        new_line = rock_line.copy()
        rock_line = process_blink(new_line)
        count = sum(rock_line.values())
    print(f"Final: {count}")


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
