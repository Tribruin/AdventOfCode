import sys

sys.path.append("/Users/rblount/Scripts/AdventOfCode/2020/tools")

from AOC import AOC

move_options = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}
move_directions = list(move_options.values())
dir_chars = list(move_options.keys())
turn_chars = ["L", "R"]
move_char = ["F"]


class Ferry_Nav:
    def __init__(self):
        self.x, self.y = 0, 0
        self.wp_x, self.wp_y = 10, -1
        self.move_x, self.move_y = move_options["E"]

    def turn_ferry(self, direction, degrees):
        for _ in range(degrees // 90):
            if direction == "R":
                self.move_x, self.move_y = -self.move_y, self.move_x
            else:
                self.move_x, self.move_y = self.move_y, -self.move_x
        return

    def move_ferry(self, direction, move_value):
        x1, y1 = move_options[direction]
        self.x += x1 * move_value
        self.y += y1 * move_value

    def forward_part1(self, move_value):
        x1, y1 = self.move_x, self.move_y
        self.x, self.y = self.x + x1 * move_value, self.y + y1 * move_value

    def move_waypoint(self, direction, move_value):
        x1, y1 = move_options[direction]
        self.wp_x += x1 * move_value
        self.wp_y += y1 * move_value

    def forward_part2(self, move_value):
        self.x, self.y = (
            self.x + self.wp_x * move_value,
            self.y + self.wp_y * move_value,
        )

    def turn_waypoint(self, direction, degrees):
        for _ in range(degrees // 90):
            if direction == "R":
                self.wp_x, self.wp_y = -self.wp_y, self.wp_x
            else:
                self.wp_x, self.wp_y = self.wp_y, -self.wp_x

    def manhattan_dist(self):
        return abs(self.x) + abs(self.y)


def part1():

    ferry = Ferry_Nav()
    for step in steps:
        char, value = step["move"], step["value"]
        # print(f"{char}{value}: ", end="")

        if char in dir_chars:
            ferry.move_ferry(char, value)
        elif char in turn_chars:
            ferry.turn_ferry(char, value)
        else:
            ferry.forward_part1(value)
        # print(f"x={ferry.x} y={ferry.y} dir={ferry.direction}")

    print(ferry.x, ferry.y, ferry.manhattan_dist())


def part2():
    ferry = Ferry_Nav()
    for step in steps:
        char, value = step["move"], step["value"]
        # print(f"{char}{value}: ", end="")
        if char in dir_chars:
            ferry.move_waypoint(char, value)
        elif char in turn_chars:
            ferry.turn_waypoint(char, value)
        else:
            ferry.forward_part2(value)
        # print(f"x={ferry.x} y={ferry.y} wp_x = {ferry.wp_x} wp_y = {ferry.wp_y}")

    print(ferry.x, ferry.y, ferry.manhattan_dist())


a = AOC(12, test=False)
steps = [{"move": x[0], "value": int(x[1:])} for x in a.read_lines()]
part1()
part2()