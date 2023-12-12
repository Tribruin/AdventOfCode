from AOC import AOC, getDateYear
from TerminalColors import *

testing = False


def parse_input(codeInput):
    foundMonkeys = dict()
    unfoundMonkeys = dict()
    for monkeyName, value in codeInput.split_lines(":"):
        valueSplit = value.split()
        if len(valueSplit) == 1:
            foundMonkeys[monkeyName] = int(valueSplit[0])
        else:
            unfoundMonkeys[monkeyName] = valueSplit

    return (foundMonkeys, unfoundMonkeys)


def processMonkey(monkeyName):
    # print(f"Processing Monkey: {monkeyName}")
    if monkeyName in foundMonkeys.keys():
        # print(f"  Returning {foundMonkeys[monkeyName]} for {monkeyName}")
        return foundMonkeys[monkeyName]
    monkey1, operand, monkey2 = unfoundMonkeys[monkeyName]
    match operand:
        case "+":
            result = processMonkey(monkey1) + processMonkey(monkey2)
        case "-":
            result = processMonkey(monkey1) - processMonkey(monkey2)
        case "*":
            result = processMonkey(monkey1) * processMonkey(monkey2)
        case "/":
            result = processMonkey(monkey1) / processMonkey(monkey2)
    foundMonkeys[monkeyName] = result
    # print(f"  Returning {foundMonkeys[monkeyName]} for {monkeyName}")÷
    return result


def part1(dataInput):
    global foundMonkeys
    global unfoundMonkeys
    foundMonkeys, unfoundMonkeys = dataInput
    processMonkey("root")
    print(f"Monkey root will yell: {int(foundMonkeys['root'])}")


def part2(code):
    found = False
    humn = 0
    # humn = 3423279932930
    # humnDelta = 1000000000000
    humnDelta = 10**12
    global foundMonkeys
    global unfoundMonkeys
    foundMonkeys, unfoundMonkeys = parse_input(code)
    monkey1, monkey2 = unfoundMonkeys["root"][0], unfoundMonkeys["root"][2]
    num2 = processMonkey(monkey2)
    oldNum1 = 0
    while not found:
        foundMonkeys, unfoundMonkeys = parse_input(code)
        oldHumn = humn
        humn += humnDelta
        monkey1, monkey2 = unfoundMonkeys["root"][0], unfoundMonkeys["root"][2]
        foundMonkeys["humn"] = humn
        num1 = processMonkey(monkey1)
        num2 = processMonkey(monkey2)
        print(f"Proessing humn: {humn} - Result {num1} & {num2} - Delta {humnDelta}")
        if num1 == num2:
            found = True
        elif num1 < num2:
            humn = oldHumn
            humnDelta = humnDelta // 10

    print(f"Proessing humn: {humn} - Result {int(num1)} & {int(num2)}")


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    dataInput = parse_input(codeInput)

    part1(dataInput)
    part2(codeInput)


if __name__ == "__main__":
    main()
