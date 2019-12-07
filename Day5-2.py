#!/usr/bin/python3

test = True
# test = False

# TEST INPUT STRINGS ###
# inputString = "3,9,8,9,10,9,4,9,99,-1,8"
# inputString = "3,9,7,9,10,9,4,9,99,-1,8"
# inputString = "3,3,1108,-1,8,3,4,3,99"
# inputString = "3,3,1107,-1,8,3,4,3,99"
inputString = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"
# inputString = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"


# Actual Input String
# inputString = "3,225,1,225,6,6,1100,1,238,225,104,0,1101,32,43,225,101,68,192,224,1001,224,-160,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1001,118,77,224,1001,224,-87,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,1102,5,19,225,1102,74,50,224,101,-3700,224,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1102,89,18,225,1002,14,72,224,1001,224,-3096,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1101,34,53,225,1102,54,10,225,1,113,61,224,101,-39,224,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1101,31,61,224,101,-92,224,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1102,75,18,225,102,48,87,224,101,-4272,224,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1101,23,92,225,2,165,218,224,101,-3675,224,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1102,8,49,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,226,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,1007,677,226,224,1002,223,2,223,1006,224,344,1001,223,1,223,108,677,226,224,102,2,223,223,1006,224,359,1001,223,1,223,7,226,226,224,1002,223,2,223,1005,224,374,101,1,223,223,107,677,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,419,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,434,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,449,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,464,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,479,1001,223,1,223,1008,226,226,224,102,2,223,223,1005,224,494,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,509,101,1,223,223,8,226,677,224,1002,223,2,223,1006,224,524,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,539,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,554,101,1,223,223,1108,677,677,224,102,2,223,223,1006,224,569,101,1,223,223,1107,226,677,224,102,2,223,223,1005,224,584,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,599,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,614,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,629,101,1,223,223,107,226,677,224,102,2,223,223,1005,224,644,101,1,223,223,8,677,677,224,102,2,223,223,1005,224,659,1001,223,1,223,108,677,677,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226"

inputArray =  inputString.split(",")
validInstructions = [1, 2, 3, 4, 5, 6, 7, 8, 99]

def printToLog(out):
	if test:
		print(out)
	return
	

def executeProgram():

	def performFunction(op, a=0, b=0, c=0, d=0):
		if (op == 1 ):
			inputArray[c] = str(a + b)
			printToLog("Stored: {0} in Position {1}".format(a+b, c))
			return 4

		elif (op == 2):
			inputArray[c] = str(a * b)
			printToLog("Stored: {0} in Position {1}".format(a*b, c))
			return 4

		elif (op == 3):
			val = input("Enter Value: ")
			inputArray[a] = val
			printToLog("Stored: {0} in Position {1}".format(val, a))
			return 2

		elif (op == 4):
			print("*** OUTPUT: {0} ***".format(a))
			printToLog("Printed {0}".format(a))
			return 2

		elif (op == 5):
			if ( a != 0 ):
				printToLog("Value {0} is TRUE, setting next instruction to {1}".format(a, b))
				return (b - c)
			else:
				printToLog("Value {0} is FALSE, setting next instruction to {1}".format(a, c + 3))
				return 3

		elif (op == 6):
			if ( a == 0 ):
				printToLog("Value {0} is FALSE, setting next instruction to {1}".format(a, b))
				return (b - c)
			else:
				printToLog("Value {0} is TRUE, setting next instruction to {1}".format(a, c + 3))
				return 3

		elif (op == 7):
			if ( a < b ):
				inputArray[c] = 1
			else:
				inputArray[c] = 0				
			printToLog("Stored: {0} in Position {1}".format( 1 * (a < b), c))
			return 4

		elif (op == 8):
			if ( a == b ):
				inputArray[c] = 1
			else:
				inputArray[c] = 0
			printToLog("Stored: {0} in Position {1}".format( 1 * (a == b), c))
			return 4
				
		else:
			pass
		return
		
	def computeParameters(mask, parameterArray):

		returnArray = []
		parameterArray = list(map(lambda x : int(x), parameterArray))
		printToLog("Input Mask: {0} Parameters {1}".format(mask, parameterArray))
		for i in range(len(parameterArray)-1):
			if mask[i] == '0':
				printToLog("\tGetting Array Value")
				x = int(inputArray[parameterArray[i]])
				printToLog("\t\tArray Position: {0} is {1}".format(parameterArray[i], x))
			elif mask[i] == '1':
				printToLog("\tGetting Parameter Value")
				x = int(parameterArray[i])
				printToLog("\t\tParameter Value is {0}".format(x))
			returnArray.append(x)
		returnArray.append(int(parameterArray[-1]))
		printToLog("\tExecutionArray: {0}".format(returnArray))
		return returnArray
			
	opCounter = 0
	while opCounter <= len(inputArray):
		instruction = inputArray[opCounter].zfill(5)
		operand = int(instruction[3:5])
		mask = instruction[0:3][::-1]
		printToLog("Current Position: {0}\tExecution Code: {1}".format(opCounter, instruction))

		if operand not in validInstructions:
			print("*** Illegal Instruction ({0}) ***".format(operand))
			exit()

		if operand in [1, 2, 7, 8]:
			a, b, c = computeParameters(mask, inputArray[opCounter + 1 : opCounter + 4])
			printToLog("Performing Function {0} with Parameters ({1}, {2}) and Output Position {3}".format(operand, a, b, c))
			returnVal = performFunction(operand, a, b, c)
			
		elif operand in [3]:
			a = computeParameters(mask, inputArray[opCounter + 1: opCounter + 2])[0]
			printToLog("Performing Function {0} with Position {1}".format(operand, a))
			returnVal = performFunction(operand,a)
			
		elif operand in [4]:
			a = computeParameters(mask, inputArray[opCounter + 1: opCounter + 2])[0]
			if mask[0] == '0':
				a = inputArray[a]
			printToLog("Performing Function {0} with Position {1}".format(operand, a))
			returnVal = performFunction(operand,a)
			
		elif operand in [5, 6]:
			a, b = computeParameters(mask, inputArray[opCounter + 1: opCounter + 3])
			printToLog("Performing Function {0} with Parameter ({1}) Position {2}".format(operand, a, b))
			returnVal = performFunction(operand, a, b, opCounter)
		
		elif operand in [99]:
			printToLog("Ending Program")
			opCounter = len(inputArray) + 1
		else:
		  pass

		printToLog("----------------------------------------")	
		opCounter += returnVal
		
	return 


def main():
	
	executeProgram()

if __name__ == "__main__":
	main()

	
	
	
	