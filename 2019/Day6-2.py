#!/usr/local/bin/python3
from operator import itemgetter
import sys

log = True
startName = "YOU"
endName = "SAN"

# Test Data

# planetInput = "Day6-Test3.txt"

# Actual Data
planetInput = "/Users/rblount/Scripts/AdventOfCode/2019/Day6-Input-Final.txt"


def printToLog(out):
    if log:
        print(out)
    return


class Planet:

    def __init__(self, objectName, parent):
        self.name = objectName
        self.moons = []
        self.parent = parent
        try:
            self.parentName = parent.name
        except:
            self.parentName = "None"
        self.planetData = self.planetData()
        if self.parent != None:
            parent.addOrbit(self)
        return

    def numberOfParentPlanets(self):
        parentOrbits = 0
        if self.parent == None:
            parentPlanets = 0
        else:
            parentPlanets = 1 + self.parent.numberOfParentPlanets()
        return parentPlanets

    def addOrbit(self, moon):
        self.moons.append(moon)
        return

    def numberOfChildOrbits(self):
        printToLog("Checking orbits for Planet {0} with Number of moons: {1}".format(self.name, len(self.moons)))
        orbits = 0
        if len(self.moons) != 0:
            for moon in self.moons:
                orbits += moon.numberOfChildOrbits()
            else:
                orbits += self.numberOfParentPlanets()
        printToLog("Plant {0} has child orbits: {1}".format(self.name, orbits))
        return orbits

    def planetData(self):
        return {'name': self.name, 'parent': self.parentName, 'moons': list(map(lambda x: x.name, self.moons))}

    def __str__(self):
        return str(self.name)


def getInputFromFile(filename):

    returnInput = []

    input = []
    r = open(filename, "r")
    for line in r:
        x, y = line.rstrip().split(")")
        input.append({'name': y, 'parent': x})

    # Now let's find the COM (Only Planet listed as a Parent, not a Child)
    uniqueParents = set(list(map(itemgetter('parent'), input)))
    uniquePlanets = set(list(map(itemgetter('name'), input)))
    COMName = list(uniqueParents.difference(uniquePlanets))[0]

    return input, COMName


def getTotalOrbits(planetArray):
    orbits = 0
    for planet in planetArray:
        orbits += planet.numberOfChildOrbits()
    return orbits


def printPlanets(planetArray):
    for planet in planetArray:
        printToLog("Planet Name: {0:^3}\tParent Planet: {1} with # of Ancestors: {2}".format(
            planet.name, planet.parentName, planet.numberOfParentPlanets()))
        for moon in planet.moons:
            printToLog("\tMoon: {0}".format(str(moon)))
    return


def createPlanetsFromParent(planetInput, parentPlanet):
    # printToLog("Entering Creating Planets from Parent Planet: {0}".format(parentPlanet))
    returnInput = []

    # Now lets create a list with all the planets in an order from COM outward
    childPlanets = list(filter(lambda x: x['parent'] == parentPlanet.name, planetInput))
    if len(childPlanets) == 0:
        return []
    else:
        for planet in childPlanets:
            newPlanet = Planet(planet['name'], parentPlanet)
            returnInput.append(newPlanet)
            returnInput += createPlanetsFromParent(planetInput, newPlanet)

    return returnInput


def totalNumberOfOrbits(planetArray):
    orbits = 0
    for planet in planetArray:
        orbits += planet.numberOfParentPlanets()
    return orbits


def totalNumberOfTransfers(startPlanet, endPlanet):

    def findCommonPlanet(startPlanet, endPlanet):

        def returnListOfParentPlanet(planet):

            planets = []
            # printToLog("Checking for Parents of {0}".format(planet.name))
            if planet.parent == None:
                printToLog("**** FOUND THE EDGE OF THE UNIVERSE ****")
                return [planet]
            else:
                planets.append(planet)
                planets = planets + returnListOfParentPlanet(planet.parent)
                return planets

        # Find intersecting Planets
        # printToLog(str(startPlanet) + str(endPlanet))
        startPlanetParents = returnListOfParentPlanet(startPlanet.parent)
        endPlanetParents = returnListOfParentPlanet(endPlanet.parent)
        # printToLog(list(map(lambda x: str(x), startPlanetParents)))
        # printToLog(list(map(lambda x: str(x), endPlanetParents)))
        commonParents = list(set(startPlanetParents).intersection(set(endPlanetParents)))
        # printToLog(list(map(lambda x: str(x), commonParents)))

        # Now find the closest planet to both startPlanet
        # By default, this will also be the closest distance to endPlanet

        closestPlanet = commonParents.pop(0)
        closestDistance = transfersBetweenPlanets(startPlanet, closestPlanet)
        for planet in commonParents:
            checkDistance = transfersBetweenPlanets(startPlanet, planet)
            if checkDistance < closestDistance:
                closestPlanet = planet
                closestDistance = checkDistance

        return closestPlanet

    def transfersBetweenPlanets(startPlanet, endPlanet):

        if startPlanet == endPlanet:
            return 0
        else:
            return 1 + transfersBetweenPlanets(startPlanet.parent, endPlanet)

    commonPlanet = findCommonPlanet(startPlanet, endPlanet)
    printToLog("Found Common Planet: {0}".format(commonPlanet.name))
    transfer1 = transfersBetweenPlanets(startPlanet, commonPlanet)
    printToLog("\tTransfers Between Planet {0} and {1} is: {2}".format(startPlanet.name, commonPlanet.name, transfer1))
    transfer2 = transfersBetweenPlanets(endPlanet, commonPlanet)
    printToLog("\tTransfers Between Planet {0} and {1} is: {2}".format(endPlanet.name, commonPlanet.name, transfer2))

    return transfer1 + transfer2


def main():
    planets, COMName = getInputFromFile(planetInput)

    # Create the Center of Mass
    planetArray = [Planet(COMName, None)]
    planetArray += createPlanetsFromParent(planets, planetArray[0])

    orbits = 0
    # printPlanets(planetArray)
    print("Total number of orbits: {0}".format(totalNumberOfOrbits(planetArray)))

    myPlanet = list(filter(lambda x: x.name == startName, planetArray))[0]
    santaPlanet = list(filter(lambda x: x.name == endName, planetArray))[0]

    print("Total number of Transfers from {0} to {1} is {2}".format(
        myPlanet.name, santaPlanet.name, totalNumberOfTransfers(myPlanet.parent, santaPlanet.parent)))


if __name__ == "__main__":
    main()
