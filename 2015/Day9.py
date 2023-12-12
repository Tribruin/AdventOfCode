import itertools

# inputFile = "/Users/rblount/OneDrive/AdventOfCode/2015/Day9-Input-Test.txt"
inputFile = "/Users/rblount/OneDrive/AdventOfCode/2015/Day9-Input.txt"

def readFile(fileName):
    f = open(fileName, "r")
    citys = []
    routes = dict()

    for line in f.readlines():
        route, distance = line.split(" = ")
        source, destination = route.split(" to ")
        # Add the route and the reverse route
        citys.append(source)
        citys.append(destination)
        
        # Add a route from source to destinstaion. 
        if source not in routes.keys():
            routes[source] = {destination: int(distance)}
        else:
            routes[source][destination] = int(distance)

        # Add Reverse Route
        if destination not in routes.keys():
            routes[destination] = {source: int(distance)}
        else:
            routes[destination][source] = int(distance)
    
    # Return a list of cities, removing duplicates. 
    citys = set(citys)

    return citys, routes

def getDistance(route, allRoutes):
    distance = 0
    i = 0
    for i in range(len(route) - 1):
        distance += allRoutes[route[i]][route[i+1]]
    return distance     

def part1():
    departureCities, routes = readFile(inputFile)
    possibleRoutes = itertools.permutations(departureCities)
    # print(possibleRoutes)

    shortestDistance = 9999999
    for route in possibleRoutes:
        distance = getDistance(list(route), routes)
        if distance < shortestDistance:
            shortestDistance = distance
            shortestRoute = route
    print(shortestRoute, shortestDistance)

def part2():
    departureCities, routes = readFile(inputFile)
    possibleRoutes = itertools.permutations(departureCities)
    # print(possibleRoutes)

    longestDistance = 0
    for route in possibleRoutes:
        distance = getDistance(list(route), routes)
        if distance > longestDistance:
            longestDistance = distance
            longestRoute = route
    print(longestRoute, longestDistance)

part1()
part2()
