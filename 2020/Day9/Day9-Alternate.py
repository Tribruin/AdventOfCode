from itertools import permutations, combinations


INPUT_FILE = "Day9-Input.txt"
PREAMBLE_LEN = 25


def read_file():
    with open(INPUT_FILE, "r") as f:
        data = [int(i) for i in f.read().splitlines()]
        return data


def Part1():
    def check_for_valid(value, preamble):
        # Returns True if value is in list of sums of all 2 item combinations of preamble
        return value in [sum(i) for i in combinations(preamble, 2)]

    for y in range(PREAMBLE_LEN, len(data) - 1):
        if not check_for_valid(data[y], data[y - PREAMBLE_LEN : y]):
            print(f"Bad Number: {data[y]}")
            return data[y]


def Part2(num_to_find):
    def check_for_valid(value, preamble):
        for combos in range(2, len(preamble)):
            ranges = [
                preamble[i : i + combos] for i in range(len(preamble) - combos + 1)
            ]
            for pair in ranges:
                if sum(pair) == value:
                    return pair
        return False

    data_to_check = data[0 : data.index(num_to_find)]
    pair = check_for_valid(num_to_find, data_to_check)
    print(pair, min(pair) + max(pair))


data = read_file()
bad_number = Part1()
Part2(bad_number)