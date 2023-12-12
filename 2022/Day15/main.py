from AOC import AOC, getDateYear, manhattan_dist
from TerminalColors import *

testing = False
minXToCheck = minYToCheck = 0
tuningFreqMulti = 4000000
if testing:
    yToCheck = 10
    maxXToCheck = maxYToCheck = 20
else:
    yToCheck = 2000000
    maxXToCheck = maxYToCheck = 4000000


def parse_input(codeInput):
    sensors = dict()
    beacons = dict()
    lines = codeInput.find_all_in_lines("-*\d+")
    for line in lines:
        sensor = (int(line[0]), int(line[1]))
        beacon = (int(line[2]), int(line[3]))
        dist = manhattan_dist(sensor, beacon)
        sensors[sensor] = {"dist": dist, "closest": beacon}
        beacons[beacon] = {"dist": float("inf"), "closest": ""}

    return sensors, beacons


def findMinMaxPoints(sensors):
    xMin = float("inf")
    xMax = -float("inf")
    for sensorPoint, sensorData in sensors.items():
        x = sensorPoint[0]
        dist = sensorData["dist"]
        if x - dist < xMin:
            xMin = x - dist
        if x + dist > xMax:
            xMax = x + dist
    return xMin, xMax


def part1(sensors, beacons):
    xMin, xMax = findMinMaxPoints(sensors)

    count = 0
    for x in range(xMin, xMax):
        pointToCheck = (x, yToCheck)
        if x % 1000 == 0:
            pass
            # print(f"Checking Point {pointToCheck} in range ({xMin, xMax})")
        for sensorPoint, sensorData in sensors.items():
            if (manhattan_dist(pointToCheck, sensorPoint) <= sensorData["dist"]) and (
                pointToCheck not in beacons.keys()
            ):
                count += 1
                break
    print(count)


def part2(dataInput):
    pass


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    sensors, beacons = parse_input(codeInput)

    part1(sensors, beacons)
    # part2(dataInput)


if __name__ == "__main__":
    main()
