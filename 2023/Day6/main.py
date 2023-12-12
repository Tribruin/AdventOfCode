from AOC import AOC, getDateYear
from TerminalColors import *

testing = False


def parse_input(codeInput: AOC):
    data = codeInput.find_all_ints_in_lines()
    result = list()
    for i in range(len(data) + 1):
        result.append((data[0][i], data[1][i]))
    return result


def distsTravelled(time):
    dists = list()
    for sec in range(1, time):
        speed = sec
        dist = (time - sec) * speed
        dists.append(dist)
    return dists


def part1(dataInput):
    total = 1
    for time, winDist in dataInput:
        dists = distsTravelled(time)
        totalWins = sum(1 for i in dists if i > winDist)
        print(f"Dist: {winDist} - Winners {totalWins}")
        total *= totalWins
    print(total)


def part2(dataInput):
    totalTimeStr = ""
    totalDistStr = ""
    for time, winDist in dataInput:
        totalTimeStr += str(time)
        totalDistStr += str(winDist)

    totalTime = int(totalTimeStr)
    totalDist = int(totalDistStr)

    dists = distsTravelled(totalTime)
    totalWins = sum(1 for i in dists if i > totalDist)
    print(totalWins)


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
