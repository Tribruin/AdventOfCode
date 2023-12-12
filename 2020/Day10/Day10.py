# INPUT_FILE = "day10-Input-Test.txt"
INPUT_FILE = "day10-Input.txt"


def read_file():
    with open(INPUT_FILE, "r") as f:
        adaptors = [0] + [int(i) for i in f.read().splitlines()]
        adaptors.sort()
        adaptors.append(adaptors[-1] + 3)
    return adaptors


def part1():
    # Loop through chargers in accending order and count the differences
    chargers = {1: 0, 2: 0, 3: 0}
    for i in range(1, len(adaptors)):
        jolt_diff = adaptors[i] - adaptors[i - 1]
        chargers[jolt_diff] += 1
    print(chargers[1] * chargers[3])


def part2():
    counts = dict()
    for value in adaptors:
        counts[value] = 0
    counts[0] = 1

    for inc, value in enumerate(adaptors):

        for x in range(1, 4):
            if abs(adaptors[inc] - adaptors[inc - x]) <= 3:
                counts[adaptors[inc]] += counts[adaptors[inc - x]]
    # print(counts)
    print(counts[adaptors[-1]])


adaptors = read_file()
part1()
part2()