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

    for step in range(steps):
        k = len(template)
        new_template = template[0]
        for i in range(k - 1):
            a, b = template[i], template[i+1]
            x = a+b
            new_template += rules[x] + b
        # new_template += template[k-1]
        print(step)
        template = new_template

    chars = string.ascii_uppercase
    count_dict = dict()
    for char in chars:
        count_dict[char] = template.count(char)

    values = [x for x in count_dict.values() if x != 0]
    print(max(values) - min(values))


def part2(template, rules):
    steps = 40

    for step in range(steps):
        k = len(template)
        new_template = template[0]
        for i in range(k - 1):
            a, b = template[i], template[i+1]
            x = a+b
            new_template += rules[x] + b
        # new_template += template[k-1]
        print(step)
        template = new_template

    chars = string.ascii_uppercase
    count_dict = dict()
    for char in chars:
        count_dict[char] = template.count(char)

    values = [x for x in count_dict.values() if x != 0]
    print(max(values) - min(values))


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
    # part2(template, rules)


if __name__ == "__main__":
    main()
