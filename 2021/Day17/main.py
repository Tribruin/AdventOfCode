#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
import re
from AOC import AOC

testing = False


class Projectile:

    def __init__(self, a, b, vel_x, vel_y) -> None:

        self.x_low = a[0]
        self.x_high = a[1]
        self.y_high = b[0]
        self.y_low = b[1]
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.pos = (0, 0)
        self.max_y = 0

    def move_projectile(self):
        self.pos = add_tuples(self.pos, (self.vel_x, self.vel_y))
        self.vel_x = self.vel_x - 1 if self.vel_x >= 1 else 0
        self.vel_y = self.vel_y - 1
        if self.pos[1] > self.max_y:
            self.max_y = self.pos[1]

    def check_pos(self) -> int:
        """Check postition of projectile

        Returns:
            int:
                0 = still in air
                1 = overshot target
                2 = inside target
        """

        x, y = self.pos
        if (self.x_low <= x <= self.x_high) and (self.y_high <= y <= self.y_low):
            # inside target
            return 2

        elif y < self.y_high:
            # overshot target
            return 1

        else:
            return 0


def add_tuples(tuple1, tuple2) -> tuple:
    x1, y1 = tuple1
    x2, y2 = tuple2
    return (x1 + x2, y1 + y2)


def parse_input(data_input):
    numbers = re.findall(r"[-]*\d+", data_input[0])
    return (int(numbers[0]), int(numbers[1])), (int(numbers[2]), int(numbers[3]))


def part1(a, b):

    max_y_height = 0
    for x_vel in range(a[1] // 3, 0, -1):
        for y_vel in range(-a[1], a[1] * 3):

            proj = Projectile(a, b, x_vel, y_vel)
            result = False

            while not result:
                proj.move_projectile()
                result = proj.check_pos()
                if result == 1:
                    pass

                elif result == 2:
                    if proj.max_y > max_y_height:
                        max_y_height = proj.max_y
                        max_vels = (x_vel, y_vel)
    print(f"Max Y: {max_y_height}")
    print(f"Max Velocities {max_vels}")


def part2(a, b):
    valid_vels = 0
    for x_vel in range(a[1] + 1, 0, -1):
        for y_vel in range(b[0], a[1] * 4):
            proj = Projectile(a, b, x_vel, y_vel)
            result = False

            while not result:
                proj.move_projectile()
                result = proj.check_pos()
                if result == 1:
                    pass
                    # print("Overshot Target")
                elif result == 2:
                    # print(f"{x_vel,y_vel}")
                    valid_vels += 1
    print(f"Total Valid Shots {valid_vels}")


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    # global data
    code_data = AOC(codeDate, codeYear, test=testing)
    data_input = code_data.read_lines()
    a, b = parse_input(data_input)

    part1(a, b)
    part2(a, b)


if __name__ == "__main__":
    main()
