#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC

testing = True


def parse_input(code_input):

    moves = [int(x) for x in code_input[0].split(",")]
    return moves


def generate_list():
    if testing:
        list_size = 5
    else:
        list_size = 256
    return [x for x in range(list_size)]


def modify_list(current_list, pos, length):

    if pos+length < len(current_list) + 1:
        pre_list = current_list[:pos]
        sub_list = current_list[pos:pos+length]
        remain_list = current_list[pos+length:]
        new_list = pre_list + sub_list[::-1] + remain_list
    else:
        front_count = (length + pos) % len(current_list)
        back_count = length - front_count
        sub_list = current_list[-back_count:] + current_list[:front_count]
        sub_list = sub_list[::-1]
        remain_list = current_list[front_count: front_count + len(current_list) - length]
        new_list = sub_list[-front_count:] + remain_list + sub_list[:back_count]

    return new_list


def part1(data_input):

    number_list = generate_list()
    moves = data_input
    skip_size = 0
    position = 0

    for length in moves:
        number_list = modify_list(number_list, position, length)
        position = (skip_size + length + position) % len(number_list)
        skip_size += 1

    print(number_list[0] * number_list[1])


def part2(data_input):
    number_list = [x for x in range(256)]
    moves = [ord(x) for x in data_input]
    moves = moves + [17, 31, 73, 47, 23]
    moves = moves * 64
    skip_size = 0
    position = 0

    for length in moves:
        number_list = modify_list(number_list, position, length)
        position = (skip_size + length + position) % len(number_list)
        skip_size += 1

    dense_hash = list()
    for i in range(0, 256, 16):
        xor_list = number_list[i]
        element = number_list[i+1:i+16]
        for k in element:
            xor_list = xor_list ^ number_list[k]
        dense_hash.append(str(hex(xor_list))[2:4])
    print("".join(dense_hash))


def main():

    # Get the path name and strip to the last 1 or 2 folder paths
    codePath = os.path.dirname(sys.argv[0])
    absCodePath = os.path.abspath(codePath)
    codeDate = int(absCodePath.split("/")[-1][3:])
    codeYear = int(absCodePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    # global data
    code_data = AOC(codeDate, codeYear, test=testing)
    data_input = code_data.read_lines()
    data_input = parse_input(data_input)

    part1(data_input)
    # part2(code_data.read_lines()[0])


if __name__ == "__main__":
    main()
