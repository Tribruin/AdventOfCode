from AOC import AOC, getDateYear
from TerminalColors import *

testing = False
digits = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def parse_input(codeInput: AOC):
    result = codeInput.find_all_in_lines()
    return result


def part1(dataInput: AOC):
    data = dataInput.find_all_in_lines()
    x = 0
    for line in data:
        x += int(f"{line[0][0]}{line[-1][-1]}")
        print(f"{line[0][0]}{line[-1][-1]}")
    print(x)


def part2(dataInput: AOC):
    data = dataInput.read_lines()
    numberWords = digits.keys()
    total = 0
    for line in data:
        firstDigit = None
        lastDigit = None
        # Find the first number in line
        for i in range(len(line)):
            for word in numberWords:
                wordLen = len(word)
                if line[i : i + wordLen] == word:
                    firstDigit = digits[word]
                    break
            if firstDigit != None:
                break
        # print(firstDigit)
        for i in range(len(line), 0, -1):
            for word in numberWords:
                wordLen = len(word)
                if line[i - wordLen : i] == word:
                    lastDigit = digits[word]
                    break
            if lastDigit != None:
                break
        print(firstDigit, lastDigit)
        total += 10 * firstDigit + lastDigit
    print(total)


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    # dataInput = parse_input(codeInput)

    # part1(codeInput)
    part2(codeInput)


if __name__ == "__main__":
    main()
