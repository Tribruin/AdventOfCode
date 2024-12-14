from AOC import AOC, getDateYear, addTuples
from TerminalColors import *

testing = True
if testing:
    x_max, y_max = 11, 7
else:
    x_max, y_max = 101, 103


def print_grid(robots):
    robot_pos = [x["pos"] for x in robots]
    for y in range(y_max):
        for x in range(x_max):
            if robot_pos.count((x, y)) == 0:
                print(".", end="")
            else:
                print(robot_pos.count((x, y)), end="")
        print()
    print()


def parse_input(codeInput: AOC):
    result = list()
    for line in codeInput.find_all_ints_in_lines():
        result.append({"pos": (line[0], line[1]), "vel": (line[2], line[3])})
    return result


def make_move(robot):
    pos = robot["pos"]
    vel = robot["vel"]

    check_pos = addTuples(pos, vel)
    new_x = (check_pos[0] + x_max) % x_max
    new_y = (check_pos[1] + y_max) % y_max
    return (new_x, new_y)


def get_quads(robots) -> list():
    x_mid = x_max // 2
    y_mid = y_max // 2

    quads = [(0, 0), (1, 0), (0, 1), (1, 1)]
    quad_contents = {x: [] for x in quads}
    for robot in robots:
        x, y = robot["pos"]
        if x == x_mid or y == y_mid:
            continue
        quad_x = 0 + (x > x_mid)
        quad_y = 0 + (y > y_mid)

        quad_contents[(quad_x, quad_y)].append(robot)
    return quad_contents


def check_for_tree(robots):
    robots_pos = [i["pos"] for i in robots]
    lines = list()
    for y_check in range(y_max):
        line = [(x, y) for (x, y) in robots_pos if y == y_check]
        line = sorted(list(set(line)))
        lines.append(line)

    x_mid = x_max // 2
    is_a_tree = True

    for line in lines:
        line_x = sorted([i[0] for i in line])

        # check if mid_point in line, if not, not a tree


def part1(dataInput):
    moves = 100
    robots = dataInput

    for _ in range(moves):
        for robot in robots:
            robot["pos"] = make_move(robot)

    results = get_quads(robots)
    safety_value = 1
    for quad in results.values():
        safety_value *= len(quad)
    print(safety_value)
    # print_grid(robots)


def part2(dataInput):
    robots = dataInput
    idx = 0
    while True:
        print_grid(robots)
        check_for_tree(robots)
        for robot in robots:
            robot["pos"] = make_move(robot)


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    dataInput = parse_input(codeInput)

    # part1(dataInput)
    part2(dataInput)


if __name__ == "__main__":
    main()
