from timeit import timeit

# INPUT_FILE = "Day6-Input-Test.txt"
INPUT_FILE = "Day6-Input.txt"


def read_file():
    with open(INPUT_FILE) as f:
        return [i.split() for i in f.read().split("\n\n")]


def part1():
    print(sum([len(set("".join(i))) for i in dec_forms]))


def part2():
    print(sum([len(list(set.intersection(*map(set, i)))) for i in dec_forms]))


dec_forms = read_file()
print(timeit(part1, number=1) * 1000)
print(timeit(part2, number=1) * 1000)