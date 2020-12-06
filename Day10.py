import numpy as np
import math

rows = 0
columns = 0


def angleToAsteroid(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        if y2 > y1:
            return 90
        else:
            return 270
    s1 = (y2 - y1) / (x2 - x1)  # Slope of a horizontal line
    angle = math.degrees(math.atan(s1))
    if x2 < x1:
        angle -= 180
    if angle < 0:
        angle += 360
    return round(angle, 3)


class AsteroidField:
    def __init__(self, inputFile):

        f = open(inputFile)
        lines = f.readlines()
        self.columns = len(lines[0]) - 1
        self.rows = len(lines)
        self.asteriodField = np.zeros((self.rows, self.columns), dtype=bool)
        for y in range(self.rows):
            for x in range(self.columns):
                if lines[y][x] == "#":
                    self.asteriodField[y][x] = True

        return

    def checkViews(self, x0, y0):
        # print(f"Checking for views at {x0}, {y0}")
        views = 0

        # First cycle through asteroids and find the angle between the two lines
        for y1 in range(self.rows):
            for x1 in range(self.columns):
                if self.asteriodField[y1][x1] and not (x0 == x1 and y0 == y1):
                    viewAngle = angleToAsteroid((x0, y0), (x1, y1))
                    # print(f"From {x0,y0} to {x1,y1} is Angle: {viewAngle}")
                    if x0 > x1:
                        x2start, x2finish, xStep = x0, x1, -1
                    elif x0 == x1:
                        x2start, x2finish, xStep = x0, x1, 1
                    else:
                        x2start, x2finish, xStep = x0, x1, 1
                    if y0 > y1:
                        y2start, y2finish, yStep = y0, y1, -1
                    elif y0 == y1:
                        y2start, y2finish, yStep = y0, y1, 1
                    else:
                        y2start, y2finish, yStep = y0, y1, 1
                    # print(f"  Checking for Asteroids from {x2start,y2start} to {x2finish,y2finish} with steps {xStep, yStep}")
                    blockView = False
                    for y2 in range(y2start, y2finish + yStep, yStep):
                        for x2 in range(x2start, x2finish + xStep, xStep):
                            if (x2 == x0 and y2 == y0) or (x2 == x1 and y2 == y1):
                                pass
                            else:
                                # print(f"  Check for Asteroid at {x2, y2}", end="")
                                if self.asteriodField[y2][x2]:
                                    viewAngle2 = angleToAsteroid((x0, y0), (x2, y2))
                                    # print(f"  From {x0,y0} to {x2,y2} is Angle: {viewAngle2}")
                                    # print(f"  {viewAngle} versus {viewAngle2}")
                                    if viewAngle == viewAngle2:
                                        # print(f"**BLOCKED**")
                                        blockView = True
                                        break
                                else:
                                    pass
                                    # print(f"  No Asteroid found at {x2,y2}")
                    if not blockView:
                        views += 1

        return views


def findBestLocation(AF):
    bestViewableObjects = 0
    bestAsteroid = (0, 0)

    for y in range(AF.rows):
        for x in range(AF.columns):
            if AF.asteriodField[y][x]:
                viewableObjects = AF.checkViews(x, y)
                print(f"***Found: {viewableObjects} from {x,y}")
                if viewableObjects > bestViewableObjects:
                    bestViewableObjects = viewableObjects
                    bestAsteroid = (x, y)

    return bestAsteroid, bestViewableObjects


def main():

    A = AsteroidField("Day10-Input.txt")
    bestAsteroid, bestViewableObjects = findBestLocation(A)
    print(
        f"Found the best Asteroid at {bestAsteroid} with {bestViewableObjects} viewable objects"
    )


if __name__ == "__main__":
    main()
