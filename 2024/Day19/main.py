from AOC import AOC, getDateYear
from TerminalColors import *

testing = False
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
        new_pattern = pattern.replace(towel, "", 1)
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
    cache[pattern] = False
    return False


def part1(dataInput):
    towels, patterns = dataInput

    valid_patterns = []
    for idx, pattern in enumerate(patterns):
        # print(f"{idx}/{pattern}", end="")
        if find_if_valid_pattern(towels, pattern):
            valid_patterns.append(pattern)
            # print(" - Valid")
        else:
            pass
            # print(" - Invalid")
    print(len(valid_patterns))


def find_combinations_with_cache(base_blocks, target_line, depth=0):
    # Cache to store results for each remaining string
    cache = {}

    # @cache
    def backtrack(remaining, depth):
        print(f"Depth: {depth}")
        # If the result for this state is cached, return it
        if remaining in cache:
            return cache[remaining]

        # Base case: If the target string is fully matched, return one empty combination
        if not remaining:
            return [[]]

        # Store combinations for this state
        combinations = []

        for block in base_blocks:
            if remaining.startswith(
                block
            ):  # Check if block matches the start of the remaining string
                # Recurse with the remaining string after removing the current block
                for sub_combination in backtrack(remaining[len(block) :], depth + 1):
                    combinations.append([block] + sub_combination)

        # Store result in cache before returning
        cache[remaining] = combinations
        return combinations

    # Start backtracking and return results
    return backtrack(target_line, depth)


def part2(dataInput):

    # I HAVE NO IDEA HOW TO DO THIS
    # See test.py for the solution

    towels, patterns = dataInput
    valid_patterns = [x for x in patterns if cache[x] == True]

    total_combos = 0
    for pattern in valid_patterns:
        print(f"Pattern: {pattern}")
        combos = find_combinations_with_cache(towels, pattern, depth=0)
        total_combos += len(combos)
        print(f"{len(combos)} - {total_combos}")
    print(total_combos)


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
