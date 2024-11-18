from AOC import AOC, getDateYear, findLenXLenY, addTuples
from TerminalColors import *

testing = True
moves = {">": (1, 0), "V": (0, 1), "<": (-1, 0), "^": (0, -1), ".": (0, 0)}
newDirects = {
    "\\": {
        ">": ["V"],
        "V": [">"],
        "<": ["^"],
        "^": ["<"],
    },
    "/": {">": ["^"], "V": ["<"], "<": ["V"], "^": [">"]},
    "-": {">": [">"], "V": ["<", ">"], "<": ["<"], "^": ["<", ">"]},
    "|": {">": ["^", "V"], "V": ["V"], "<": ["^", "V"], "^": ["^"]},
    ".": {">": [">"], "V": ["V"], "<": ["<"], "^": ["^"]},
}


def parse_input(codeInput: AOC):
    result = dict()
    for y, line in enumerate(codeInput.read_lines()):
        for x, point in enumerate(line):
            result[(x, y)] = point
    return result


def printMap(mirrorMap: dict, currentPos=(0, 0), currentDir=">"):
    (minX, minY), (maxX, maxY) = findLenXLenY(mirrorMap.keys())
    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            if (x, y) == currentPos:
                print(f"{BBLUE}{currentDir}{ENDCOLOR}", end="")
            elif lightMap[(x, y)] > 0:
                if mirrorMap[(x, y)] in ["\\", "/", "|", "-"]:
                    print(f"{BYELLOW}{mirrorMap[(x,y)]}{ENDCOLOR}", end="")
                else:
                    print(f"{BYELLOW}#{ENDCOLOR}", end="")
            else:
                print(f"{mirrorMap[(x, y)]}{ENDCOLOR}", end="")
        print()
    print()


def mapLightToEnd(mirrorMap, pos, dir):
    (xMin, yMin), (xMax, yMax) = findLenXLenY(mirrorMap)
    pathFollowed = list()
    while xMin <= pos[0] <= xMax and yMin <= pos[1] <= yMax:
        printMap(mirrorMap, pos, dir)
        pathFollowed.append((pos, dir))
        lightMap[pos] += 1
        nextPos = addTuples(pos, moves[dir])
        if nextPos not in mirrorMap.keys():
            # printMap(mirrorMap, pos, dir)
            pos = nextPos
            continue
        nextMirror = mirrorMap[nextPos]
        nextDir = newDirects[nextMirror][dir]
        if (nextPos, nextDir) in pathFollowed:
            print("Found a Loop")
            return nextPos, nextDir

        pos = nextPos
        if len(nextDir) == 1:
            dir = nextDir[0]
        else:
            for testDir in nextDir:
                print("{BRED}Checking new split direction")
                mapLightToEnd(mirrorMap, pos, testDir)


def part1(mirrorMap: dict):
    global lightMap
    lightMap = dict()
    for point in mirrorMap:
        lightMap[point] = 0

    startPoint = (0, 0)
    currentDir = ">"
    returnedPos, returnedDir = mapLightToEnd(mirrorMap, startPoint, currentDir)


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
