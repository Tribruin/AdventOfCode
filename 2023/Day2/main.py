from AOC import AOC, getDateYear
from TerminalColors import *

testing = False
maxCounts = {"red": 12, "green": 13, "blue": 14}


def parse_input(codeInput: AOC):
    result = dict()
    games = codeInput.split_line_re(":|;")
    for game in games:
        gameNum = int(game[0].split()[1])
        colorCounts = game[1:]
        result[gameNum] = colorCounts

    return result


def part1(dataInput: dict):
    validGames = []
    for gameNum, draws in dataInput.items():
        maxColorCounts = {"red": 0, "green": 0, "blue": 0}  # Red, Green, Blue
        for draw in draws:
            counts = {"red": 0, "green": 0, "blue": 0}
            for cubesDrawn in draw.split(","):
                counts[cubesDrawn.split()[1]] += int(cubesDrawn.split()[0])
            # print(counts)
            for color, count in counts.items():
                if count > maxColorCounts[color]:
                    maxColorCounts[color] = count
            # print(maxColorCounts
        valid = True
        for color, count in maxColorCounts.items():
            if count > maxCounts[color]:
                valid = False
                # print("Not Valid")
                break
        if valid:
            validGames.append(gameNum)
            # print(validGames)
    print(sum(validGames))


def part2(dataInput):
    gamesPowers = []
    for gameNum, draws in dataInput.items():
        minColorCounts = {"red": 0, "green": 0, "blue": 0}
        for draw in draws:
            counts = {"red": 0, "green": 0, "blue": 0}
            for cubesDrawn in draw.split(","):
                counts[cubesDrawn.split()[1]] += int(cubesDrawn.split()[0])
            # print(counts)
            for color, count in counts.items():
                if count > minColorCounts[color]:
                    minColorCounts[color] = count
            # print(minColorCounts)
        gamePower = 1
        for count in minColorCounts.values():
            gamePower = gamePower * count
        # print(gamePower)
        gamesPowers.append(gamePower)

    print(sum(gamesPowers))


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
