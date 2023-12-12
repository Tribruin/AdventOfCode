import numpy as np
import timeit

# file = "Day3-InputTest.txt"
file = "Day3-Input.txt"


class Slope:
    def __init__(self, filename) -> None:

        with open(file=filename) as f:
            lines = f.readlines()

        self.columns = len(lines[0]) - 1
        self.rows = len(lines)
        self.slope_data = np.zeros((self.rows, self.columns), dtype=bool)
        self.original_slope_data = self.slope_data

        for y in range(self.rows):
            for x in range(self.columns):
                self.slope_data[y][x] = lines[y][x] == "#"
        return

    def extend_slope(self):
        """ Extend the existing array by a copy of the starting array """
        temp_array = np.concatenate((self.slope_data, self.original_slope_data), axis=1)
        self.slope_data = temp_array
        self.columns = len(self.slope_data[0])

    def check_for_trees(self, moves):
        found_trees = 0
        right, down = moves
        y = 0
        x = 0
        while y < self.rows:
            if x >= self.columns:
                self.extend_slope()

            if self.slope_data[y][x]:
                found_trees += 1
                # print(f"Found a tree at ({x}, {y})")
            # else:
            #     print(f"No tree at ({x}, {y})")

            x += right
            y += down
        return found_trees


def part1():

    slope = Slope(file)
    print(slope.check_for_trees((3, 1)))


def part2():
    ski_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = []
    slope = Slope(filename=file)
    for ski_slope in ski_slopes:
        trees.append(slope.check_for_trees(moves=ski_slope))

    print(trees, np.prod(trees))


print(timeit.timeit(part1, number=1))
print(timeit.timeit(part2, number=1))