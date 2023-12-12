#!/usr/bin/python3
lowerRange = 158126
upperRange = 624574
testGroup = [111111, 223450, 123789, 113333, 111122, 123444, 111122, 111222]
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
		if self.isIncreasing:	
			return (len(list(filter(lambda x : self.strNumber.count(x) == 2, list(self.strNumber)))) > 1)
		else:
			return False
	
	def checkForIncrease(self):
		return ( list(self.strNumber) == sorted(self.strNumber))
		
def checkRangeOfNumbers(startNumber, endNumber):
	goodNumbers = list(filter(lambda x: combo(x).hasDuplicate, range(startNumber, endNumber)))
	
	return goodNumbers

def main():

# 	for test in testGroup:
# 		print(combo(test).output())

	goodNums = checkRangeOfNumbers(lowerRange, upperRange)
	print ("{0} Good Combinations found in Range {1} - {2}".format(len(goodNums), lowerRange, upperRange))


if __name__ == "__main__":
	main()
