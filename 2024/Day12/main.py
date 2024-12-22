## NEED TO SOLVE PART 2 SITLL

from AOC import AOC, getDateYear, getMaxYMaxX, addTuples
from TerminalColors import *

testing = True
y_max = x_max = 0
part1_moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
part2_moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# Organize the corners
# True = Occupied by same plant
# False = Not occupied by same plant
# None = Doesn't matter for this corner

all_corners = {
    "OTL": [False, False, None, False, None, None, None, None],
    "OTR": [None, False, False, None, False, None, None, None],
    "OBL": [None, None, None, False, None, False, False, None],
    "OBR": [None, None, None, None, False, None, False, False],
    "IBR": [None, None, None, None, True, None, True, False],
    "IBL": [None, None, None, True, None, False, True, None],
    "ITR": [None, True, False, None, True, None, None, None],
    "ITL": [False, True, None, True, None, None, None, None],
}


def parse_input(codeInput: AOC):
    matrix = codeInput.read_lines()
    garden = dict()
    for y, line in enumerate(matrix):
        for x, plant in enumerate(line):
            garden[plant] = garden.get(plant, []) + [(y, x)]
    global y_max, x_max
    y_max, x_max = getMaxYMaxX(matrix)

    plant_plots = list()
    for plant, poses in garden.items():
        remaining_poses = dict()
        remaining_poses_list = poses.copy()
        for pos in poses:
            remaining_poses[pos] = get_neighbors_part1(pos, poses)
        while len(remaining_poses_list) != 0:
            check_pos = remaining_poses_list[0]
            plot = dfs_recursive(remaining_poses, check_pos)
            plant_plots.append({"plant": plant, "plot": plot})
            for loc in plot:
                remaining_poses_list.remove(loc)
                del remaining_poses[loc]

    return plant_plots


def dfs_recursive(graph, start, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, path, visited)

    return path


def get_neighbors_part1(pos, all_positions):
    all_neighbors = list()
    for move in part1_moves:
        poss_neigh = addTuples(pos, move)
        if poss_neigh in all_positions:
            all_neighbors.append(poss_neigh)
    return all_neighbors


def get_neighbors_part2(position, all_positions):
    all_neighbors = list()
    for move in part2_moves:
        poss_neigh = addTuples(position, move)
        if poss_neigh in all_positions:
            all_neighbors.append(move)
    return all_neighbors


def get_measurements_part1(plant):
    poses = plant["plot"]
    area = len(poses)
    perimeter = 0
    for pos in poses:
        perimeter += 4 - len(get_neighbors_part1(pos, poses))
    return area, perimeter


def get_measurements_part2(plant):

    # def check_for_corner(position, neighbors):
    #     corners_found = ""
    #     corner_count = 0
    #     for corner_name, corner_pattern in all_corners.items():
    #         valid_corner = True
    #         for check_corner, req_value in zip(part2_moves, corner_pattern):
    #             in_neighbors = check_corner in neighbors
    #             if req_value == None:
    #                 continue
    #             elif in_neighbors == req_value:
    #                 continue
    #             # elif req_value and in_neighbors:
    #             #     continue
    #             # elif not (req_value and in_neighbors):
    #             #     continue
    #             else:
    #                 valid_corner = False
    #                 break
    #         if valid_corner:
    #             corners_found += f"{corner_name},"
    #             corner_count += 1
    #     print(position, corners_found)
    #     return corner_count

    positions = sorted(plant["plot"])
    area = len(positions)
    perimeter = 0

    # for position in positions:
    #     all_neighbors = get_neighbors_part2(position, positions)
    #     corners = check_for_corner(position, all_neighbors)
    #     perimeter += corners

    for y in range(-1, y_max + 1):
        for x in range(-1, x_max + 1):
            if (y, x) in positions:
                continue
            else:
                corners = get_neighbors_part1((y, x), positions)
                perimeter += corners
    return area, perimeter


def part1(dataInput):
    garden = dataInput
    total_cost = 0
    for plot in garden:
        area, permiter = get_measurements_part1(plot)
        total_cost += area * permiter
    print(total_cost)


def part2(dataInput):
    garden = dataInput
    total_cost = 0
    for plot in garden:
        area, total_corners = get_measurements_part2(plot)
        plant_cost = area * total_corners
        total_cost += plant_cost
        print(plot["plant"], area, total_corners, plant_cost)
    print(total_cost)


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
