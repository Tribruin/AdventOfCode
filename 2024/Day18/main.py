from math import inf
import string
import heapq
from AOC import AOC, getDateYear, moveOffets, addTuples, insideGrid
from TerminalColors import *


# Combine digits and uppercase letters
characters = string.digits + string.ascii_uppercase


testing = False
if testing:
    max_x = max_y = 7
    init_cycles = 12
else:
    max_x = max_y = 71
    init_cycles = 1024


def print_grid(path: list, blocks: list):
    print(f"{CLEAR}")
    for y in range(max_y):
        for x in range(max_x):
            if (x, y) in blocks:
                print("X", end="")
            elif (x, y) in path:
                print(f"{BOLD}O{ENDCOLOR}", end="")
            else:
                print(".", end="")
        print()
    print()


def print_grid_inprocess(locs: dict, blocks: list):
    print(f"{CLEAR}")
    for y in range(max_y):
        for x in range(max_x):
            if (x, y) in blocks:
                print("X", end="")
            elif (x, y) in locs.keys() and locs[(x, y)] < inf:
                char_to_print = characters[locs[(x, y)]]
                print(f"{BOLD}{char_to_print}{ENDCOLOR}", end="")
            else:
                print(".", end="")
        print()
    print()


def dijkstra(graph, start, goal, corr_mem):
    """
    Perform Dijkstra's algorithm to find the shortest path from start to goal.

    :param graph: A dictionary where keys are nodes and values are dictionaries
                    of neighbors with edge costs.
    :param start: The starting node.
    :param goal: The goal node.
    :return: A tuple (path, cost) where path is a list of nodes from start to goal,
                    and cost is the total cost.
    """
    # Priority queue to store (cost, node)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    # Distances from start to each node
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    # To reconstruct the shortest path
    came_from = {}

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)
        # print_grid_inprocess(distances, corr_mem)

        # Stop if we reached the goal
        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            return path, current_cost

        for neighbor, weight in graph[current_node].items():
            new_cost = current_cost + weight
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                came_from[neighbor] = current_node
                heapq.heappush(priority_queue, (new_cost, neighbor))

    # If no path is found
    return None, float("inf")


def parse_input(codeInput: AOC):
    lines = codeInput.find_all_ints_in_lines()
    result = [(x, y) for x, y in lines]
    return result


def part1(dataInput):
    corr_mem = dataInput[:init_cycles]
    open_spaces = {
        (x, y): dict()
        for x in range(max_x)
        for y in range(max_y)
        if (x, y) not in corr_mem
    }

    # Get the neighbors
    for open_space in open_spaces.keys():
        for move in moveOffets.values():
            pos_neigh = addTuples(open_space, move)
            if pos_neigh not in corr_mem and insideGrid(pos_neigh, (max_x, max_y)):
                open_spaces[open_space][pos_neigh] = 1
            else:
                pass
                # open_spaces[open_space][pos_neigh] = 1

    path, cost = dijkstra(open_spaces, (0, 0), (max_x - 1, max_y - 1), corr_mem)
    print(cost)
    return path


def part2(dataInput, path):

    for cycles in range(init_cycles + 1, len(dataInput)):
        print(f"Checking Cycle: {cycles}")

        # Check to see if the newest corruption is in the existing path. If not, skip the calculation
        # if dataInput[cycles] not in path:
        #     continue
        corr_mem = dataInput[:cycles]
        open_spaces = {
            (x, y): dict()
            for x in range(max_x)
            for y in range(max_y)
            if (x, y) not in corr_mem
        }

        # Get the neighbors
        for open_space in open_spaces.keys():
            for move in moveOffets.values():
                pos_neigh = addTuples(open_space, move)
                if pos_neigh not in corr_mem and insideGrid(pos_neigh, (max_x, max_y)):
                    open_spaces[open_space][pos_neigh] = 1
                else:
                    pass
                    # open_spaces[open_space][pos_neigh] = 1

        path, cost = dijkstra(open_spaces, (0, 0), (max_x - 1, max_y - 1), corr_mem)
        if cost == inf:
            print(f"Found Cycle: {cycles} - {corr_mem[-1]}")
            break


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    dataInput = parse_input(codeInput)

    path = part1(dataInput)
    part2(dataInput, path)


if __name__ == "__main__":
    main()
