import timeit

# file = "Day3-InputTest.txt"
file = "Day3-Input.txt"


class Slope:
    def __init__(self, filename) -> None:

        lines = []
        with open(file=filename) as f:
            for line in f:
                lines.append(line.strip())

        self.columns = len(lines[0])
        self.rows = len(lines)
        self.slope_data = lines

        return

    def check_for_trees(self, moves):
        found_trees = 0
        right, down = moves
        x = 0
        for y in range(0, self.rows, down):
            if self.slope_data[y][x % self.columns] == "#":
                found_trees += 1
            x += right
        return found_trees


def part1():

    slope = Slope(file)
    print(slope.check_for_trees((3, 1)))


def part2():
    ski_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    result = 1
    slope = Slope(filename=file)
    for ski_slope in ski_slopes:
        result *= slope.check_for_trees(moves=ski_slope)
    print(result)


print(timeit.timeit(part1, number=1))
print(timeit.timeit(part2, number=1))