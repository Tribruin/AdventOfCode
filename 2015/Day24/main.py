#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC
from itertools import combinations, permutations

testing = False


# def part1(input):
#     bag1_count = 2

#     count_found = False
#     while not count_found:
#         check_perms = [
#             x for x in perms if sum(x[:bag1_count]) * 2 == sum(x[bag1_count:])
#         ]
#         found_bag1s = list()
#         print(f"Checking for bag 1 has {bag1_count} bags")

#         for perm in check_perms:
#             bag1 = perm[:bag1_count]
#             print(f"Checking Bag1 {bag1}")
#             bag1_lbs = sum(bag1)
#             bag2bag3 = perm[bag1_count:]
#             for i in range(2, len(bag2bag3) - 1):
#                 bag2_lbs = sum(bag2bag3[:i])
#                 bag3_lbs = sum(bag2bag3[i:])
#                 if bag1_lbs == bag2_lbs == bag3_lbs:
#                     bag1_total_size = bag1_count
#                     found_bag1s.append(bag1)
#                     count_found = True
#         bag1_count += 1
#     print(found_bag1s)


def part1(input):

    # Find all combinations of bags with the bag1_count1 of presents
    # Then find all combinations where bag2 + bag3 weight is twice
    # bag1 weight or bag1 weight is 1/3 of total weight of packages

    bag1_count = 3
    count_found = True
    found_bag1s = list()
    bag1_weight = sum(input) // 3
    # while not len(found_bag1s) != 0:
    while len(found_bag1s) == 0:                                #
        check_perms = list(combinations(input, bag1_count))
        print(f"Checking for bag 1 has {bag1_count} presents")

        for bag1 in check_perms:
            # print(f"Check bag1 presents {bag1}")
            bag1_lbs = sum(bag1)
            bag2_bag3 = input.copy()
            for i in bag1:
                bag2_bag3.remove(i)
            if bag1_lbs == bag1_weight:
                found_bag1s.append(bag1)
        print(f"Found {len(found_bag1s)} combinations that balance.")
        bag1_count += 1

    min_qe = 999999999999
    max_bag1 = list()
    for bag in found_bag1s:
        qe = 1
        for value in bag:
            qe *= value
        if qe < min_qe:
            min_qe = qe
            max_bag1 = bag
    print(max_bag1, min_qe)


def part2(input):
    # Find all combinations of bags with the bag1_count1 of presents
    # Then find all combinations where bag2 + bag3 weight is twice
    # bag1 weight

    bag1_count = 3
    count_found = True
    found_bag1s = list()
    bag1_weight = sum(input) // 4
    while not len(found_bag1s) != 0:
        check_perms = list(combinations(input, bag1_count))
        print(f"Checking for bag 1 has {bag1_count} presents")

        for bag1 in check_perms:
            # print(f"Check bag1 presents {bag1}")
            bag1_lbs = sum(bag1)
            bag2_bag3 = input.copy()
            for i in bag1:
                bag2_bag3.remove(i)
            if bag1_lbs == bag1_weight:
                found_bag1s.append(bag1)
        print(f"Found {len(found_bag1s)} combinations that balance.")
        bag1_count += 1

    min_qe = 999999999999
    max_bag1 = list()
    for bag in found_bag1s:
        qe = 1
        for value in bag:
            qe *= value
        if qe < min_qe:
            min_qe = qe
            max_bag1 = bag
    print(max_bag1, min_qe)


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=testing)
    input = data.read_int()

    part1(input)
    part2(input)


if __name__ == "__main__":
    main()
