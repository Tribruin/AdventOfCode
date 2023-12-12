#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC
from functools import reduce
from math import sqrt

testing = False


def factors(n):

    # Generate the factors of the number n
    step = 2 if n % 2 else 1
    return set(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0),
        )
    )


def part1(input):
    i = 0
    presents = 0
    largest_presents = 0
    while presents < input:
        i += 1
        presents = sum(factors(i)) * 10
        # if presents > largest_presents:
        #     largest_presents = presents
    print(f"House: {i} - Presents: {presents}")


def part2(input):
    i = 1
    presents = 0
    largest_presents = 0
    elves = dict()
    while presents < input:
        all_factors = factors(i)
        for factor in all_factors:
            if factor in elves.keys():
                elves[factor] += 1
            else:
                elves[factor] = 1
        elves_delivering = [x for x in all_factors if elves[x] <= 50]
        elves_delivering.sort()
        presents = sum(elves_delivering) * 11

        if presents > largest_presents:
            largest_presents = presents
            print(f"House: {i} - Presents: {presents}")
        i += 1


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=testing)
    input = data.read_int()[0]

    part1(input)
    part2(input)


if __name__ == "__main__":
    main()
