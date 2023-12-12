from AOC import AOC, getDateYear
from TerminalColors import *

testing = False

# Adding a comment
# Adding a second comment


def parse_input(codeInput: AOC):
    result = codeInput.find_all_ints_in_lines()
    return result


def printLine(line, indent, spacing):
    if not testing:
        return
    indentSpace = " " * (indent) * spacing
    print(indentSpace, end="")
    for i in line[:-1]:
        print(f"{str(i):^{spacing}} ", end="")
    print(f"{RED}{line[-1]:^{spacing}}{ENDCOLOR}")
    return


def part1(dataInput):
    def findDiffBetweenNumbers(sequence: list, depth, spacing):
        newSeq = list()
        for x in range(0, len(sequence) - 1):
            value = sequence[x + 1] - sequence[x]
            newSeq.append(value)
        if len(set(newSeq)) == 1:
            returnValue = newSeq[0]
            # printLine(newSeq + [newSeq[0]], depth + 1, spacing)
            returnValue = returnValue + sequence[-1]
            # printLine(sequence + [returnValue], depth, spacing)
            return returnValue
        else:
            returnValue = (
                findDiffBetweenNumbers(newSeq, depth + 1, spacing) + sequence[-1]
            )
            printLine(sequence + [returnValue], depth, spacing)
            return returnValue

    total = 0
    maxIntLength = 0
    for line in dataInput:
        maxInt = max(line)
        if len(str(maxInt)) > maxIntLength:
            maxIntLength = len(str(maxInt))
    if maxIntLength % 2 == 0:
        maxIntLength += 1

    for line in dataInput:
        newDiffValue = findDiffBetweenNumbers(line, 0, maxIntLength)
        print()
        total += newDiffValue
    print(f"Final Total: {total}")


def part2(dataInput):
    def findDiffBetweenNumbers(sequence: list):
        newSeq = list()
        for x in range(0, len(sequence) - 1):
            value = sequence[x + 1] - sequence[x]
            newSeq.append(value)
        if len(set(newSeq)) == 1:
            newDiffValue = newSeq[0]
            return sequence[0] - newDiffValue
        else:
            newDiffValue = sequence[0] - findDiffBetweenNumbers(newSeq)
            return newDiffValue

    total = 0

    for line in dataInput:
        newDiffValue = findDiffBetweenNumbers(line)
        # print(newDiffValue)
        total += newDiffValue
    print(f"Final Total: {total}")


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
