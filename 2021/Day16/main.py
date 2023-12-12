#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC

testing = True
hex2bin = dict()
for i in range(16):
    hex2bin[f"{i:x}".upper()] = f"{i:04b}"


def parse_input(data_input):
    result = ""
    for i in data_input[0]:
        result += f"{hex2bin[i]}"
    return result


def parse_literal(code) -> int:

    numbers = list()
    final_numbers = list()
    while int(code, 2) > 0:

        # leading_digit, partial_code = code[0], code[1:5]
        code_len = 0

        finished = False

        while not finished:
            leading_digit, partial_code = code[0], code[1:5]
            numbers.append(int(partial_code, 2))
            code_len += 5
            if leading_digit == "0":
                finished = True
                code = code[5:]
            else:
                code = code[5:]

        joined_code = "".join([f"{x:04b}" for x in numbers])
        final_numbers.append(int(joined_code, 2))

    return final_numbers, code_len


def split_code(code):

    numbers = list()

    V, T = int(code[0:3], 2), int(code[3:6], 2)
    code = code[6:]

    if T == 4:
        while int(code, 2) > 0:
            found_numbers, used_bits = parse_literal(code)
            numbers += found_numbers
            code = code[used_bits:]

        return numbers
    else:
        if code[0] == '0':
            bit_length = 15
        else:
            bit_length = 11
        # code = code[bit_length + 1:]
        sub_code_len = int(code[1:bit_length + 1], 2)
        sub_code = code[:sub_code_len]
        found_numbers, used_bits = split_code(sub_code)
        numbers += found_numbers


def part1(code):
    values = list()
    result = split_code(code)
    # print(V, T)
    print(result)


def part2(code):
    pass


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    # global data
    code_data = AOC(codeDate, codeYear, test=testing)
    data_input = code_data.read_lines()
    data_input = parse_input(data_input)

    part1(data_input)
    part2(data_input)


if __name__ == "__main__":
    main()
