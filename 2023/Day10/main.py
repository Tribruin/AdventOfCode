from AOC import AOC, getDateYear, addTuples, subtractTuples
from TerminalColors import *

testing = True
pipes = {
    "|": [(0, -1), (0, 1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(-1, 0), (0, -1)],
    "7": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
    ".": [(0, 0), (0, 0)],
}
vertical_pipes = ["|", "L", "J"]
loop_pipes = dict(zip("-|F7LJ", "═║╔╗╚╝"))
non_loop_pipes = dict(zip("-|F7LJ.", "─│┌┐└┘ "))

# reverse_moves = {j: i for i, j in moves.items()}


def find_lenx_leny(locs: list) -> (tuple, tuple):
    minx = min([x[0] for x in locs])
    miny = min([x[1] for x in locs])
    maxx = max([x[0] for x in locs])
    maxy = max([x[1] for x in locs])
    return (minx, miny), (maxx, maxy)


def print_field(
    field: dict,
    start_pipe,
    pipe_path=list(),
    inside_points=list(),
    outside_points=list(),
):
    (minx, miny), (maxx, maxy) = find_lenx_leny(field.keys())
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            pipe = field[(x, y)]["pipe"]
            if (x, y) == start_pipe:
                print(f"{BBLUE}", end="")
                print(f"{pipe}{ENDCOLOR}", end="")
            elif (x, y) in pipe_path:
                print(f"{BCYAN}", end="")
                print(f"{loop_pipes[pipe]}{ENDCOLOR}", end="")
            elif (x, y) in inside_points:
                print(f"{BYELLOW}I{ENDCOLOR}", end="")
            elif (x, y) in outside_points:
                print(f"{BWHITE}O{ENDCOLOR}", end="")
            else:
                print(f"{non_loop_pipes[pipe]}{ENDCOLOR}", end="")
        print()
    print()
    return


def parse_input_part1(code_input: AOC):
    field = dict()

    lines = code_input.read_lines()
    for y, line in enumerate(lines):
        for x, pipe in enumerate(line):
            match pipe:
                case "S":
                    start_pipe = (x, y)
                    field[(x, y)] = {"pipe": "S", "dist": 0}
                case _:
                    field[(x, y)] = {"pipe": pipe, "dist": float("inf")}

    # Find the starting pipe

    found_exits = list()
    for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        known_pipe = addTuples(start_pipe, (x, y))
        if known_pipe not in field.keys():
            continue
        exits = [
            addTuples(known_pipe, move) for move in pipes[field[known_pipe]["pipe"]]
        ]
        if start_pipe in exits:
            found_exits.append((x, y))

    for pipe, move in pipes.items():
        if found_exits == move:
            field[start_pipe]["pipe"] = pipe
            break

    return (start_pipe, field)


def parse_input_part2(code_input: AOC):
    field = dict()

    lines = code_input.read_lines()
    for y, line in enumerate(lines):
        for x, pipe in enumerate(line):
            match pipe:
                case "S":
                    start_pipe = (x, y)
                    field[(x, y)] = {
                        "pipe": "S",
                    }
                case _:
                    field[(x, y)] = {"pipe": pipe}

    # Find the starting pipe

    found_exits = list()
    for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        known_pipe = addTuples(start_pipe, (x, y))
        if known_pipe not in field.keys():
            continue
        exits = [
            addTuples(known_pipe, move) for move in pipes[field[known_pipe]["pipe"]]
        ]
        if start_pipe in exits:
            found_exits.append((x, y))

    for pipe, move in pipes.items():
        if found_exits == move:
            field[start_pipe]["pipe"] = pipe
            break

    pipe_path = [start_pipe]
    current_pipe = start_pipe
    next_move = pipes[field[current_pipe]["pipe"]][0]
    next_pipe = addTuples(start_pipe, next_move)
    entrance = start_pipe
    finished = False

    while not finished:
        pipe_path.append(next_pipe)
        pos_exits = [addTuples(next_pipe, x) for x in pipes[field[next_pipe]["pipe"]]]
        pos_exits.remove(entrance)
        entrance = next_pipe
        next_pipe = pos_exits[0]
        if next_pipe == start_pipe:
            finished = True

    # # Fill the outedge with Os to indicate they are connected to the Outside. We will need that later.
    # (minx, miny), (maxx, maxy) = find_lenx_leny(field.keys())
    # for x in range(minx - 1, maxx + 2):
    #     field[(x, miny - 1)] = {"pipe": "O"}
    #     field[(x, maxy + 1)] = {"pipe": "O"}

    # for y in range(miny, maxy + 1):
    #     field[(minx - 1, y)] = {"pipe": "O"}
    #     field[(maxx + 1, y)] = {"pipe": "O"}

    # print("Starting Position")
    print_field(field, start_pipe=start_pipe, pipe_path=pipe_path)
    return (start_pipe, field, pipe_path)


def part1(dataInput: tuple):
    start_pos, field = dataInput
    next_pos = [
        (addTuples(start_pos, move), start_pos)
        for move in pipes[field[start_pos]["pipe"]]
    ]
    count = 0
    finished = False
    while not finished:
        temp_next_pos = list()
        count += 1
        for current_pos, entrance in next_pos:
            if field[current_pos]["dist"] > count or field[current_pos][
                "dist"
            ] == float("inf"):
                field[current_pos]["dist"] = count
            # entrance = subtractTuples(last_pos, current_pos)
            pos_exits = [
                addTuples(current_pos, x) for x in pipes[field[current_pos]["pipe"]]
            ]
            pos_exits.remove(entrance)
            next_exit = pos_exits[0]
            # print(
            #     current_pos,
            #     field[current_pos]["pipe"],
            #     field[current_pos]["dist"],
            #     entrance,
            #     next_exit,
            # )
            temp_next_pos.append((next_exit, current_pos))
            if next_exit == start_pos:
                finished = True

        next_pos = temp_next_pos

    highest_value = max(
        [x["dist"] for x in field.values() if x["dist"] != float("inf")]
    )
    print(highest_value)


def part2(dataInput):
    def check_if_inside(pos, field, pipe_path):
        # Reference https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/
        # But, only check for veriticals that have a north component. That fixes the issue with
        # duplicate counting.

        # First check is the pos is on the line
        # print_field(field=field, start_pipe=pos, pipe_path=pipe_path)
        # print(f"Checking Point {pos} - ", end="")
        (x, y) = pos
        if pos in pipe_path:
            # We don't care about the pipes in the loop
            # print(f"{BLUE}Point on Pipe{ENDCOLOR}")
            return False

        (minx, _), (maxx, _) = find_lenx_leny(field)
        count_crossings = 0

        for x1 in range(minx, x):
            if (x1, y) in pipe_path and field[(x1, y)]["pipe"] in vertical_pipes:
                count_crossings += 1

        if count_crossings % 2 == 0:
            # print(f"{RED}Point Outside{ENDCOLOR}")
            return False
        else:
            # print(f"{GREEN}Point Inside{ENDCOLOR}")
            return True

    start_pos, field, pipe_path = dataInput
    (minx, miny), (maxx, maxy) = find_lenx_leny(field)
    points_inside = list()
    points_outside = list()
    points_inside_count = 0
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            if check_if_inside(
                pos=(x, y),
                field=field,
                pipe_path=pipe_path,
            ):
                points_inside_count += 1
                points_inside.append((x, y))
            else:
                points_outside.append((x, y))
            # print(f"Found Inside Points: {points_inside_count}")
            # print()

    print(points_inside_count)

    # # First lets find all the positions and determine if they can reach the edge
    # neighbor_moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    # pos_to_check = field.keys()
    # for pos in pos_to_check:
    #     if field[pos]["pipe"] == "O":
    #         # Already Checked, moving on
    #         break
    #     if field[pos]["pipe"] == ".":
    #         for move in neighbor_moves:
    #             test_pos = addTuples(pos, move)
    #             if field[test_pos]["pipe"] == "O":
    #                 field[pos]["pipe"] = "O"
    #                 break
    #     print(f"Checked: {pos}")
    #     print_field(field, pos)

    # print_field(field=field, start_pipe=start_pos)


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)

    # dataInput = parse_input_part1(codeInput)
    # part1(dataInput)

    dataInput = parse_input_part2(codeInput)
    part2(dataInput)


if __name__ == "__main__":
    main()
