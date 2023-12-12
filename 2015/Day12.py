import json

filename = "/Users/rblount/OneDrive/AdventOfCode/2015/Day12-Input.txt"
# filename = "/Users/rblount/OneDrive/AdventOfCode/2015/Day12-Input-Test.txt"

def printJsonPretty(jsonValue):
    """ Print a JSON Object in a human readable format. For testing purposes. """
    print(json.dumps(jsonValue, sort_keys=True, indent=4, separators=(",", ":")))

def parseListPart1(inputData):
    totalCount = 0
    if type(inputData) == list:
        lenOfList = len(inputData)
        for i in range(lenOfList):
            totalCount += parseListPart1(inputData[i])
    elif type(inputData) == dict:
        values = list(inputData.values())
        totalCount += parseListPart1(values)
    elif type(inputData) == int:
        return inputData
    else:
        return 0
    
    return totalCount

def parseListPart2(inputData):
    totalCount = 0
    if type(inputData) == list:
        lenOfList = len(inputData)
        for i in range(lenOfList):
            totalCount += parseListPart2(inputData[i])
    elif type(inputData) == dict:
        values = list(inputData.values())
        if 'red' in values:
            return 0
        totalCount += parseListPart2(values)
    elif type(inputData) == int:
        return inputData
    else:
        return 0
    
    return totalCount


f = open(filename)
inputData = f.read()
data = json.loads(inputData)
print(parseListPart1(data))
print(parseListPart2(data))


