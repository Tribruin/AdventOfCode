from AOC import AOC, getDateYear
from TerminalColors import *
import re

testing = False


def parse_input_part1(codeInput: AOC):
    lines = codeInput.read_lines()
    result = dict()
    symbolPos = list()
    for lineno, line in enumerate(lines):
        numbers = re.findall("\d+", line)
        copyLine = line
        for number in numbers:
            xpos = copyLine.find(number)
            result[(xpos, lineno)] = number
            copyLine = copyLine.replace(number, "." * len(number), 1)
        symbols = re.finditer("[^0-9.]", line)
        for symbol in symbols:
            symbolPos.append((symbol.start(), lineno))
    return result, symbolPos, lines


def parse_input_part2(codeInput: AOC):
    lines = codeInput.read_lines()
    result = dict()
    symbolPos = list()
    for lineno, line in enumerate(lines):
        numbers = re.findall("\d+", line)
        copyLine = line
        for number in numbers:
            xpos = copyLine.find(number)
            result[(xpos, lineno)] = number
            copyLine = copyLine.replace(number, "." * len(number), 1)
        symbols = re.finditer("\*", line)
        for symbol in symbols:
            symbolPos.append((symbol.start(), lineno))
    return result, symbolPos, lines


def nextToSymbol(numStart, symbolsList, length) -> bool:
    xStart, y = numStart
    xEnd = xStart + length

    # Check Row Above
    for xPos in range(xStart - 1, xEnd + 1):
        # print(f"Checking ({xPos, y-1})")
        if (xPos, y - 1) in symbolsList:
            print(f"    Found Symbol @ ({xPos, y-1})")
            return True

    # If not found alrady:
    # print(f"Checking ({xStart-1}, {y}) and ({xEnd}, {y}))")
    if (xStart - 1, y) in symbolsList or (xEnd, y) in symbolsList:
        print(f"    Found Symbol @ ({xStart - 1}, {y}) or ({xEnd, y})")
        return True

    # If not found already
    for xPos in range(xStart - 1, xEnd + 1):
        # print(f"Checking ({xPos, y+1})")
        if (xPos, y + 1) in symbolsList:
            print(f"    Found Symbol @ ({xPos, y+1})")
            return True
            break

    return False


def part1(numbers: dict, symbolPos: list, schematic: list):
    total = 0
    for pos, number in numbers.items():
        print(f"Check {number} @ {pos}")
        isFound = nextToSymbol(pos, symbolPos, len(number))
        if isFound:
            print(f"    Found Match {number} @ {pos}")
            total += int(number)
        else:
            print(f"    No Symbol Found")
    print(total)


def part2(numbers: dict, asterisks: list, schemantic: list):
    total = 0

    for asteriskPos in asterisks:
        x, y = asteriskPos
        foundNumbers = list()

        for (numX, numY), number in numbers.items():
            # Check if the number is in the line above or below
            minX = numX - 1
            maxX = numX + len(number)
            if numY == y - 1 or numY == y + 1:
                if minX <= x <= maxX:
                    foundNumbers.append(int(number))

            # Check if the number is in the same line
            elif numY == y:
                if maxX == x or minX == x:
                    foundNumbers.append(int(number))

        if len(foundNumbers) == 2:
            total += foundNumbers[0] * foundNumbers[1]

    print(total)


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    dataInput, symbolPos, schematic = parse_input_part1(codeInput)

    # part1(dataInput, symbolPos, schematic)

    dataInput, symbolPos, schematic = parse_input_part2(codeInput)
    part2(dataInput, symbolPos, schematic)


if __name__ == "__main__":
    main()
