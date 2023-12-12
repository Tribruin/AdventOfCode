#!/usr/local/bin/python3

class Planet:
    def __init__(self, position, name):
        self.position = position
        self.velocity = [0,0,0]
        self.name = name
        return

    def changeVelocity(self, sisterPlant):
        for i in range(len(self.position)):
            if self.position[i] > sisterPlant.position[i]:
                self.velocity[i] -= 1
            elif self.position[i] < sisterPlant.position[i]:
                self.velocity[i] += 1
        return
    
    def updatePosition(self):
        self.position = [self.position[i] + self.velocity[i] for i in range(len(self.position))]

    def getEnergy(self):
        pot = 0
        kin = 0
        for i in self.position:
            pot += abs(i)
        for j in self.velocity:
            kin += abs(j)
        return pot*kin
                    # self.deltaVelocity = [0,0,0]

    def returnPosVel(self):
        return self.position, self.velocity

    def __str__(self):
        output = f"pos=<x= {self.position[0]:3}, y= {self.position[1]:3}, z= {self.position[2]:3}>, vel=<x= {self.velocity[0]:3}, y= {self.velocity[1]:3}, z= {self.velocity[2]:3}>"
        return output

def currentUniverse(planets):

    for planet in planets:
        currentState = []
        for planet in planets:
            currentState.append(planet.returnPosVel())
    return currentState
    
    
def main():

    # Test 1
    totalMoves = 10
    # P1 = Planet([-1, 0, 2], "P1")
    # P2 = Planet([2, -10, -7], "P2")
    # P3 = Planet([4, -8, 8], "P3")
    # P4 = Planet([3, 5, -1], "P4")

    # totalMoves = 100
    P1 = Planet([-8, -10, 0], "P1")
    P2 = Planet([5, 5, 10], "P2")
    P3 = Planet([2, -7, 3], "P3")
    P4 = Planet([9, -8, -3], "P4")

    # Real Input
    # totalMoves = 1000
    # P1 = Planet([-14, -4, -11], "P1")
    # P2 = Planet([-9, 6, -7], "P2")
    # P3 = Planet([4, 1, 4], "P3")
    # P4 = Planet([2, -14, -9], "P4")

    planets = [P1, P2, P3, P4]

    for planet in planets:
        print(planet)

    moves = 0
    history = []
    historyComplete = []
    foundDuplicate = False
    while not foundDuplicate:
        for planet in planets:
            for sisterPlanet in planets:
                if planet is not sisterPlanet:
                    planet.changeVelocity(sisterPlanet)
        for planet in planets:
            planet.updatePosition()

        totalEnergy = 0
        for planet in planets:
            totalEnergy += planet.getEnergy()
       
        if totalEnergy in history:
            # print(f"Checking for matches of energy: {totalEnergy} at move: {moves}")
            idx = history.index(totalEnergy)
            if currentUniverse(planets) == historyComplete[idx]:
                foundDuplicate = True
                foundEnergy = history.index(totalEnergy)
                # print(historyComplete)

        if not foundDuplicate:
            history.append(totalEnergy) 
            historyComplete.append(currentUniverse(planets))
            moves += 1
            if (moves % 10000 == 0):
                print(f"Checking on move: {moves}")
            if moves > 1000000000:
                print(f"I give up!")
                foundDuplicate = True

    print(f"Completed {moves} moves to find a duplicate position with enery: {totalEnergy} at index: {foundEnergy}")
    # print(history)

if __name__ == "__main__":
    main()