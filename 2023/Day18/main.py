from AOC import AOC, addTuples, getDateYear, findLenXLenY
from TerminalColors import *

testing = False
moveDirs = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}


def parse_input(codeInput: AOC):
    result = codeInput.split_lines(delimeter=" ")
    return result


def writeMapToFile(edgePoints: list, allPoints: list = list()):
    (minX, minY), (maxX, maxY) = findLenXLenY(edgePoints)
    with open("/Users/rblount/Scripts/AdventOfCode/2023/Day18/map.txt", mode="w") as f:
        for y in range(minY, maxY + 1):
            mapDrawing = ""
            for x in range(minX, maxX + 1):
                if (x, y) in edgePoints:
                    mapDrawing += "#"
                else:
                    mapDrawing += "."
            f.write(mapDrawing)
        f.close()


def printMap(edgePoints: list, allPoints: list = list()):
    (minX, minY), (maxX, maxY) = findLenXLenY(edgePoints)
    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            if (x, y) in edgePoints:
                print("#", end="")
            else:
                print(",", end="")
        print()
    print()


def isInside(point, edgePoints) -> bool:
    (x, y) = point
    inside = False
    # Test all points and how many
    if (x, y) in edgePoints:
        return False
    for x1 in range(0, x):
        if ((x1, y) in edgePoints) and ((x1, y - 1) in edgePoints):
            # check if crossing a line by check the x1,y point and one above
            # if both are in the edges, we are crossing a vertical line
            inside = not inside
    return inside


def part1(moves):
    pos = (0, 0)
    edges = [pos]
    for move in moves:
        dir, steps, color = move
        print(f"Moving: {dir} {steps}")
        for i in range(int(steps)):
            pos = addTuples(pos, moveDirs[dir])
            edges.append(pos)
    writeMapToFile(edges)

    interior = edges.copy()
    (minX, minY), (maxX, maxY) = findLenXLenY(edges)
    print(f"x: {minX} - {maxX}, y: {minY} - {maxY}")
    for y in range(minY, maxY + 1):
        print(f"Check line: {y}")
        for x in range(minX, maxX + 1):
            if isInside((x, y), edges):
                interior.append((x, y))
    # printMap(interior)
    print(len(set(interior)))


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
