# import sys
from collections import deque
import numpy as np
from math import sqrt

# sys.path.append("/Users/rblount/Scripts/AdventOfCode/tools")

from AOC import AOC

side_orientations = ["T", "B", "L", "R", "FT", "FB", "FL", "FR"]


class Tile:
    def __init__(self, tile_data) -> None:
        self.tile_number = int(tile_data[0][5:9])
        self.tile = np.zeros((10, 10), dtype=int)
        self.found_sides = 0
        for line_no, line in enumerate(tile_data[1:]):
            self.tile[line_no] = np.asarray(
                [1 if line[x] == "#" else 0 for x in range(len(line))]
            )
        # print(f"Tile No: {self.tile_number}")
        top_bin = "".join([f"{x}" for x in self.tile[0]])
        top_bin_rev = top_bin[::-1]
        bottom_bin = "".join([f"{x}" for x in self.tile[9]])
        bottom_bin_rev = bottom_bin[::-1]
        left_bin = "".join([f"{x}" for x in self.tile[:, 0]])
        left_bin_rev = left_bin[::-1]
        right_bin = "".join([f"{x}" for x in self.tile[:, 9]])
        right_bin_rev = right_bin[::-1]
        top_value = int(top_bin, 2)
        top_value_rev = int(top_bin_rev, 2)
        bottom_value = int(bottom_bin, 2)
        bottom_value_rev = int(bottom_bin_rev, 2)
        left_value = int(left_bin, 2)
        left_value_rev = int(left_bin_rev, 2)
        right_value = int(right_bin, 2)
        right_value_rev = int(right_bin_rev, 2)
        self.tile_sides = deque(
            [
                top_value,
                right_value,
                bottom_value,
                left_value,
                top_value_rev,
                bottom_value_rev,
                left_value_rev,
                right_value_rev,
            ]
        )
        self.tile_on_side = deque()
        self.tile_without_borders = np.zeros((8, 8), dtype=int)
        for x in range(1, 9):
            self.tile_without_borders[x - 1] = self.tile[x][1:9]

    def print_tile(self):
        for line in self.tile:
            for bit in line:
                if bit:
                    print("#", end="")
                else:
                    print(".", end="")
            print()

    def find_tiles_on_sides(self):
        for other_tile in puzzle:
            if other_tile != self:
                for side_value in self.tile_sides:
                    if (
                        side_value in other_tile.tile_sides
                        and other_tile not in self.tile_on_side
                    ):
                        # found_sides += 1
                        self.tile_on_side.append(other_tile)
        self.found_sides = len(self.tile_on_side)


def part1():
    side_value = 1
    for tile in puzzle:
        if tile.found_sides == 2:
            side_value *= tile.tile_number
            corner_tiles.append(tile)
    print(side_value)


def part2():
    top_left_corner = corner_tiles[0]

    pass


a = AOC(20, year=2020, test=False)
temp_puzzle = list()
read_tile_data = a.read_lines()
for i in range(0, len(read_tile_data), 12):
    temp_puzzle.append(Tile(read_tile_data[i : i + 11]))
puzzle_size = int(sqrt(len(temp_puzzle)))
puzzle = np.array(temp_puzzle)
for tile in puzzle:
    tile.find_tiles_on_sides()
corner_tiles = deque()
complied_puzzle = np.zeros((puzzle_size, puzzle_size), dtype=int)
part1()
# part2()