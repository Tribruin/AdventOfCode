import math

def angleToAsteroid(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        if y2 > y1:
            return 270
        else:
            return 90
    s1 = (y2-y1)/(x2-x1)                                                 # Slope of a horizontal line
    # angle = math.degrees(math.atan(s1))
    angle = math.atan(s1)
    # if x2 < x1:
    #     angle -= 180
    # if angle < 0:
    #     angle += 360
    return angle


centerPoint = (10,10)
points = [ (20,10), (20,15), (20,20), (15,20), (10,20), (5,20), (0,20), (0,15), (0,10), (0,5), (0,0), (0,0), (5,0), (10,0), (15,0), (20,0), (20,5) ]

for x,y in points:
    angle1 = angleToAsteroid(centerPoint, (x,y))
    angleDegrees = math.degrees(angle1)
    pSin = round(math.sin(angle1), 3)
    pCos = round(math.cos(angle1), 3)
    print(f"From (10,10) to {x,y} = {angleDegrees} with Sin: {pSin} and Cos: {pCos}")
