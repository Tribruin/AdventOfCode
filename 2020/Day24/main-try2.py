import sys
from timeit import timeit

sys.path.append("/Users/rblount/Scripts/AdventOfCode/2020/tools")

from AOC import AOC

directions = {
    "ne": (1, 1),
    "e": (2, 0),
    "se": (1, -1),
    "sw": (-1, -1),
    "w": (-2, 0),
    "nw": (-1, 1),
}

black_tiles = list()


def add_tuples(tuple1, tuple2):
    x1, y1 = tuple1
    x2, y2 = tuple2
    return (x1 + x2, y1 + y2)


def process_input(data) -> list:
    move_data = list()
    for line in data:
        line_data = list()
        i = 0
        while i < len(line):
            if line[i] in ["e", "w"]:
                line_data.append(line[i])
                i += 1
            else:
                line_data.append(line[i : i + 2])
                i += 2
        move_data.append(line_data)
    return move_data


def transverse_moves(moves) -> tuple:
    current_point = (0, 0)
    for move in moves:
        current_point = add_tuples(current_point, directions[move])
    return current_point


def get_all_neighbors(tile) -> list:
    neigbors = []
    for direction in directions.keys():
        neigbors.append(add_tuples(tile, directions[direction]))
    return neigbors


def part1():
    for moves in all_moves:
        final_tile = transverse_moves(moves)
        if final_tile in black_tiles:
            black_tiles.remove(final_tile)
        else:
            black_tiles.append(final_tile)
    print(f"Day   0 - {len(black_tiles)}")


def part2():
    check_black_tiles = black_tiles
    for day in range(1, 101):
        new_black_tiles = list()
        check_white_tiles = list()
        for tile in check_black_tiles:
            all_neighbors = get_all_neighbors(tile)
            black_neighbors = 0
            # Check the neighbors and find the black and white neighbors
            for neighbor in all_neighbors:
                if neighbor in check_black_tiles:
                    black_neighbors += 1
                else:
                    if neighbor not in check_white_tiles:
                        check_white_tiles.append(neighbor)
            if black_neighbors in [1, 2]:
                new_black_tiles.append(tile)
        for tile in check_white_tiles:
            all_neighbors = get_all_neighbors(tile)
            black_neighbors = 0
            for neighbor in all_neighbors:
                if neighbor in check_black_tiles:
                    black_neighbors += 1
            if black_neighbors == 2:
                new_black_tiles.append(tile)

        print(f"Day {day:3} - {len(new_black_tiles)}")
        # print(f"Original Black Tiles: {check_black_tiles}")
        # print(f"New Black Tiles: {list(set(new_black_tiles))}")
        check_black_tiles = list(set(new_black_tiles))


a = AOC(24, 2020, test=False)
input_data = a.read_lines()
all_moves = process_input(input_data)
print(timeit(part1, number=1))
print(timeit(part2, number=1))