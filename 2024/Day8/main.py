from itertools import combinations
from AOC import (
    AOC,
    getDateYear,
    subtractTuples,
    multiplyTuple,
    addTuples,
    insideGrid,
    getMaxYMaxX,
)
from TerminalColors import *


testing = False
y_max = x_max = 0


def parse_input(codeInput: AOC):
    matrix = codeInput.read_lines()
    antennas = dict()
    global y_max, x_max
    y_max, x_max = getMaxYMaxX(matrix)
    # Create a hash list of the antenna positions
    # Dictionary:
    #   Key: Antenna Type
    #   Value: Antenna Position
    for y in range(y_max):
        for x in range(x_max):
            spot = matrix[y][x]
            if not spot == ".":
                if spot in antennas.keys():
                    antennas[spot].append((y, x))
                else:
                    antennas[spot] = [(y, x)]
    return antennas


def calc_new_posses(antenna_pairs_coords, poss_offsets_multipler):
    """Calclualte all the possible new positions for a list
        Antenna pairs

    Args:
        antenna_pairs_coords (list): list of pairs of Antenna coordinates
        poss_offsets_multiplier (list): list of offset mulitpliers. For Part 1 [-1,1]

    Returns:
        list: List of coordinates for all possible new Antenna positins. Uses
            set() to reduce the list and remove duplicates.
    """
    poss_positions = list()
    for pair in antenna_pairs_coords:
        test_offsets = list()
        offset = subtractTuples(pair[0], pair[1])
        for multi in poss_offsets_multipler:
            dist_offset = multiplyTuple(offset, multi)
            for pos in pair:
                new_poss = addTuples(pos, dist_offset)
                if new_poss not in pair and insideGrid(new_poss, max=(y_max, x_max)):
                    test_offsets.append(new_poss)
        poss_positions += test_offsets
    return list(set(poss_positions))


def part1(antenna_types):
    total_positions = list()
    antenna_pairs = dict()
    for antenna_type, antenna_locs in antenna_types.items():
        antenna_pairs[antenna_type] = combinations(antenna_locs, 2)
        poss_positions = calc_new_posses(antenna_pairs[antenna_type], [-1, 1])
        total_positions += poss_positions
    print(len(set(total_positions)))


def part2(antenna_types):
    total_positions = list()
    antenna_pairs = dict()
    poss_offsets = list(range(-x_max - 1, x_max))
    poss_offsets.remove(0)
    for antenna_type, antenna_locs in antenna_types.items():
        # Check if there is only one of Antenna type.
        # Not sure this comes in to play, but is called out in the problem statement
        if len(antenna_locs) == 1:
            break
        antenna_pairs[antenna_type] = combinations(antenna_locs, 2)
        poss_positions = calc_new_posses(antenna_pairs[antenna_type], poss_offsets)
        total_positions += poss_positions
        total_positions += antenna_locs

    print(len(set(total_positions)))


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
