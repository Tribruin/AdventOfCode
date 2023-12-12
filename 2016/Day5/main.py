#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
import hashlib
from timeit import timeit

# sys.path.append("/Users/rblount/Scripts/AdventOfCode/tools")

from AOC import AOC


def part1():
    index = 0
    for digit in range(8):
        digit_found = False
        while not digit_found:
            check_hash_input = input_data + str(index)
            hash = hashlib.md5(check_hash_input.encode()).hexdigest()
            if hash[0:5] == "00000":
                print(hash[5], end="")
                digit_found = True
            index += 1
    print()


def part2():
    index = 0
    password = ["-", "-", "-", "-", "-", "-", "-", "-"]
    for digit in range(8):
        digit_found = False
        while not digit_found:
            check_hash_input = input_data + str(index)
            hash = hashlib.md5(check_hash_input.encode()).hexdigest()
            if hash[0:5] == "00000":
                digit_pos = int(hash[5], 16)
                if digit_pos < 8 and password[digit_pos] == "-":
                    digit = hash[6]
                    password[digit_pos] = str(digit)
                    print("".join(password))
                    digit_found = True
            index += 1
    print()


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=False)
    global input_data
    input_data = data.read_lines()[0]

    # print(f"Time for Part One: {timeit(part1, number=1)}")
    print(f"Time for Part Two: {timeit(part2, number=1)}")


if __name__ == "__main__":
    main()
