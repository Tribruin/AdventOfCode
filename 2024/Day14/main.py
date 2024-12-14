from AOC import AOC, getDateYear, addTuples
from TerminalColors import *
from time import sleep

testing = False
if testing:
    x_max, y_max = 11, 7
else:
    x_max, y_max = 101, 103


def print_grid(robots):
    robot_pos = [x["pos"] for x in robots]
    print(f"{CLEAR}")
    for y in range(y_max):
        for x in range(x_max):
            if robot_pos.count((x, y)) == 0:
                print(" ", end="")
            else:
                # print(robot_pos.count((x, y)), end="")
                print("X", end="")
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


def get_quads(robots) -> list:
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


def check_for_tree(robots, idx):

    # This is a little bit of a cheat since I don't know how
    # the Christmas tree is shaped. So, I used a hint from Reddit
    # that the frame would likely not have any overlapping robots
    # If I get interested, I will resolve by looking for a shape.

    robots_all_pos = [i["pos"] for i in robots]
    robot_pos = sorted(list(set(robots_all_pos)))
    if len(robot_pos) == len(robots_all_pos):
        print_grid(robots)
        print(f"Seconds Elapsed: {idx}")
        sleep(1.0)

    # for y in range(0, y_max):
    #     for x in range(0, x_max + 1):
    #         if (x, y) not in robot_pos:
    #             # No robots, continue to check positions
    #             continue

    #             # Ok, now let's check if the the locations on top and immediate side are clear
    #             # As this is top of the tree
    #             # for neighbor in [(-1,-1), (0,-1), (1,0), [-1,0], [1,0]]


def part1(dataInput):
    moves = 100
    robots = dataInput

    for idx in range(moves):
        for robot in robots:
            robot["pos"] = make_move(robot)

    results = get_quads(robots)
    safety_value = 1
    for quad in results.values():
        safety_value *= len(quad)
    print(safety_value)
    print_grid(robots)
    print(f"Seconds Elapsed: {idx}")


def part2(dataInput):
    idx = 1
    robots = dataInput

    while idx < 10000:
        for robot in robots:
            robot["pos"] = make_move(robot)
        check_for_tree(robots, idx)
        # print_grid(robots)
        # print(f"Seconds Elapsed: {idx}")
        # sleep(0.05)
        idx += 1


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
