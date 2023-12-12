#!/usr/bin/python3
import time


lowerRange = 158126
upperRange = 624574
# testGroup = [111111, 223450, 123789, 113333, 111122, 123444, 111122, 111222]
# testGroup = [113333]


class combo(): 

	def __init__(self, x):
	
		self.strNumber = str(x).zfill(6)
		self.num = x
		self.isIncreasing  = self.checkForIncrease()
		self.hasDuplicate = self.checkForDuplicate()
		
	def __str__(self):
		return self.strNumber
		
	def output(self):
		returnString = "Num: {0} Inc: {1} Dup: {2}".format(self.strNumber, self.isIncreasing, self.hasDuplicate)
		return returnString
		
	def checkForDuplicate(self):
		i = 0
		duplicate = False
		if not self.isIncreasing:
		# Let's not check the non increasing numbers
			return duplicate
			
		for i in range(len(self.strNumber)-1):
# 			print("Found {0} of {1} in {2}".format(self.strNumber.count(self.strNumber[i]), self.strNumber[i], self.strNumber))
			if self.strNumber[i] == self.strNumber[i+1]:
				if self.strNumber.count(self.strNumber[i]) > 2:
					duplicate = False
				else:
					duplicate = True
					break
		return duplicate
		
	def checkForIncrease(self):
		i = 0 
		increasing = True
		for i in range(len(self.strNumber)-1):
			if (int(self.strNumber[i]) > int(self.strNumber[i+1])):
				increasing = False
				break
		return increasing
		
def checkRangeOfNumbers(startNumber, endNumber):
	goodNumbers = []
	for i in range(startNumber, endNumber + 1):
		checkNum = combo(i)
		if checkNum.hasDuplicate:
			goodNumbers.append(i)
	
	return goodNumbers

def main():

# 	for test in testGroup:
# 		print(combo(test).output())

	goodNums = checkRangeOfNumbers(lowerRange, upperRange)
	print ("{0} Good Combinations found in Range {1} - {2}".format(len(goodNums), lowerRange, upperRange))


if __name__ == "__main__":
	main()
