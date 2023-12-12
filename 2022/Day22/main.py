
import re
from time import sleep
from os import system
from AOC import AOC, getDateYear, addTuples
from TerminalColors import *

testing = False
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
directionArrows = [">", "v", "<", "^"]
rotateMoves = {"L": -1, "R": 1}
printHeight = 40


def parse_input(codeInput):
    openSpaces = list()
    walls = list()
    x = y = 1
    for line in codeInput.read_lines_no_strip()[:-2]:
        for char in line:
            if char == ".":
                openSpaces.append((x, y))
            elif char == "#":
                walls.append((x, y))
            else:
                pass
            x += 1
        x = 1
        y += 1

    moves = re.findall('\d+[A-Z]', codeInput.read_lines()[-1])

    return (openSpaces, walls, moves)


def printMap(currPos, currDir, lastMove):
    system('clear')
    print(f"Last Move: {lastMove}")
    maxX = max(x[0] for x in allSpaces)
    maxY = max(y[1] for y in allSpaces)
    currY = currPos[1]
    if maxY < printHeight:
        minYPrint = 1
        maxYPrint = maxY + 1
    elif currY < printHeight:
        minYPrint = 1
        maxYPrint = printHeight + 1
    elif (maxY - currY) < printHeight:
        minYPrint = maxY - printHeight
        maxYPrint = printHeight + 1
    else:
        minYPrint = currY - printHeight // 2
        maxYPrint = currY + printHeight // 2 + 1

    print("    ", end="")
    for x in range(1, maxX + 1):
        if x // 100 != 0:
            print(f"{x // 100}", end="")
        else:
            print(" ", end="")
    print()
    print("    ", end="")
    for x in range(1, maxX + 1):
        if (x > 100) or x // 10 != 0:
            print(f"{(x % 100) // 10 }", end="")
        else:
            print(" ", end="")
    print()
    print("    ", end="")
    for x in range(1, maxX + 1):
        print(x % 10, end="")
    print()

    for y in range(minYPrint, maxYPrint):
        print(f"{y:>4}", end="")
        for x in range(1, maxX + 1):
            if (x, y) == currPos:
                print(f"{BBLUE}{directionArrows[currDir]}{ENDCOLOR}", end="")
            elif (x, y) in previousSpaces.keys():
                print(f"{WHITE}{directionArrows[previousSpaces[(x,y)]]}{ENDCOLOR}", end="")
            elif (x, y) in openSpaces:
                print(f"{GREEN}.{ENDCOLOR}", end="")
            elif (x, y) in walls:
                print(f"{RED}#{ENDCOLOR}", end="")
            else:
                print(" ", end="")
        print()
    print()
    pass


def makeMovePart1(currPos, currDir, currMove):
    moves = int(currMove[:-1])
    rotate = currMove[-1]
    for _ in range(moves):
        previousSpaces[currPos] = currDir
        newPos = addTuples(currPos, directions[currDir])
        if newPos not in allSpaces:
            match currDir:
                case 0:
                    newY = currPos[1]
                    newX = min([i[0] for i in allSpaces if i[1] == newY])
                case 1:
                    newX = currPos[0]
                    newY = min([i[1] for i in allSpaces if i[0] == newX])
                case 2:
                    newY = currPos[1]
                    newX = max([i[0] for i in allSpaces if i[1] == newY])
                case 3:
                    newX = currPos[0]
                    newY = max([i[1] for i in allSpaces if i[0] == newX])
            newPos = (newX, newY)
        if newPos in openSpaces:
            currPos = newPos
        elif newPos in walls:
            # Hit a wall, so stop now!
            break

    currDir = (currDir + rotateMoves[rotate]) % 4

    return currPos, currDir


def part1(dataInput):
    global openSpaces
    global walls
    global allSpaces
    global previousSpaces
    openSpaces, walls, moves = dataInput
    allSpaces = openSpaces + walls
    previousSpaces = dict()
    currDir = 0
    y = 1
    x = min([x[0]for x in openSpaces if x[1] == 1])
    currPos = (x, y)

    # printMap(currPos, currDir, "0R")

    for move in moves:
        # sleep(0.5)
        previousSpaces[currPos] = currDir
        currPos, currDir = makeMovePart1(currPos, currDir, move)

    # printMap(currPos, currDir, move)
    print(currPos, currDir)
    print(1000 * currPos[1] + 4 * currPos[0] + currDir)


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
