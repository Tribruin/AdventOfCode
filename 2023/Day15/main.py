import re
from collections import OrderedDict
from AOC import AOC, getDateYear
from TerminalColors import *

testing = False


def parse_input(codeInput: AOC):
    result = codeInput.split_line()
    return result


def hashValue(code: str) -> int:
    wordValue = 0
    for character in code:
        wordValue += ord(character)
        wordValue = (wordValue * 17) % 256
    return wordValue


def part1(dataInput):
    totalSum = 0
    for word in dataInput:
        newValue = hashValue(word)
        print(word, newValue)
        totalSum += newValue
    print(totalSum)


def part2(dataInput):
    boxes = {x: OrderedDict() for x in range(0, 256)}
    lenses = list()
    for lens in dataInput:
        inputSplit = re.findall("^\w+|[-=]|\d", lens)
        inputSplit.append(hashValue(inputSplit[0]))
        lenses.append(inputSplit)

    for lens in lenses:
        boxNum = lens[-1]
        label = lens[0]
        box = boxes[boxNum]
        if lens[1] == "=":
            boxes[boxNum][label] = lens[2]
        elif lens[1] == "-" and label in box.keys():
            boxes[boxNum].pop(label)

    totalPower = 0
    for x, box in boxes.items():
        boxTotal = 0
        for pos, focalLength in enumerate(box.values()):
            boxTotal += (x + 1) * (pos + 1) * int(focalLength)
        totalPower += boxTotal
    print(totalPower)


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
