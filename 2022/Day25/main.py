from AOC import AOC, getDateYear
from TerminalColors import *

testing = False
values = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
revValues = {y: x for x, y in values.items()}


def parse_input(codeInput):
    result = list()
    for line in codeInput.read_lines():
        result.append([x for x in line])
    return result


def calcSnafuNum(num) -> int:
    # if type(num) == dict:
    #     num = list(num.values())
    tempSum = 0
    power = len(num) - 1
    for char in num:
        tempSum += (5**power) * char
        power -= 1
    return tempSum


def part1(dataInput):
    total = 0
    for line in dataInput:
        tempLine = [values[x] for x in line]
        total += calcSnafuNum(tempLine)

    maxPower = -1
    found = False
    workingTotal = total
    while not found:
        maxPower += 1
        digit = total // (5**maxPower)
        if digit == 0:
            found = True

    newNumber = {x: 0 for x in range(maxPower, -1, -1)}
    for i in newNumber.keys():
        digit = workingTotal // (5**i)
        if digit <= 2:
            newNumber[i] = digit
            workingTotal = total - calcSnafuNum(newNumber.values())

        else:
            for k in range(i + 1, maxPower + 1):
                if newNumber[k] != 2:
                    newNumber[k] += 1
                    break
                else:
                    newNumber[k] = -2

            workingTotal = total - calcSnafuNum(newNumber.values())
            digit = workingTotal // (5**i)
            newNumber[i] = digit
            workingTotal = total - calcSnafuNum(newNumber.values())
    if newNumber[maxPower] == 0:
        newNumber.pop(maxPower)
    for i in newNumber.values():
        print(revValues[i], end="")
    print()


def part2(dataInput):
    pass


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
