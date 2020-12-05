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

    def __str__(self):
        output = f"pos=<x= {self.position[0]:3}, y= {self.position[1]:3}, z= {self.position[2]:3}>, vel=<x= {self.velocity[0]:3}, y= {self.velocity[1]:3}, z= {self.velocity[2]:3}>"
        return output
    
def main():

    totalMoves = 1000
    P1 = Planet([-14, -4, -11], "P1")
    P2 = Planet([-9, 6, -7], "P2")
    P3 = Planet([4, 1, 4], "P3")
    P4 = Planet([2, -14, -9], "P4")
    planets = [P1, P2, P3, P4]

    for planet in planets:
        print(planet)

    for moves in range(totalMoves):   
        for planet in planets:
            for sisterPlanet in planets:
                if planet is not sisterPlanet:
                    planet.changeVelocity(sisterPlanet)
        for planet in planets:
            planet.updatePosition()

        # if (moves+1) % 10 == 0:
        #     print(f"\nAfter {moves + 1} Steps")
        #     for planet in planets:
        #         print(planet)

    print(f"Completed {totalMoves}")
    for planet in planets:
        print(planet)

    totalEnergy = 0
    for planet in planets:
        totalEnergy += planet.getEnergy()

    print(f"Total Energy: {totalEnergy}")
    


if __name__ == "__main__":
    main()