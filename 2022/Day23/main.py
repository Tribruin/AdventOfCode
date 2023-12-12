from AOC import AOC, getDateYear, addTuples
from TerminalColors import *

testing = False
allSides = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
posToCheck = {
    0: {"dir": "north", "move": (0, -1), "check": [(-1, -1), (0, -1), (1, -1)]},
    1: {"dir": "south", "move": (0, 1), "check": [(-1, 1), (0, 1), (1, 1)]},
    2: {"dir": "west", "move": (-1, 0), "check": [(-1, -1), (-1, 0), (-1, 1)]},
    3: {"dir": "east", "move": (1, 0), "check": [(1, -1), (1, 0), (1, 1)]},
}


def parse_input(codeInput):
    result = list()
    lines = codeInput.read_lines()
    for y, line in enumerate(lines):
        for x, pos in enumerate(line):
            if pos == "#":
                result.append((x, y))
    return result


def printMap(positions):
    minX = min([i[0] for i in positions])
    maxX = max([i[0] for i in positions])
    minY = min([i[1] for i in positions])
    maxY = max([i[1] for i in positions])

    print()
    for y in range(minY - 1, maxY + 2):
        for x in range(minX - 2, maxX + 3):
            if (x, y) in positions:
                print("#", end="")
            else:
                print(".", end="")
        print()


def evalNextMove(elf, currentElfPos, startLook):
    empty = True
    for side in allSides:
        pos = addTuples(elf, side)
        # print(f"Checking {pos}")
        if pos in currentElfPos:
            empty = False
            # print("Filled")
            break

    if empty:
        return elf

    for lookAt in range(startLook, startLook + 4):
        blocked = False
        lookPos = lookAt % 4
        for pos in posToCheck[lookPos]["check"]:
            if addTuples(elf, pos) in currentElfPos:
                blocked = True
                break
        if not blocked:
            pass
            newPos = addTuples(elf, posToCheck[lookPos]["move"])
            return newPos
    return elf


def part1(dataInput):
    lookPos = 0
    elfPositions = dataInput
    # print("Starting Position")
    # printMap(elfPositions)
    for k in range(10):
        # Phase 1 - Determine possible move
        nextMoves = list()
        for elf in elfPositions:
            nextMove = evalNextMove(elf, elfPositions, lookPos)
            # print(f"{elf} -> {nextMove}")
            nextMoves.append(nextMove)

        # Phase 2 - check if two elves are moving to the same position:
        for pos in range(len(elfPositions)):
            nextMoveElf = nextMoves[pos]
            if nextMoveElf in nextMoves[pos + 1 :]:
                # find all moves wiht this pos
                replacements = [i for i, x in enumerate(nextMoves) if x == nextMoveElf]
                for i in replacements:
                    nextMoves[i] = elfPositions[i]
        elfPositions = nextMoves
        # print(f"After {k+1} moves:")
        # printMap(elfPositions)
        lookPos += 1 - 4 * (lookPos // 4)

    # Compute the min/max points:
    minX = min([i[0] for i in elfPositions])
    maxX = max([i[0] for i in elfPositions])
    minY = min([i[1] for i in elfPositions])
    maxY = max([i[1] for i in elfPositions])
    xLen = maxX - minX + 1
    yLen = maxY - minY + 1
    print((xLen * yLen) - len(elfPositions))


def part2(dataInput):
    lookPos = 0
    elfPositions = dataInput
    moves = 0
    foundNoMoves = False
    # print("Starting Position")
    # printMap(elfPositions)

    while not foundNoMoves:
        moves += 1
        # Phase 1 - Determine possible move
        nextMoves = list()
        for elf in elfPositions:
            nextMove = evalNextMove(elf, elfPositions, lookPos)
            # print(f"{elf} -> {nextMove}")
            nextMoves.append(nextMove)

        # Phase 2 - check if two elves are moving to the same position:
        for pos in range(len(elfPositions)):
            nextMoveElf = nextMoves[pos]
            if nextMoveElf in nextMoves[pos + 1 :]:
                # find all moves wiht this pos
                replacements = [i for i, x in enumerate(nextMoves) if x == nextMoveElf]
                for i in replacements:
                    nextMoves[i] = elfPositions[i]
        if nextMoves == elfPositions:
            break
        # print(f"After {k+1} moves:")
        # printMap(elfPositions)
        elfPositions = nextMoves
        lookPos += 1 - 4 * (lookPos // 4)
        if moves % 10 == 0:
            print(f"Current Move: {moves}")
    print(f"Final result: {moves}")


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
