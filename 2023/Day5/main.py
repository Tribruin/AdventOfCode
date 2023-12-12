from AOC import AOC, getDateYear
from TerminalColors import *
import math

testing = False
categories = [
    "seed",
    "soil",
    "fertilizer",
    "water",
    "light",
    "temperature",
    "humidty",
    "location",
]


def parse_input(codeInput: AOC):
    result = codeInput.find_all_ints_in_lines()
    maps = dict()
    maps["seed"] = result[0]
    i = 3
    for category in categories[1:]:
        maps[category] = list()
        while result[i] != []:
            dest, source, span = result[i]
            maps[category].append((source, dest, span))
            i += 1
        i += 2
    return maps


def part1(plantMap):
    lowestLocation = math.inf
    for seed in plantMap["seed"]:
        # print(f"Seed: {seed}, ", end="")
        location = seed
        for category in categories[1:]:
            for plantRange in plantMap[category]:
                source, dest, span = plantRange
                if source <= location < source + span:
                    location = dest + (location - source)
                    break
            # print(f"{category}: {location}, ", end="")
        # print()
        if location < lowestLocation:
            lowestLocation = location
    print(f"Starting Location: {lowestLocation}")


def part2(plantMap):
    lowestLocation = math.inf
    seeds = list()
    for i in range(0, len(plantMap["seed"]), 2):
        seeds.append((plantMap["seed"][i], plantMap["seed"][i + 1]))

    for seedStart, seedSpan in seeds:
        print(f"Running seed span {seedStart} to {seedStart + seedSpan}")
        for seed in range(seedStart, seedStart + seedSpan):
            if (seed % 100000) == 0:
                print(
                    f"Checking Seed: {(seed // 100000) * 100000:,} of {(seedStart + seedSpan):,}"
                )
            # print(f"Seed: {seed}, ", end="")
            location = seed
            for category in categories[1:]:
                for plantRange in plantMap[category]:
                    source, dest, span = plantRange
                    if source <= location < source + span:
                        location = dest + (location - source)
                        break
                # location = plantMap[category].get(location, location)
                # print(f"{category}: {location}, ", end="")
            # print()
            if location < lowestLocation:
                lowestLocation = location
    print(f"Starting Location: {lowestLocation}")


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
