#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from typing import Tuple
from AOC import AOC
import numpy as np

testing = False


def print_array(array: np.array):
    # chars = {True: "█", False: " "}
    chars = {True: "#", False: "."}
    y_max, x_max = array.shape

    for y in range(y_max):
        for x in range(x_max):
            print(f"{chars[array[y,x]]}", end="")
        print()
    print()


def add_tuples(tuple1, tuple2) -> tuple:
    x1, y1 = tuple1
    x2, y2 = tuple2
    return (x1 + x2, y1 + y2)


def parse_input(data_input) -> Tuple[list, np.array]:

    algo_text = data_input[0]
    algo_light = [x for x, y in enumerate(algo_text) if y == "#"]
    image = data_input[2:]
    x_len, y_len = len(image[0]), len(image)
    image_array = np.zeros((y_len, x_len), dtype=bool)

    for y in range(y_len):
        for x in range(x_len):
            image_array[y, x] = True if image[y][x] == "#" else False

    return algo_light, image_array


def process_stage(image_array: np.array, argo_list) -> np.array:
    image_array = np.pad(image_array, 3, mode='constant', constant_values=False)
    print_array(image_array)
    new_array = np.zeros(image_array.shape, dtype=bool)

    x_len, y_len = np.shape(new_array)
    neighbor_array_list = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbor_array = np.array(neighbor_array_list, dtype="i,i")
    neighbor_array = np.reshape(neighbor_array, (3, 3))

    for y in range(1, y_len-1):
        for x in range(1, x_len-1):
            sub_array = image_array[y-1:y+2, x-1:x+2]
            sub_array = np.reshape(sub_array, -1)
            sub_digits = {True: "1", False: "0"}
            bin_digit = [sub_digits[x] for x in sub_array]
            bin_num = int("".join(bin_digit), 2)
            # print((y, x), bin_num)
            new_array[(y, x)] = True if bin_num in argo_list else False

    return new_array


def part1(algo_list, image):
    for _ in range(2):
        image = process_stage(image, algo_list)
        print_array(image)
    print(np.sum(image))


def part2(data_input):
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
    algo, image = parse_input(data_input)

    part1(algo, image)
    part2(data_input)


if __name__ == "__main__":
    main()
