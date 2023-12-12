from datetime import datetime
import numpy as np

# inputSignal = "12345678"
# inputSignal = "80871224585914546619083218645595"
inputSignal = "03036732577212944063491565474664"
# inputSignal = "59712692690937920492680390886862131901538154314496197364022235676243731306353384700179627460533651346711155314756853419495734284609894966089975988246871687322567664499495407183657735571812115059436153203283165299263503632551949744441033411147947509168375383038493461562836199103303184064429083384309509676574941283043596285161244885454471652448757914444304449337194545948341288172476145567753415508006250059581738670546703862905469451368454757707996318377494042589908611965335468490525108524655606907405249860972187568380476703577532080056382150009356406585677577958020969940093556279280232948278128818920216728406595068868046480073694516140765535007"
basePattern = [0, 1, 0, -1]
noOfPhases = 100


def parseInputSignal(inputValue):
    inputList = [int(i) for i in inputValue]
    inputListNp = np.array(inputList)
    return inputList


def generatePattern(basePattern, length):
    startTime = datetime.now()
    returnPattern = np.zeros((length, length), dtype=np.int8)
    for level in range(1, length + 1):

        x = 0
        repeat = length // level + 1
        levelPattern = []
        for _ in range(repeat):
            levelPattern += [basePattern[x]] * level
            x += 1
            if x >= len(basePattern):
                x = 0

        returnPattern[level - 1] = levelPattern[1 : length + 1]
        # print(f"Generating Level: {level} of base pattern")
    endTime = datetime.now() - startTime
    print(f"Total time generating pattern array: {endTime}")
    return returnPattern


def printArrayAsValue(array):
    value = ""
    lengthOfArray = len(array)
    for i in array:
        value = value + str(i)
    return value


def Part1Alternate(inputArray):
    funcStartTime = datetime.now()
    baseArray = generatePattern(basePattern, len(inputArray))
    for x in range(noOfPhases):

        # startTime = datetime.now()
        newArray = list()
        fullArray = [inputArray] * len(inputArray)
        multiple = np.multiply(fullArray, baseArray)

        # endTime = datetime.now() - startTime
        newArray = np.sum(multiple, axis=1)
        inputArray = [abs(x) % 10 for x in newArray]
        # endTime = datetime.now() - startTime
        # print(f"Phase {x}, Total time: {endTime}")

    funcEndTime = datetime.now() - funcStartTime
    print(f"Part 1 function time: {funcEndTime}")
    return printArrayAsValue(inputArray)[:8]


def Part2(inputArray):
    offset = int(inputSignal[0:7])
    print(offset)
    inputArray = inputArray * 1000
    baseArray = generatePattern(basePattern, len(inputArray))
    for x in range(noOfPhases):
        startTime = datetime.now()
        newArray = list()
        fullArray = [inputArray] * len(inputArray)
        multiple = np.multiply(fullArray, baseArray)
        endTime = datetime.now() - startTime
        print(f"Phase {x}, Multiple time: {endTime}")

        newArray = np.sum(multiple, axis=1)
        inputArray = [abs(x) % 10 for x in newArray]

        endTime = datetime.now() - startTime
        print(f"Phase {x}, time: {endTime}")

    return printArrayAsValue(inputArray)[offset:8]


def main():
    inputArray = parseInputSignal(inputSignal)
    result1 = Part1Alternate(inputArray)
    print(f"Part 1 Result: {result1}")
    # result2 = Part2(inputArray)
    # print(f"Part 2 Result: {result2}")


if __name__ == "__main__":
    main()
