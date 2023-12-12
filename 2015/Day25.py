import numpy as np

startingNumber = 20151125
multBy = 252533
dividBy = 33554393

# using a 0 based array, where puzzle is 1 based
finalColumn = 3029
finalRow = 2947

if finalColumn > finalRow:
    arraySize = finalColumn * 2 + 1
else:
    arraySize = finalRow * 2 + 1

# array=np.zeros((arraySize, arraySize ), dtype=int)

# array[0][0] = startingNumber
currentNumber = startingNumber
previousRow = 1
previousColumn = 1

for row in range(2, arraySize):
    for currentRow in range(row, 0, -1):

        currentColumn = row - currentRow + 1
        # array[currentRow][currentColumn] = (array[previousRow][previousColumn] * multBy) % dividBy
        currentNumber = (currentNumber * multBy) % dividBy
        # print(f"({currentRow}, {currentColumn}) = {currentNumber}")
        # previousColumn, previousRow = currentColumn, currentRow
        if (currentColumn == finalColumn) and (currentRow == finalRow):
            print(finalRow, finalColumn, currentNumber)
            exit(0)
