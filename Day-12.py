#!/usr/local/bin/python3

class Planet:
    def __init__(self, position):
        self.x, self.y, self.z = position
        self.currentXVelocity = self.currentYVelocity = self.currentZVelocity = 0
        return

    def changeVelocity(self, velocityDelta):
        deltaX, deltaY, deltaZ = velocityDelta
        self.currentXVelocity += deltaX
        self.currentYVelocity += deltaY
        self.currentZVelocity += deltaZ
        return

    def __str__(self):
        output = "Position: {0}, Current Velocity: {1}".format((self.x, self.y, self.z), (self.currentXVelocity, self.currentYVelocity, self.currentZVelocity))
        return output
    
def main():
    x = Planet((1,1,1))
    print(x)
    x.changeVelocity((-1,1,10))
    print(x)

if __name__ == "__main__":
    main()