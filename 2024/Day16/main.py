import heapq
from AOC import AOC, getDateYear, moveOffets, addTuples, subtractTuples
from TerminalColors import *
from math import inf

testing = True
direction_costs = {
    ">": {">": 1, "^": 1001, "v": 1001, "<": 1},
    "^": {">": 1001, "^": 1, "v": 1, "<": 1001},
    "<": {">": 1, "^": 1001, "v": 1001, "<": 1},
    "v": {">": 1001, "^": 1, "v": 1, "<": 1001},
}


def parse_input(codeInput: AOC):
    lines = codeInput.read_lines()
    walls = list()
    paths = list()
    for y, line in enumerate(lines):
        for x, pos in enumerate(line):
            match pos:
                case "S":
                    start_pos = ((y, x), "<")
                    paths.append((y, x))
                case "E":
                    end_pos_loc = (y, x)
                    paths.append((y, x))
                case "#":
                    walls.append((y, x))
                case _:
                    paths.append((y, x))

    end_pos = list()
    for dir, val in moveOffets.items():
        neigh = subtractTuples(end_pos_loc, val)
        if neigh not in walls:
            end_pos.append((end_pos_loc, dir))

    directions = moveOffets.keys()

    graph = dict()
    for path in paths:
        for direction in directions:

            path_neighbors = dict()
            for move_dir, move_val in moveOffets.items():
                neighbor = addTuples(path, move_val)
                if neighbor not in walls:
                    path_neighbors[(neighbor, move_dir)] = direction_costs[direction][
                        move_dir
                    ]
            graph[(path, direction)] = path_neighbors

    return (start_pos, end_pos, graph)


def dijkstra(graph, start, goal):
    """
    Perform Dijkstra's algorithm to find the shortest path from start to goal.

    :param graph: A dictionary where keys are nodes and values are dictionaries of neighbors with edge costs.
    :param start: The starting node.
    :param goal: The goal node.
    :return: A tuple (path, cost) where path is a list of nodes from start to goal, and cost is the total cost.
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


def part1(dataInput):
    start_pos, end_poses, graph = dataInput
    best_route_cost = inf
    for end_pos in end_poses:
        print(start_pos, end_pos)
        route, cost = dijkstra(graph, start_pos, end_pos)
        print(len(route), cost)
        if cost < best_route_cost:
            best_route_cost = cost
            best_route = route
    print(best_route_cost)


def part2(dataInput):
    pass


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
