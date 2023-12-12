
import re
from collections import deque
from AOC import AOC, getDateYear
from TerminalColors import *

testing = True
totalTimeInTunnel = 30


def parse_input(codeInput):
    result = dict()
    for line in codeInput.read_lines():
        temp = line.split()
        name = temp[1]
        rate = int(re.findall('\d+', temp[4])[0])
        nextValves = [x[0:2] for x in temp[9:]]
        if rate == 0:
            time = 1
        else:
            time = 2
        result[name] = {'rate': rate, 'next': nextValves, 'time': time}
    return result


def calculateFlow(currentPath: deque, valves: dict) -> int:
    currentFlow = 0
    valvesOpened = deque()
    timeElapsed = 0
    flowRates = list()
    currentTotalFlow = 0

    while len(currentPath) != 0:

        currentValve, opened = currentPath.popleft()
        currentTotalFlow += currentFlow  # Add Flow for previous minute
        print(f"== Minute {timeElapsed} ==")
        if len(valvesOpened) == 0:
            print("No valves opened")
        else:
            print("Value ", end="")
            for i, _, _ in valvesOpened:
                print(f"{i}, ", end="")
            print(f"are open for {currentTotalFlow} pressure")

        print(f"You moved to valve {currentValve}")
        print()
        timeElapsed += 1

        if opened:
            currentTotalFlow += currentFlow                 # Add for minut to open valve
            flowRates.append(currentFlow)
            print(f"== Minute {timeElapsed} ==")

            if currentFlow == 0:
                print("No valves opened")
            else:
                print("Value ", end="")
                for i, _, _ in valvesOpened:
                    print(f"{i}, ", end="")
                print(f"are open for {currentFlow} pressure")
            print(f"You open valve {currentValve}")
            print()

            # if len(valvesOpened) == 0:
            #     currentTotalFlow = 0
            # else:
            #     currentTotalFlow = valvesOpened[-1][2]
            currentFlow += valves[currentValve]['rate']
            valvesOpened.append((currentValve, timeElapsed, currentFlow))
            timeElapsed += 1

    for timeCount in range(timeElapsed, totalTimeInTunnel + 1):
        print(f"== Minute {timeCount} ==")
        print("Values ", end="")
        for valveName, _, _ in valvesOpened:
            print(f"{valveName}, ", end="")
        print(f"are open for {currentFlow} pressure")
        print()

    totalFlow = 0
    currentFlow = 0
    for i in range(0, totalTimeInTunnel+1):
        totalFlow += currentFlow
        if len(valvesOpened) > 0:
            if i > valvesOpened[0][1]:
                currentFlow = valvesOpened[0][2]
                valvesOpened.popleft()

    totalFlow += currentFlow

    print(totalFlow)

    return totalFlow


def part1(valves):
    startingPath = 'AA'
    fullPath = [('AA', False), ('DD', True), ('CC', False), ('BB', True), ('AA', False),
                ('II', False), ('JJ', True), ('II', False), ('AA', False), ('DD', False), ('EE', False), ('FF', False), ('GG', False), ('HH', True), ('GG', False), ('FF', False), ('EE', True), ('DD', False), ('CC', True)]
    fullPath = deque(fullPath)
    print(calculateFlow(fullPath, valves))


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
