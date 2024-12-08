from itertools import permutations, combinations, product
from time import sleep
from AOC import AOC, getDateYear
from TerminalColors import *

testing = False
operators = "*+"
operators_list = ["*", "+"]
operators_list_2 = ["%", "*", "+"]
# Using % for || so is sorts before the * and +


def parse_input(codeInput: AOC):
    lines = codeInput.read_lines()
    result = []
    for line in lines:
        tmp = line.split(":")
        tmp2 = list(map(int, tmp[1].split()))
        result.append((int(tmp[0]), tmp2))
    return result


def test_calcs(total: int, numbers: list, all_operations):
    valid = False
    for operations in all_operations:
        print(f"{BBLUE}{total} ≃ ", end="")
        for idx, number in enumerate(numbers[:-1]):
            print(f"{BBLUE}{number} ", end="")
            if operations[idx] == "%":
                print(f"{BYELLOW}‖ ", end="")
            else:
                print(f"{BYELLOW}{operations[idx]} ", end="")
        print(f"{BBLUE}{numbers[-1]}{ENDCOLOR}", end="\r")
        sleep(0.05)
        print(f"{" "} * 50", end="\r")
        tmp_result = numbers[0]
        for operator, number in zip(operations, numbers[1:]):
            if operator == "+":
                tmp_result += number
            elif operator == "*":
                tmp_result *= number
            else:
                tmp_result = int(f"{tmp_result}{number}")
            if tmp_result > total:
                # If we have surpassed the expected result, skip to the next test
                break
        if tmp_result == total:
            # If the final result is correct, return a True
            return True, operations
    return False, None


def part1(dataInput):
    result = 0
    for line in dataInput:
        total, numbers = line
        test_cases = len(numbers) - 1
        # print(f"Checking {2 ** test_cases} - ", end="")
        test_signs = list(product(operators_list, repeat=test_cases))
        test_signs_sorted = sorted(test_signs)
        valid, operations = test_calcs(total, numbers, test_signs_sorted)
        if valid:
            print(f"{BGREEN}{total} = ", end="")
            for idx, number in enumerate(numbers[:-1]):
                print(f"{BBLUE}{number} {BGREEN}{operations[idx]} ", end="")
            print(f"{BBLUE}{numbers[-1]}{ENDCOLOR}")
            result += total
        else:
            print(f"{BRED}{total} ≠ ", end="")
            for idx, number in enumerate(numbers[:-1]):
                print(f"{BBLUE}{number} {BRED}? ", end="")
            print(f"{BBLUE}{numbers[-1]}{ENDCOLOR}")
            pass
    print(result)


def part2(dataInput):
    result = 0
    for line in dataInput:
        total, numbers = line
        test_cases = len(numbers) - 1
        # print(f"Checking {3 ** test_cases} - ", end="")
        test_signs = list(product(operators_list_2, repeat=test_cases))
        valid, operations = test_calcs(total, numbers, test_signs)
        if valid:
            print(f"{BGREEN}{total} = ", end="")
            for idx, number in enumerate(numbers[:-1]):
                print(f"{BBLUE}{number} ", end="")
                if operations[idx] == "%":
                    print(f"{BGREEN}‖ ", end="")
                else:
                    print(f"{BGREEN}{operations[idx]} ", end="")
            print(f"{BBLUE}{numbers[-1]}{ENDCOLOR}")
            result += total
        else:
            print(f"{BRED}{total} ≠ ", end="")
            for idx, number in enumerate(numbers[:-1]):
                print(f"{BBLUE}{number} {BRED}? ", end="")
            print(f"{BBLUE}{numbers[-1]}{ENDCOLOR}")
            pass
    print(result)


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
