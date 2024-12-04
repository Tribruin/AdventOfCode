import re
from AOC import AOC, getDateYear
from TerminalColors import *

testing = False


def parse_input(codeInput: AOC):
    result = codeInput.file
    return result


def compute_result(dataInput: str):
    # This regex pattern returns a list of digit pairs where
    # the pattern matches mul(num, num) where num is a 1-3 digit number
    reg_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    result = re.findall(reg_pattern, dataInput)

    # Interate through pairs and computer sum of product of each pair
    total = 0
    for pair in result:
        total += int(pair[0]) * int(pair[1])
    return total


def part1(dataInput):
    # This regex pattern returns a list of digit pairs where
    # the pattern matches mul(num, num) where num is a 1-3 digit number
    print(compute_result(dataInput))


def part2(dataInput):
    current_string = dataInput
    new_string = ""
    pattern_do = "do()"
    pattern_dont = "don't()"
    while current_string != "":
        # Find the next don't()
        dont_pos = current_string.find(pattern_dont)
        if dont_pos != -1:
            new_string += current_string[:dont_pos]
            current_string = current_string[dont_pos + 7 :]
        else:
            new_string += current_string
            break

        # Now find the next do()
        do_pos = current_string.find(pattern_do)
        current_string = current_string[do_pos + 4 :]
        if do_pos == -1:
            break

    print(compute_result(new_string))


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
