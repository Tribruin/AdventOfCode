#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC

testing = False


def parse_input(input_data: AOC):

    lines = input_data.read_lines()
    sig_patterns = [x.split("|") for x in lines]
    return sig_patterns


def sorted_string(string: str) -> str:
    return "".join(sorted(string))


def part1(sig_patterns):
    unique_counts = [2, 4, 3, 7]
    output_vals = [x[1].split() for x in sig_patterns]
    count = 0
    for line in output_vals:
        count += len([x for x in line if len(x) in unique_counts])
    print(count)


def part2(sig_patterns):
    unique_counts = {2: 1, 4: 4, 3: 7, 7: 8}
    total_result = 0
    for line in sig_patterns:

        split_line = [sorted_string(x) for x in line[0].strip().split(" ")]
        subs = {x: "" for x in range(10)}
        reversed_line = split_line[::-1]
        length = len(split_line)

        # First let's find the 1, 4, 7, 8
        for x, digit in enumerate(reversed_line):
            if len(digit) in unique_counts.keys():
                subs[unique_counts[len(digit)]] = sorted_string(digit)
                split_line.pop(length - x - 1)

        # Next let's find the 0
        a = sorted_string(set(subs[7]).difference(set(subs[1])))
        cf = subs[1]
        eg = sorted_string(set(subs[8]).difference(set(subs[7]).union(subs[4])))
        cefg = sorted_string(cf + eg)

        for val in split_line:
            if set(cefg).issubset(val):
                subs[0] = val
                break
        split_line.pop(split_line.index(subs[0]))

        # Now let's find the 2, 3
        b = "".join(set(subs[0]).difference(set(cefg + a)))
        f23 = [x for x in split_line if b not in x]
        if set(cf).issubset(set(f23[0])):
            subs[3] = sorted_string(f23[0])
            subs[2] = sorted_string(f23[1])
        else:
            subs[3] = sorted_string(f23[1])
            subs[2] = sorted_string(f23[0])
        split_line.pop(split_line.index(subs[3]))
        split_line.pop(split_line.index(subs[2]))

        # Now find the 9
        for digit in split_line:
            if set(cf).issubset(set(digit)):
                subs[9] = digit
                break
        split_line.pop(split_line.index(subs[9]))

        # Finally we find the 6, 5
        if len(split_line[0]) == 6:
            subs[6] = split_line[0]
            subs[5] = split_line[1]
        else:
            subs[6] = split_line[1]
            subs[5] = split_line[0]

        # Did we get everything? Yes, let's resort the dict
        found_subs = {y: x for x, y in subs.items()}

        # Now lets compute the output:
        result = ""
        for digit in line[1].strip().split(" "):
            result += str(found_subs[sorted_string(digit)])
        # print(result)
        total_result += int(result)
    print(total_result)


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    data = AOC(codeDate, codeYear, test=testing)
    sig_patterns = parse_input(data)

    part1(sig_patterns)
    part2(sig_patterns)


if __name__ == "__main__":
    main()
