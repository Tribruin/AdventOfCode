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
    def find_time(next_bus, start_time, step):
        time_period, time_delta = next_bus
        while (start_time + time_delta) % time_period != 0:
            start_time += step
        return start_time

    buses = [
        (int(y), int(x)) for x, y in enumerate(a.read_lines()[1].split(",")) if y != "x"
    ]
    time = step = buses[0][0]
    for bus in buses[1:]:
        time = find_time(bus, time, step)
        step *= bus[0]
    print(time)


a = AOC(13, test=False)
print(timeit(part1, number=1))
print(timeit(part2, number=1))