from AOC import AOC, getDateYear
from TerminalColors import *

testing = True
cache = {}
towel_combos = {}


def parse_input(codeInput: AOC):
    lines = codeInput.read_lines()
    towels = lines[0].split(", ")
    patterns = lines[2:]
    return (towels, patterns)


def find_if_valid_pattern(towels, pattern, depth=0):
    """This application uses a caching mechanism to store the
    results of the patterns that have been checked.
    If we have see the pattern before, we can return the result as it won't change"""
    if pattern in cache:
        return cache[pattern]
    valid_pattern = False
    check_towels = [x for x in towels if pattern.startswith(x)]
    available_towels = towels.copy()
    for towel in check_towels:
        # print(f"Checking {towel} in {pattern} - {depth}")
        # if pattern.startswith(towel):
        new_pattern = pattern.replace(towel, "", 1)
        # available_towels.remove(towel)
        if len(new_pattern) == 0:
            cache[pattern] = True
            return True
        else:
            valid_pattern = find_if_valid_pattern(
                available_towels, new_pattern, depth + 1
            )
            if valid_pattern:
                cache[pattern] = True
                return True
    # else:
    #         continue
    cache[pattern] = False
    return False


def part1(dataInput):
    towels, patterns = dataInput

    valid_patterns = []
    for idx, pattern in enumerate(patterns):
        # print(f"{idx}/{pattern}")
        print(f"{idx}/{pattern}", end="")
        if find_if_valid_pattern(towels, pattern):
            valid_patterns.append(pattern)
            print(" - Valid")
        else:
            print(" - Invalid")
    print(len(valid_patterns), len(cache))


def part2(dataInput):
    towels, patterns = dataInput
    for towel in towels:
        towel_combos[towel] = list()
        for other_towel in towels:
            if other_towel.startswith(towel):
                towel_combos[towel].append(other_towel)
    pass


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    dataInput = parse_input(codeInput)

    # part1(dataInput)
    part2(dataInput)


if __name__ == "__main__":
    main()
