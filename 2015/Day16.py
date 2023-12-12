inputFile = "Day16-Input.txt"
traitsFile = "Day16-Traits.txt"


def readInput():
    sues = []
    f = open(inputFile, "r")
    for line in f.readlines():
        sue = {}
        lineSplit = line.split(",")
        sue["name"] = lineSplit[0].split(":")[0].strip()
        sue[lineSplit[0].split(":")[1].strip()] = int(lineSplit[0].split(":")[2])
        sue[lineSplit[1].split(":")[0].strip()] = int(lineSplit[1].split(":")[1])
        sue[lineSplit[2].split(":")[0].strip()] = int(lineSplit[2].split(":")[1])

        sues.append(sue)

    return sues


def readTraits():
    f = open(traitsFile, "r")
    traits = {}
    for line in f.readlines():
        lineSplit = line.split(":")
        traits[lineSplit[0].strip()] = int(lineSplit[1].strip())
    return traits


def checkForTraitPart1(sues, keyToCheck, valueToCheck):
    # Takes a list of "Sues" and returns an updated list where either key/value pair match or
    # key/value pair do not exist

    returnSues = []
    for sue in sues:
        value = sue.get(keyToCheck)
        if value == valueToCheck or value == None:
            returnSues.append(sue)

    return returnSues


def checkForTraitPart2(sues, keyToCheck, valueToCheck):
    # Takes a list of "Sues" and returns an updated list where either key/value pair match or
    # key/value pair do not exist

    fewerThan = ["pomeranians", "goldfish"]
    greaterThan = ["cats", "trees"]
    returnSues = []
    for sue in sues:
        value = sue.get(keyToCheck)
        if keyToCheck in set(fewerThan):
            if value == None:
                returnSues.append(sue)
            elif value < valueToCheck:
                returnSues.append(sue)
        elif keyToCheck in set(greaterThan):
            if value == None:
                returnSues.append(sue)
            elif value > valueToCheck:
                returnSues.append(sue)
        elif value == None:
            returnSues.append(sue)
        elif value == valueToCheck:
            returnSues.append(sue)

    return returnSues


sues = readInput()
traits = readTraits()

# print(checkForTrait(sues, "children", 3))

# Part 1
for key, value in traits.items():
    sues = checkForTraitPart1(sues, key, value)
print(sues)

# Part 2
sues = readInput()
for key, value in traits.items():
    sues = checkForTraitPart2(sues, key, value)
print(sues)
