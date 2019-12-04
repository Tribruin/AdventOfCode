#!/usr/bin/python3

#Good Input String
#defaultInputString = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,6,27,1,9,27,31,1,31,10,35,2,13,35,39,1,39,10,43,1,43,9,47,1,47,13,51,1,51,13,55,2,55,6,59,1,59,5,63,2,10,63,67,1,67,9,71,1,71,13,75,1,6,75,79,1,10,79,83,2,9,83,87,1,87,5,91,2,91,9,95,1,6,95,99,1,99,5,103,2,103,10,107,1,107,6,111,2,9,111,115,2,9,115,119,2,13,119,123,1,123,9,127,1,5,127,131,1,131,2,135,1,135,6,0,99,2,0,14,0"

# Bad Input String
defaultInputString = "1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,6,27,1,9,27,31,1,31,10,35,2,13,35,39,1,39,10,43,1,43,9,47,1,47,13,51,1,51,13,55,2,55,6,59,1,59,5,63,2,10,63,67,1,67,9,71,1,71,13,75,1,6,75,79,1,10,79,83,2,9,83,87,1,87,5,91,2,91,9,95,1,6,95,99,1,99,5,103,2,103,10,107,1,107,6,111,2,9,111,115,2,9,115,119,2,13,119,123,1,123,9,127,1,5,127,131,1,131,2,135,1,135,6,0,99,2,0,14,0"

expectedResult = 19690720
def executeProgram(inputArray):

	def performFunction(operation, a, b):
	# 	print(a,b)
		if operation == 1:
			return a + b
		elif operation == 2:
			return a * b
		else:
			print("ERROR: Operand: {0}, A & B: {1}, {2}".format(operation, a, b))

	# Iterate through program

	position = 0 
	while (inputArray[position] != 99):
		opperand, aPos, bPos, resultPos = list(inputArray[position:position + 4])
		result = performFunction(opperand, inputArray[aPos], inputArray[bPos])
		inputArray[resultPos] = result
		position = position + 4

	return inputArray

def checkArray():
	noun = 0

	while noun < 100:

		verb = 0 
		while verb < 100:

			# Reset Input Array
			currentArray = list(map(lambda x : int(x), defaultInputString.split(",")))
			currentArray[1] = noun
			currentArray[2] = verb
			outputArray = executeProgram(currentArray)
			if int(outputArray[0]) == expectedResult:
				return noun, verb, outputArray
			
			verb += 1
	
		noun += 1

def main():
	
	resultNoun, resultVerb, outputArray = checkArray()
	print ("Noun: {0}, Verb: {1}, Result {2}, Answer: {3}".format(resultNoun, resultVerb, outputArray[0], 100*resultNoun + resultVerb))	


if __name__ == "__main__":
	main()

	
	
	
	