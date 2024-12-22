import heapq
from AOC import AOC, getDateYear, getMaxYMaxX, moveOffets, addTuples
from TerminalColors import *

testing = True
max_y, max_x = 0, 0


def parse_input(codeInput: AOC):
    lines = codeInput.read_lines()
    walls = []
    open_spots = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                walls.append((y, x))
            elif char == ".":
                open_spots.append((y, x))
            elif char == "S":
                start = (y, x)
            elif char == "E":
                end = (y, x)
    global max_y, max_x
    max_y, max_x = getMaxYMaxX(codeInput.read_lines())
    return (open_spots, walls, start, end)


def print_grid(walls, open_spots, start, end):
    for y in range(max_y):
        for x in range(max_x):
            if (y, x) in walls:
                print("#", end="")
            elif (y, x) in open_spots:
                print(".", end="")
            elif (y, x) == start:
                print("S", end="")
            elif (y, x) == end:
                print("E", end="")
        print()


def get_neighbors(node, poss_neighbors):
    neighbors = []
    for move in moveOffets.values():
        neighbor = addTuples(node, move)
        if neighbor in poss_neighbors:
            neighbors.append(neighbor)
    return neighbors


def dijkstra(graph, start, goal):
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


def run_race(open_spots, start, end):
    graph = dict()
    for open_spot in open_spots:
        graph[open_spot] = dict()
        neighbors = get_neighbors(open_spot, open_spots)
        for neighbor in neighbors:
            graph[open_spot][neighbor] = 1

    path, cost = dijkstra(graph, start, end)
    if path is None:
        return None
    return cost


def part1(dataInput):
    open_spots, walls, start, end = dataInput
    open_spots += [start, end]
    speed_gt_hundred = 0
    # print_grid(walls, open_spots, start, end)
    base_speed = run_race(open_spots, start, end)

    poss_cheats = [(y, x) for y in range(1, max_y - 1) for x in range(1, max_x - 1)]
    poss_cheat_pairs = list()
    for poss_cheat in poss_cheats:
        cheat_neighors = get_neighbors(poss_cheat, poss_cheats + open_spots)
        for cheat_neighbor in cheat_neighors:
            if poss_cheat in open_spots and cheat_neighbor in open_spots:
                # If both postions are open spots, we don't need to cheat
                continue
            # Check to see if the reverse is already in the list of cheat, eliminating duplicates
            if (
                cheat_neighbor,
                poss_cheat,
            ) not in poss_cheat_pairs and cheat_neighbor in poss_cheats:
                poss_cheat_pairs.append((poss_cheat, cheat_neighbor))

    print(f"Total Poss Cheats: {len(poss_cheat_pairs)}")

    poss_cheat_pairs = [((7, 6), (7, 5))]

    cheat_savings = dict()
    for poss_cheat_pair in poss_cheat_pairs:
        check_open_spots = open_spots.copy()
        check_open_spots += poss_cheat_pair
        check_speed = run_race(check_open_spots, start, end)
        speed_savings = base_speed - check_speed
        if speed_savings > 0:
            print(f"Remvoing {poss_cheat_pair} Speed Savings: {speed_savings}")
            cheat_savings[speed_savings] = cheat_savings.get(speed_savings, 0) + 1
        if speed_savings >= 100:
            speed_gt_hundred += 1

    for key, value in cheat_savings.items():
        print(f"Speed Savings: {key} Count: {value}")
    print(f"Cheats that lower by 100 picoseconds: {speed_gt_hundred}")


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
