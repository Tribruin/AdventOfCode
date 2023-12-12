from itertools import permutations, combinations


INPUT_FILE = "Day9-Input.txt"
PREAMBLE_LEN = 25


def read_file():
    with open(INPUT_FILE, "r") as f:
        data = [int(i) for i in f.read().splitlines()]
        return data


def Part1():
    def check_for_valid(value, preamble):
        pairs = combinations(preamble, 2)
        for pair in pairs:
            if sum(pair) == value:
                return True
        return False

    x = PREAMBLE_LEN
    for num_to_check in range(x, len(data) - 1):
        if check_for_valid(
            data[num_to_check], data[num_to_check - PREAMBLE_LEN : num_to_check]
        ):
            pass
        else:
            print(f"Bad Number: {data[num_to_check]}")
            return data[num_to_check]


def Part2(num_to_find):
    def check_for_valid(value, preamble):
        for combos in range(2, len(preamble)):
            pairs = [
                preamble[i : i + combos] for i in range(len(preamble) - combos + 1)
            ]
            # print(pairs)
            for pair in pairs:
                # print(pair, sum(pair))
                if sum(pair) == value:
                    return pair
        return False

    data_to_check = data[0 : data.index(num_to_find)]
    pair = check_for_valid(num_to_find, data_to_check)
    print(pair, min(pair) + max(pair))


data = read_file()
bad_number = Part1()
Part2(bad_number)