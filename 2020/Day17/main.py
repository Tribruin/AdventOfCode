import sys
import numpy as np

sys.path.append("/Users/rblount/Scripts/AdventOfCode/2020/tools")

from AOC import AOC


def parse_input(data):
    temp_array = []
    for line in data:
        temp_line = [1 if x == "#" else 0 for x in line]
        temp_array.append(temp_line)
    return [temp_array]


def part1():
    def inc_energy_souce(source):
        shape = np.shape(source)
        z, y, x = shape

        new_array = np.zeros((z + 2, y + 2, x + 2), dtype=int)
        for z1 in range(z):
            for y1 in range(y):
                for x1 in range(x):
                    new_array[z1 + 1][y1 + 1][x1 + 1] = source[z1][y1][x1]
        return new_array

    working_array = energy_source
    for i in range(6):
        working_array = inc_energy_souce(working_array)
        print(working_array)


def part2():
    pass


a = AOC(17, test=True)
data = a.read_lines()
energy_source = parse_input(data)
energy_source = np.asarray(energy_source)
part1()