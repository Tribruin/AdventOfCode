#!/usr/local/bin/python3
from operator import itemgetter

log = False

# Test Data

# planetInput = "Day6-Test2.txt"

# Actual Data
planetInput = "Day6-Input-Final.txt"


def printToLog(out):
    if log:
        print(out)
    return
<<<<<<< HEAD
    
=======

>>>>>>> 251a61f74f1630411df76de9302c83e3ca677b4e

class Planet:

    def __init__(self, objectName, parentObject):
        self.name = objectName
        self.moons = []
        self.parentObject = parentObject
<<<<<<< HEAD
        try: 
=======
        try:
>>>>>>> 251a61f74f1630411df76de9302c83e3ca677b4e
            self.parentName = parentObject.name
        except:
            self.parentName = "None"
        self.planetData = self.planetData()
        if self.parentObject != None:
            parentObject.addOrbit(self)
        return
<<<<<<< HEAD
        
=======

>>>>>>> 251a61f74f1630411df76de9302c83e3ca677b4e
    def numberOfParentPlanets(self):
        parentOrbits = 0
        if self.parentObject == None:
            parentPlanets = 0
        else:
            parentPlanets = 1 + self.parentObject.numberOfParentPlanets()
        return parentPlanets
<<<<<<< HEAD
            
    
    def addOrbit(self, moon):
        self.moons.append(moon)
        return
        
=======

    def addOrbit(self, moon):
        self.moons.append(moon)
        return

>>>>>>> 251a61f74f1630411df76de9302c83e3ca677b4e
    def numberOfChildOrbits(self):
        printToLog("Checking orbits for Planet {0} with Number of moons: {1}".format(self.name, len(self.moons)))
        orbits = 0
        if len(self.moons) != 0:
            for moon in self.moons:
                orbits += moon.numberOfChildOrbits()
            else:
<<<<<<< HEAD
                orbits += self.numberOfParentPlanets()	
        printToLog("Plant {0} has child orbits: {1}".format(self.name, orbits))
        return orbits
            

    def planetData(self):
        return {'name' : self.name, 'parent' : self.parentName , 'moons' : list(map(lambda x : x.name, self.moons))}
    
=======
                orbits += self.numberOfParentPlanets()
        printToLog("Plant {0} has child orbits: {1}".format(self.name, orbits))
        return orbits

    def planetData(self):
        return {'name': self.name, 'parent': self.parentName, 'moons': list(map(lambda x: x.name, self.moons))}

>>>>>>> 251a61f74f1630411df76de9302c83e3ca677b4e
    def __str__(self):
        return str(self.name)


def getInputFromFile(filename):

<<<<<<< HEAD
    returnInput  = []
    
    input = []
    r = open(filename,"r")
    for line in r:
        x, y = line.rstrip().split(")")
        input.append({'name' : y, 'parent' : x})
        

    # Now let's find the COM (Only Planet listed as a Parent, not a Child)
    uniqueParents = set(list(map(itemgetter('parent'), input)))
    uniquePlanets = set(list(map(itemgetter('name'), input)))
    COMName = list(uniqueParents.difference(uniquePlanets))[0]

=======
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

>>>>>>> 251a61f74f1630411df76de9302c83e3ca677b4e
    return input, COMName


def getTotalOrbits(planetArray):
    orbits = 0
    for planet in planetArray:
        orbits += planet.numberOfChildOrbits()
    return orbits
<<<<<<< HEAD
    
=======

>>>>>>> 251a61f74f1630411df76de9302c83e3ca677b4e

def printPlanets(planetArray):
    for planet in planetArray:
        printToLog("Planet Name: {0:^3}\tParent Planet: {1} with # of Ancestors: {2}".format(planet.name, planet.parentName, planet.numberOfParentPlanets()))
        for moon in planet.moons:
            printToLog("\tMoon: {0}".format(str(moon)))
    return

<<<<<<< HEAD
def createPlanetsFromParent(planetInput, parentPlanet):	
    printToLog("Entering Creating Planets from Parent Planet: {0}".format(parentPlanet))
    returnInput = []
    
    # Now lets create a list with all the planets in an order from COM outward
    childPlanets = list(filter(lambda x : x['parent'] == parentPlanet.name, planetInput))
=======

def createPlanetsFromParent(planetInput, parentPlanet):
    printToLog("Entering Creating Planets from Parent Planet: {0}".format(parentPlanet))
    returnInput = []

    # Now lets create a list with all the planets in an order from COM outward
    childPlanets = list(filter(lambda x: x['parent'] == parentPlanet.name, planetInput))
>>>>>>> 251a61f74f1630411df76de9302c83e3ca677b4e
    if len(childPlanets) == 0:
        return []
    else:
        for planet in childPlanets:
            newPlanet = Planet(planet['name'], parentPlanet)
            returnInput.append(newPlanet)
            returnInput += createPlanetsFromParent(planetInput, newPlanet)

    return returnInput
<<<<<<< HEAD
    
=======


>>>>>>> 251a61f74f1630411df76de9302c83e3ca677b4e
def totalNumberOfOrbits(planetArray):
    orbits = 0
    for planet in planetArray:
        orbits += planet.numberOfParentPlanets()
    return orbits
<<<<<<< HEAD
    
def main():
    planets, COMName = getInputFromFile(planetInput)
    
    # Create the Center of Mass
    planetArray = [Planet(COMName, None)]
    planetArray += createPlanetsFromParent(planets, planetArray[0])
    
    
    orbits = 0
    printPlanets(planetArray)
    print("Total number of orbits: {0}".format(totalNumberOfOrbits(planetArray)))
        
        

if __name__ == "__main__":
    main()
    
    
=======


def main():
    planets, COMName = getInputFromFile(planetInput)

    # Create the Center of Mass
    planetArray = [Planet(COMName, None)]
    planetArray += createPlanetsFromParent(planets, planetArray[0])

    orbits = 0
    printPlanets(planetArray)
    print("Total number of orbits: {0}".format(totalNumberOfOrbits(planetArray)))


if __name__ == "__main__":
    main()
>>>>>>> 251a61f74f1630411df76de9302c83e3ca677b4e
