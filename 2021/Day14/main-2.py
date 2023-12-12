#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC
import string

testing = False


def parse_input(data_input):

    template = data_input[0]
    rules = dict()
    for rule in data_input[2:]:
        x, y = rule.split(" -> ")
        rules[x] = y
    return template, rules


def part1(template, rules):
    steps = 10

    polymer = dict()
    for i in range(len(template) - 1):
        sub = template[i:i+2]
        polymer[sub] = polymer.get(sub, 0) + 1

    for i in range(steps):
        new_polymer = dict()
        for pair, count in polymer.items():
            z = rules[pair]
            xz = pair[0]+z
            zy = z+pair[1]
            new_polymer[xz] = new_polymer.get(xz, 0) + count
            new_polymer[zy] = new_polymer.get(zy, 0) + count
        polymer = new_polymer

    elements = {template[0]: 1}
    for pair, val in polymer.items():
        char = pair[1]
        elements[char] = elements.get(char, 0) + val
    print(max(elements.values()) - min(elements.values()))


def part2(template, rules):
    steps = 40

    polymer = dict()
    for i in range(len(template) - 1):
        sub = template[i:i+2]
        polymer[sub] = polymer.get(sub, 0) + 1

    for i in range(steps):
        new_polymer = dict()
        for pair, count in polymer.items():
            z = rules[pair]
            xz = pair[0]+z
            zy = z+pair[1]
            new_polymer[xz] = new_polymer.get(xz, 0) + count
            new_polymer[zy] = new_polymer.get(zy, 0) + count
        polymer = new_polymer

    elements = {template[0]: 1}
    for pair, val in polymer.items():
        char = pair[1]
        elements[char] = elements.get(char, 0) + val
    print(max(elements.values()) - min(elements.values()))


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    # global data
    code_data = AOC(codeDate, codeYear, test=testing)
    data_input = code_data.read_lines()
    template, rules = parse_input(data_input)

    part1(template, rules)
    part2(template, rules)


if __name__ == "__main__":
    main()
