from itertools import combinations
inputFile = "/Users/rblount/OneDrive/AdventOfCode/2015/Day17-Input.txt"

totalVolume = 150

# jars = [20, 15, 10, 5, 5]

def readFile():
    jars = list()
    f = open(inputFile, "r")
    for line in f.readlines():
        jars.append(int(line.rstrip()))

    return jars

jars = readFile()

def part1():
    jarsToCheck = []
    for i in range(4, len(jars)-1):
        jarsToCheck += list(combinations(jars, i))

    count = 0
    for jarSet in jarsToCheck: 
    # print(list(jarSet), sum(list(jarSet)))
        if sum(list(jarSet)) == totalVolume:
            count += 1

    print(count) 

def part2():

    jarsToCheck = []
    i = 4
    count = 0
    while count == 0:
        jarsToCheck = list(combinations(jars, i))
        for jarSet in jarsToCheck: 
    # print(list(jarSet), sum(list(jarSet)))
            if sum(list(jarSet)) == totalVolume:
                count += 1
        i += 1

    print(count, i) 

part1()
part2()