inputFile = "/Users/rblount/Scripts/AdventOfCode/2015/Day8-Input.txt"
# inputFile = ""


def readFile(filename):
    f = open(filename, "r")
    lines = []

    for line in f.readlines():
        tempLine = line.rstrip()
        textInMemoryLen = decodeString(tempLine)
        textExpandedLen = encodeeString(tempLine)
        lines.append(
            {
                "text": tempLine,
                "textLength": len(tempLine),
                "charMemory": textInMemoryLen,
                "encodeLen": textExpandedLen,
            }
        )
        # print(lines)

    return lines


def decodeString(stringToProcess):
    counter = 0
    i = 0
    length = len(stringToProcess)
    while i < length:
        char = stringToProcess[i]
        if char == "\\":
            if stringToProcess[i + 1] == '"' or stringToProcess[i + 1] == "\\":
                counter += 1
                i += 2
            elif stringToProcess[i + 1] == "x":
                counter += 1
                i += 4
            else:
                counter += 1
                i += 1
        else:
            counter += 1
            i += 1

    # Remove the count for the leading and trailing "s
    counter -= 2
    return counter


def encodeeString(stringToProcess):
    counter = 0
    i = 0
    length = len(stringToProcess)
    while i < length:
        char = stringToProcess[i]
        if char == "\\":
            counter += 2
            i += 1
        elif char == '"':
            counter += 2
            i += 1
        else:
            counter += 1
            i += 1

    # Add the leading and training "s
    counter += 2
    return counter


textLines = readFile(inputFile)
sumOfChars = sum([i["textLength"] for i in textLines])
memoryChars = sum([i["charMemory"] for i in textLines])
expandedChar = sum([i["encodeLen"] for i in textLines])
print(sumOfChars, memoryChars, sumOfChars - memoryChars)
print(expandedChar, sumOfChars, expandedChar - sumOfChars)
