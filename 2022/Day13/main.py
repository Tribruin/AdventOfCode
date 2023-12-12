
from AOC import AOC, getDateYear
import re
import ast
import json
from TerminalColors import *

testing = True


def parse_input(codeInput):
    lines = codeInput.read_lines()
    result = list()
    for i in range(0, len(lines), 3):
        # result.append((ast.literal_eval(lines[i]), ast.literal_eval(lines[i+1])))   # Research Literal_Eval
        packet1 = json.loads(lines[i])
        packet2 = json.loads(lines[i+1])
        result.append((packet1, packet2))
    return result


def compareLeftRight(left, right, depth):

    # print(f"{' '  * depth * 2} - Compare: {left} vs {right}")
    depth += 1
    valid = True
    complete = False
    lenLeft = len(left)
    lenRight = len(right)

    for i in range(lenLeft):
        if i + 1 > lenRight:
            print(f"{' ' * (depth * 2 + 4)} - Right side ran out of items, so inputs are {BOLD}not{ENDCOLOR} in the right order")
            return False, True
        leftValue = left[i]
        rightValue = right[i]
        leftType = type(leftValue)
        rightType = type(rightValue)
        print(f"{' ' * (depth * 2 + 2)} - Compare {leftValue} vs {rightValue}")
        if leftType == int and rightType == int:
            # print(f"{' '  * depth * 2} - Compare: {left} vs {right}")
            if leftValue < rightValue:
                print(f"{' ' * (depth * 2 + 4)} - Left side is smaller, so inputs are {BOLD}in the right order{ENDCOLOR}")
                return True, True
            elif leftValue > rightValue:
                print(f"{' ' * (depth * 2 + 4 )} - Right side is smaller, so inputs are {BOLD}not{ENDCOLOR} in the right order")
                return False, True
            else:
                pass
        else:
            if leftType == int:
                print(f"{' ' * (depth * 2 + 4)} - Mixed types; covert left to [{leftValue}] and retry comparison")
                leftValue = [leftValue]
            if rightType == int:
                print(f"{' ' * (depth * 2 + 4)} - Mixed types; covert right to [{rightValue}] and retry comparison")
                rightValue = [rightValue]
            valid, complete = compareLeftRight(leftValue, rightValue, depth + 1)
            if complete:
                break

    complete = False
    if complete:
        if valid:
            print(f"{' ' * (depth * 2 + 4)} - Left side ran out of items, so inputs are {BOLD}in the right order{ENDCOLOR}")

    return valid, complete


def part1(dataInputs):

    validInput = 0
    for x, dataInput in enumerate(dataInputs):
        print(f"== Pair {x + 1} ==")
        left, right = dataInput
        print(f"{' ' * 2} - Compare: {left} vs {right}")
        valid, _ = compareLeftRight(left, right, 0)
        print()

        if valid:
            validInput += (x+1)
            print(f"== Pair {x+1} == is {GREEN}VALID{ENDCOLOR}")
        else:
            print(f"== Pair {x+1} == is {RED}NOT VALID{ENDCOLOR}")

        print(f"Current Total: {validInput}")
        print()

    print(validInput)


def part2(dataInput):
    pass


def main():

    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    dataInput = parse_input(codeInput)

    part1(dataInput)
    # part2(dataInput)


if __name__ == "__main__":
    main()
