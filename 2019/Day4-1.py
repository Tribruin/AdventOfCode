#!/usr/bin/python3

lowerRange = 158126
upperRange = 624574


class combo():

    def __init__(self, x):

        self.strNumber = str(x).zfill(6)
        self.num = x
        self.hasDuplicate = self.checkForDuplicate()
        self.isIncreasing = self.checkForIncrease()

    def __str__(self):
        return self.strNumber

    def checkForDuplicate(self):
        i = 0
        duplicate = False
        for i in range(len(self.strNumber)-1):
            # 			print("Checking {0}{1}".format(self.strNumber[i], self.strNumber[i+1]))
            if self.strNumber[i] == self.strNumber[i+1]:
                duplicate = True
                break
        return duplicate

    def checkForIncrease(self):
        i = 0
        increasing = True
        for i in range(len(self.strNumber)-1):
            # 			print("Checking {0}{1}".format(self.strNumber[i], self.strNumber[i+1]))
            if (int(self.strNumber[i]) > int(self.strNumber[i+1])):
                increasing = False
                break
        return increasing


def checkRangeOfNumbers(startNumber, endNumber):
    goodNumbers = []
    for i in range(startNumber, endNumber + 1):
        checkNum = combo(i)
        if checkNum.hasDuplicate and checkNum.isIncreasing:
            goodNumbers.append(i)

    return goodNumbers


def main():
    goodNums = checkRangeOfNumbers(lowerRange, upperRange)
    print("{0} Good Combinations found in Range {1} - {2}".format(len(goodNums), lowerRange, upperRange))


if __name__ == "__main__":
    main()
