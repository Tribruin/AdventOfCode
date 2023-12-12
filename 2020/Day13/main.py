import sys
from timeit import timeit

sys.path.append("/Users/rblount/Scripts/AdventOfCode/2020/tools")

from AOC import AOC


def part1():
    depart_time = int(a.read_lines()[0])
    routes = [int(x) for x in a.read_lines()[1].split(",") if x != "x"]
    next_buses = [i - (depart_time % i) for i in routes]
    next_bus_delta = min(next_buses)
    print(next_bus_delta * routes[next_buses.index(next_bus_delta)])


def part2():
    def find_time(two_buses, start_time, step):
        while True:
            time_period, time_delta = two_buses[1]
            if (start_time + time_delta) % time_period == 0:
                return start_time
            start_time += step

    buses = [
        (int(y), int(x)) for x, y in enumerate(a.read_lines()[1].split(",")) if y != "x"
    ]
    step = 1
    time = buses[0][0]
    for i in range(len(buses) - 1):
        step *= buses[i][0]
        time = find_time(buses[i : i + 2], time, step)
    print(time)


a = AOC(13, test=False)
print(timeit(part1, number=1))
print(timeit(part2, number=1))