from AOC import AOC, getDateYear, getMaxYMaxX, addTuples, insideGrid
from TerminalColors import *

testing = False
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
max_y = max_x = 0
all_paths = list()


# Recursive DFS function
def dfs_recursive(tree, node, visited=None):
    if visited is None:
        visited = list()  # Initialize the visited set
    visited.append(node)  # Mark the node as visited
    if tree[node]["val"] == 9:
        all_paths.append(visited.copy())
        # print(f"{RED}{visited}{ENDCOLOR}")
        return
    children = tree[node]["neigh"]
    for child in children:  # Recursively visit children
        # print(f"{node} -> {child}")  # Print the current node (for illustration)
        # print(visited)
        if child not in visited:
            dfs_recursive(tree, child, visited)
            visited.pop()
    # print(f"{BLUE}{all_paths}{ENDCOLOR}")


def parse_input(codeInput: AOC):
    data_map = codeInput.read_lines()
    global max_y, max_x
    max_y, max_x = getMaxYMaxX(data_map)
    result = dict()
    for y, line in enumerate(data_map):
        for x, point in enumerate(line):
            if data_map[y][x] == ".":
                result[(y, x)] = {"val": -1, "neigh": list()}
            else:
                result[(y, x)] = {"val": int(point), "neigh": list()}

    for pos, values in result.items():
        if values["val"] == -1:
            continue
        for move in moves:
            poss_neighbor = addTuples(pos, move)
            if (
                insideGrid(poss_neighbor, (max_y, max_x))
                and result[poss_neighbor]["val"] == values["val"] + 1
            ):
                result[pos]["neigh"].append(poss_neighbor)

    return result


def part1(trail_map):
    # Find all starging locations
    trail_starts, trail_ends = list(), list()
    for y in range(0, max_y):
        for x in range(0, max_x):
            if trail_map[(y, x)]["val"] == 0:
                trail_starts.append((y, x))
            elif trail_map[(y, x)]["val"] == 9:
                trail_ends.append((y, x))

    for trail_start in trail_starts:
        dfs_recursive(trail_map, trail_start)
    unique_paths = list()
    for path in all_paths:
        start, end = path[0], path[-1]
        if (start, end) not in unique_paths:
            unique_paths.append((start, end))
    # for unique_path in unique_paths:
    #     print(f"{BLUE}{unique_path}{ENDCOLOR}")
    print(f"Unique Start/End: {len(unique_paths)}")


def part2(trail_map):
    # I am not sure why I am doubling up the all_paths list, so I just used the original list from part1 since it is still
    # valid. Somehing in Python that i don't understand

    # # Find all starging locations
    # trail_starts, trail_ends = list(), list()
    # for y in range(0, max_y):
    #     for x in range(0, max_x):
    #         if trail_map[(y, x)]["val"] == 0:
    #             trail_starts.append((y, x))
    #         elif trail_map[(y, x)]["val"] == 9:
    #             trail_ends.append((y, x))

    # for trail_start in trail_starts:
    #     dfs_recursive(trail_map, trail_start)
    # # unique_paths = list()
    # # for path in all_paths:
    # #     start, end = path[0], path[-1]
    # #     if (start, end) not in unique_paths:
    # #         unique_paths.append((start, end))
    # # for unique_path in unique_paths:
    # #     print(f"{BLUE}{unique_path}{ENDCOLOR}")

    print(f"Unique Paths: {len(all_paths)}")


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    dataInput = parse_input(codeInput)

    part1(dataInput)
    part2(dataInput)


if __name__ == "__main__":
    main()
