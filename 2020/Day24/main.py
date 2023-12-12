import sys
from timeit import timeit

sys.path.append("/Users/rblount/Scripts/AdventOfCode/2020/tools")

from AOC import AOC

BLACK = False
WHITE = True
COLORS = {False: "Black", True: "White"}

directions = {
    "ne": (1, 1),
    "e": (2, 0),
    "se": (1, -1),
    "sw": (-1, -1),
    "w": (-2, 0),
    "nw": (-1, 1),
}
tiles = dict()


class Hex_Tile:
    def __init__(self, coords):
        """Initiate a Hex Tile

        Args:
            coords (int,int): x, y coordinate of tile ( x + y  must be even)
        """

        self.x, self.y = coords
        self.coords = (self.x, self.y)
        if (self.x + self.y) % 2 != 0:
            raise TypeError("Invalid Coordinates")
        self.color = WHITE
        self.new_color = self.color

    def get_neighbor(self, direction):

        move = directions[direction]
        new_tile = add_tuples(self.coords, move)
        if new_tile not in tiles.keys():
            tiles[new_tile] = Hex_Tile(new_tile)
        return new_tile

    def get_all_neighbors(self):
        neigbors = []
        for tile in directions.keys():
            neigbors.append(self.get_neighbor(tile))
        return neigbors

    def change_color(self):
        self.color = not self.color

    def change_color_next_day(self):
        neighbors = self.get_all_neighbors()
        black_tiles = 0
        for neighbor in neighbors:
            current_color = tiles[neighbor].color
            if current_color == BLACK:
                black_tiles += 1
        if self.color == BLACK and (black_tiles == 0 or black_tiles > 2):
            self.new_color = WHITE
        elif self.color == WHITE and black_tiles == 2:
            self.new_color = BLACK
        else:
            self.new_color = self.color

    def __str__(self) -> str:
        return f"({self.x}, {self.y}) Color: {self.color}"


def next_day():
    for key, tile in tiles.items():
        # if tile.color != tile.new_color:
        #     print(f"Changing: {key} to {COLORS[tile.new_color]}")
        tile.color = tile.new_color


def process_input(data):
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


def add_tuples(tuple1, tuple2):
    x1, y1 = tuple1
    x2, y2 = tuple2
    return (x1 + x2, y1 + y2)


def black_tiles():
    black_tiles = 0
    for tile in tiles.keys():
        if tiles[tile].color == BLACK:
            black_tiles += 1
    return black_tiles


def print_tiles():
    x_values = set([x for x, y in tiles.keys()])
    y_values = set([y for x, y in tiles.keys()])
    x_min, x_max = min(x_values), max(x_values)
    y_min, y_max = min(y_values), max(y_values)
    # print((x_min, x_max), (y_max, y_min))
    for y in range(y_max, y_min - 1, -1):
        print(f"{y:3}: ", end="")
        for x in range(x_min, x_max + 1):
            if (x + y) % 2 != 0:
                print("  ", end="")
            else:
                if (x, y) in tiles.keys():
                    if tiles[(x, y)].color == BLACK:
                        print("◻ ", end="")
                    else:
                        print("◼︎ ", end="")
                else:
                    print("◼︎ ", end="")
        print("")
    print("     ", end="")
    for x in range(x_min, x_max + 1):
        print(f"{abs(x)} ", end="")
    print()
    # for key, tile in tiles.items():
    #     if tile.color == BLACK:
    #         print(key)


def fill_in_map():
    x_values = set([x for x, y in tiles.keys()])
    y_values = set([y for x, y in tiles.keys()])
    x_min, x_max = min(x_values), max(x_values)
    y_min, y_max = min(y_values), max(y_values)
    for y in range(y_max, y_min - 1, -1):
        for x in range(x_min, x_max + 1):
            if (x, y) not in tiles.keys() and (x + y) % 2 == 0:
                tiles[(x, y)] = Hex_Tile((x, y))


def part1():
    for line in all_moves:
        coords = (0, 0)
        for move in line:
            coords = tiles[coords].get_neighbor(move)
        tiles[coords].change_color()
    print(f"Day 0: {black_tiles()}")
    # print_tiles()


def part2():

    for day in range(1, 101):
        fill_in_map()
        current_keys = [x for x in tiles.keys()]
        for tile in current_keys:
            tiles[tile].change_color_next_day()
        next_day()
    print(f"Day {day:3}: {black_tiles():4} - Total Tiles: {len(tiles):6}")
    # print_tiles()


a = AOC(24, 2020, test=False)
input_data = a.read_lines()
all_moves = process_input(input_data)
tiles[(0, 0)] = Hex_Tile((0, 0))
print(timeit(part1, number=1))
print(timeit(part2, number=1))
