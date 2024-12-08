from AOC import AOC, getDateYear, addTuples
from TerminalColors import *

testing = False
moves = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
move_dirs = list(moves.keys())


def parse_input(codeInput: AOC):
    matrix = codeInput.read_lines()
    max_y, max_x = len(matrix), len(matrix[0])
    obstacles = list()
    for y in range(max_y):
        for x in range(max_x):
            if matrix[y][x] == "#":
                obstacles.append((y, x))
            elif matrix[y][x] in move_dirs:
                guard = ((y, x), matrix[y][x])
    return obstacles, guard, (max_y, max_x)


def rotate_gaurd(current_dir):
    """Take the current guard direction and then rotate based
    on the specified pattern (u/r/d/l)"""
    idx = move_dirs.index(current_dir)
    new_dir = move_dirs[(idx + 1) % 4]  # (idx + 1) % 4 returns 0,1,2,3,0,1,2,3,etc
    return new_dir


def check_and_move(obstacles, guard, maxes):
    """Attempt to move the guard by one space in the current directoion
    If next move is an obstacle, rotate the gaurd until they can move and move
    Check if the guard moves outside the specified map and return True if
    guard moves out of bounds."""
    max_y, max_x = maxes
    guard_pos, guard_dir = guard
    open_pos = False
    while not open_pos:
        new_pos = addTuples(guard_pos, moves[guard_dir])
        if new_pos in obstacles:
            guard_dir = rotate_gaurd(guard_dir)
        else:
            guard_pos = new_pos
            open_pos = True
    if 0 <= guard_pos[0] < max_y and 0 <= guard_pos[1] < max_x:
        out_bounds = False
    else:
        out_bounds = True
    return out_bounds, (guard_pos, guard_dir)


def part1(obstacles, guard, maxes):
    sqs_covered = list()
    sqs_covered.append(guard[0])
    found_edge = False
    # print(guard[0], guard[1])
    while not found_edge:
        found_edge, guard = check_and_move(obstacles, guard, maxes)
        if not found_edge:
            sqs_covered.append(guard[0])
        # print(guard[0], guard[1])
    print(len(set(sqs_covered)))
    return list(set(sqs_covered))


def part2(obstacles, guard, maxes):

    # Only test locations in the original path for obstacles.
    # Otherwise, the guard would never hit the spot

    poss_new_obs = part1(obstacles, guard, maxes)
    poss_new_obs.remove(guard[0])
    guard_org = guard
    valid_obs_locs = 0

    # TODO: Rework to only check locations after the new obstacle
    # Becuase the path would be the same prior to that!

    for new_obs in poss_new_obs:
        guard = guard_org
        # print(f"Checking: {new_obs}", end="")
        new_obstacles = obstacles + [new_obs]
        past_guard_pos = [guard]
        found_edge = False
        # print(guard[0], guard[1])
        while not found_edge:
            found_edge, guard = check_and_move(new_obstacles, guard, maxes)
            if guard in past_guard_pos:
                valid_obs_locs += 1
                found_edge = True
                print(f"{BRED}Found {new_obs}{ENDCOLOR}")
            else:
                past_guard_pos.append(guard)
        # print()
    print(valid_obs_locs)


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    obstacles, guard, maxes = parse_input(codeInput)

    # part1(obstacles, guard, maxes)
    part2(obstacles, guard, maxes)


if __name__ == "__main__":
    main()
