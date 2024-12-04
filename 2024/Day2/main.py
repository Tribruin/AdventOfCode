from AOC import AOC, getDateYear
from TerminalColors import *

testing = False


def parse_input(code_input: AOC):
    result = code_input.find_all_ints_in_lines()
    return result


def check_report(report: list):
    if report[0] < report[1]:
        # numbers are increasing so check for increases
        for i, j in zip(report[:-1], report[1:]):
            if -4 < i - j < 0:
                pass
            else:
                # Numbers are not increaseing, so bad report
                return False
    else:
        # numbers are decreasing, so check for decreases
        for i, j in zip(report[:-1], report[1:]):
            if 0 < i - j < 4:
                pass
            else:
                # Numbers are not decreasing, so bad report
                return False
    return True


def part1(data_input):

    valid_reports = 0
    for report in data_input:
        if check_report(report):
            valid_reports += 1
    print(valid_reports)


def part2(data_input):

    valid_reports = 0
    for report in data_input:
        if check_report(report):
            valid_reports += 1
        else:
            # Let's check for reports that can drop on input and still be valid
            for i in range(len(report)):
                test_report = report[:i] + report[i + 1 :]
                if check_report(test_report):
                    valid_reports += 1
                    break

    print(valid_reports)


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
