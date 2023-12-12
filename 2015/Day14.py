# inputFile = "/Users/rblount/OneDrive/AdventOfCode/2015/Day14-Input-Test.txt"
inputFile = "Day14-Input.txt"

totalTime = 2503

def readFile(fileName):
    reindeers = list()
    f = open(fileName, "r")
    for line in f.readlines():
        lineSplit = line.rstrip().split()
        name = lineSplit[0]
        speed = int(lineSplit[3])
        duration = int(lineSplit[6])
        rest = int(lineSplit[13])
        reindeers.append({  'name': name, 
                            'speed': speed, 'duration': duration,
                            'rest': rest, 'moving': True, 'time': 0,
                            'dist': 0, 'score': 0})

    return reindeers


def moveReindeer(reindeer):
    if reindeer['moving']:
        reindeer['dist'] += reindeer['speed']
        reindeer['time'] += 1
        # print(f"Moved {reindeer['speed']} spaces to {reindeer['dist']}", end="")
        if reindeer['time'] == reindeer['duration']:
            reindeer['moving'] = False
            reindeer['time'] = 0
            # print(" - STOPPING", end="")

    else:
        reindeer['time'] += 1
        # print(f"stopped for {reindeer['time']} seconds", end="")
        if reindeer['time'] == reindeer['rest']:
            reindeer['moving'] = True
            reindeer['time'] = 0
            # print(" - Startng ", end="")
    return reindeer


reindeers = readFile(inputFile)
print(reindeers)
for i in range(totalTime):
    for reindeerName in reindeers:
        # print(f"{i+1} seconds: {reindeerName}: ", end="")
        moveReindeer(reindeerName)
        # reindeerName = moveReindeer(reindeerName)
        # print()

    reindeers = sorted(reindeers, key = lambda i : i['dist'], reverse = True)
    reindeers[0]['score'] += 1
    for reindeer in reindeers[1:]:
        if reindeer['dist'] == reindeers[0]['dist']:
            reindeer['score'] += 1

reindeers = sorted(reindeers, key = lambda i : i['dist'], reverse = True)
print("Sorted by distance")
for reindeer in reindeers:
    print(f"{reindeer['name']} moved a total of {reindeer['dist']}")


reindeers = sorted(reindeers, key = lambda i : i['score'], reverse = True)
print("Sorted by score")
for reindeer in reindeers:
    print(f"{reindeer['name']} scored a total of {reindeer['score']}")


