#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC

testing = True


def parse_input(data_input: list):
    result = dict()
    caves = [x.split("-") for x in data_input]
    for cave in caves:
        if not cave[1] == 'start':
            if cave[0] in result.keys():
                result[cave[0]].append(cave[1])
            else:
                result[cave[0]] = [cave[1]]

    for cave in caves:
        if not cave[0] == 'start':
            if cave[1] in result.keys():
                result[cave[1]].append(cave[0])
            else:
                result[cave[1]] = [cave[0]]

    result['end'] = list()
    return result


def find_paths(caves, start_cave, last_cave) -> list:
    sub_paths = list()
    for path in caves[start_cave]:
        current_path = start_cave
        if path == last_cave and last_cave.islower():
            pass
        elif path == "end":
            sub_paths.append("end")
            return sub_paths
        else:
            current_path += find_paths(caves, caves[path], path)
            sub_paths.append(current_path)
    return sub_paths


def part1(caves):
    all_paths = find_paths(caves, "start", last_cave="")
    print(all_paths)


def part2(data_input):
    pass


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    # global data
    code_data = AOC(codeDate, codeYear, test=testing)
    data_input = code_data.read_lines()
    data_input = parse_input(data_input)

    part1(data_input)
    part2(data_input)


if __name__ == "__main__":
    main()
