import re
from itertools import combinations
from AOC import AOC, getDateYear
from TerminalColors import *

testing = True


def parse_input(codeInput: AOC):
    result = list()
    lines = codeInput.read_lines()
    for line in lines:
        springs, counts = line.split()
        icounts = [int(x) for x in counts.split(",")]
        result.append((springs, icounts))
    return result


def countSprings(springLine):
    springs = re.findall("#+", springLine)
    count = [len(x) for x in springs]
    return count


def subSting(oldString, replaceChar, loc):
    return oldString[:loc] + replaceChar + oldString[loc + 1 :]


def findAllCombos(springLine, springCount):
    # Find all the matching combinations that match the count at the
    # start of the string springLine

    allFound = False
    i = 0
    totalCount = 0
    while not allFound:
        subLine = springLine[i : i + springCount]
        missingPos = [x.start() for x in re.finditer("\?", subLine)]
        possibleSubs = combinations(missingPos, springCount)
        for possibleSub in possibleSubs:
            subCount = 0
            tempLine = subLine
            for k in possibleSub:
                tempLine = subSting(tempLine, "#", k)
            # print(tempLine, countSprings(tempLine))
            if countSprings(tempLine) == [springCount]:
                subCount += 1
        totalCount += subCount
        if subCount == 0:
            break
        i += 1


# def part1(springLines):
#     totalCount = 0
#     for line, counts in springLines:
#         totalToReplace = sum(counts) - sum(countSprings(line))
#         missingPos = [x.start() for x in re.finditer("\?", line)]
#         possibleSubs = combinations(missingPos, totalToReplace)
#         for possibleSub in possibleSubs:
#             tempLine = line
#             for i in possibleSub:
#                 tempLine = subSting(tempLine, "#", i)
#             # print(tempLine, countSprings(tempLine))
#             if countSprings(tempLine) == counts:
#                 totalCount += 1
#     print(totalCount)


def part1(springLines):
    for springLine, counts in springLines:
        findAllCombos(springLine, counts[0])


def part2(dataInput):
    # Expand the lines
    springLines = list()
    for line, counts in dataInput:
        newLine = (line + "?") * 5
        springLines.append((newLine[:-1], counts * 5))

    totalCount = 0
    for num, (line, counts) in enumerate(springLines):
        totalToReplace = sum(counts) - sum(countSprings(line))
        missingPos = [x.start() for x in re.finditer("\?", line)]
        possibleSubs = combinations(missingPos, totalToReplace)
        print(f"Line #{num} - Perms {len(list(possibleSubs))}")
        for possibleSub in possibleSubs:
            tempLine = line
            for i in possibleSub:
                tempLine = subSting(tempLine, "#", i)
            # print(tempLine, countSprings(tempLine))
            if countSprings(tempLine) == counts:
                totalCount += 1
    print(totalCount)


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
