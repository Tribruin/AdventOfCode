from datetime import datetime

# puzzleInput = "1"
puzzleInput = "1113222113"

cycles = 50

def createInitialArray(numberInput):
    array = []
    for letter in numberInput:
        array.append(int(letter))
    return array

def findDuplicates(stringToCheck):
    firstChar = stringToCheck[0]
    count = 1
    # stringToCheck.pop()
    lengthToCheck = len(stringToCheck)
    sameaChar = True
    i = 0
    while i < lengthToCheck-1  and sameaChar:
        if firstChar == stringToCheck[i+1]:
            count += 1
            i += 1
        else:
            sameaChar = False
    
    return count
    


def lookAndSay(numberArray):
    returnArray = []
    # numberArrayLen = len(numberArray)
    while len(numberArray) > 0:
    # while i < numberArrayLen:
        countDup = findDuplicates(numberArray)
        returnArray.append(countDup)
        returnArray.append(numberArray[0])
        # i += countDup
        numberArray = numberArray[countDup:]
    return returnArray

def part1():
    numberArray = createInitialArray(puzzleInput)
    print(numberArray)
    for i in range(cycles):
        startTime = datetime.now()
        numberArray = lookAndSay(numberArray)
        endTime = datetime.now()
        print(i, len(numberArray), endTime - startTime)


part1()
