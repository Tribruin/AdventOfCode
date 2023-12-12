from itertools import permutations, combinations

inputFile = "Day13-Input.txt"


def processInputFile(filename):

    guests = {}
    f = open(filename, "r")

    for line in f.readlines():
        lineSplit = line.rstrip().split(" ")
        guestName, gainLoss, points, neighbor = (
            lineSplit[0],
            lineSplit[2],
            int(lineSplit[3]),
            lineSplit[10][:-1],
        )
        if gainLoss == "lose":
            points = -points
        if guestName not in guests.keys():
            guests[guestName] = {}
        guests[guestName][neighbor] = points

    return guests


def calculateHappiness(seatingArrangment):
    seatingArrangment.append(seatingArrangment[0])
    # print(seatingArrangment)
    happiness = 0
    for i in range(len(seatingArrangment) - 1):
        guest1 = seatingArrangment[i]
        guest2 = seatingArrangment[i + 1]
        # print(guest1, guest2, allGuests[guest1][guest2], allGuests[guest2][guest1])
        happiness += allGuests[guest1][guest2] + allGuests[guest2][guest1]
    # print(happiness)
    return happiness


# Part 1
allGuests = processInputFile(inputFile)
allGuestNames = set(allGuests.keys())
allGuestSeatingArrangements = permutations(allGuestNames, len(allGuestNames))
bestHappiness = 0
for i in allGuestSeatingArrangements:
    seatingHappiness = calculateHappiness(list(i))
    if seatingHappiness > bestHappiness:
        bestHappiness = seatingHappiness
        bestArrangement = i

print(bestArrangement, bestHappiness)

# Part 2
allGuests["me"] = {}
for guest in allGuestNames:
    allGuests["me"][guest] = 0
    allGuests[guest]["me"] = 0

allGuestNames = set(allGuests.keys())
allGuestSeatingArrangements = permutations(allGuestNames, len(allGuestNames))
bestHappiness = 0
for i in allGuestSeatingArrangements:
    seatingHappiness = calculateHappiness(list(i))
    if seatingHappiness > bestHappiness:
        bestHappiness = seatingHappiness
        bestArrangement = i

print(bestArrangement, bestHappiness)
