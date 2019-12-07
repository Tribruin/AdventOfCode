#!/usr/local/bin/python3

# log = True
log = False

validInstructions = [1,2,3,4,99]


#Test Input
# projectInput = "1002,4,3,4,33"
# projectInput = "3,0,4,0,99"
# projectInput = "00001,2,3,0,4,0,99"
# projectInput = "1002,6,3,6,4,6,33"

# Real Input
projectInput = "3,225,1,225,6,6,1100,1,238,225,104,0,1101,32,43,225,101,68,192,224,1001,224,-160,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1001,118,77,224,1001,224,-87,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,1102,5,19,225,1102,74,50,224,101,-3700,224,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1102,89,18,225,1002,14,72,224,1001,224,-3096,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1101,34,53,225,1102,54,10,225,1,113,61,224,101,-39,224,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1101,31,61,224,101,-92,224,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1102,75,18,225,102,48,87,224,101,-4272,224,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1101,23,92,225,2,165,218,224,101,-3675,224,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1102,8,49,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,226,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,1007,677,226,224,1002,223,2,223,1006,224,344,1001,223,1,223,108,677,226,224,102,2,223,223,1006,224,359,1001,223,1,223,7,226,226,224,1002,223,2,223,1005,224,374,101,1,223,223,107,677,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,419,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,434,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,449,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,464,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,479,1001,223,1,223,1008,226,226,224,102,2,223,223,1005,224,494,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,509,101,1,223,223,8,226,677,224,1002,223,2,223,1006,224,524,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,539,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,554,101,1,223,223,1108,677,677,224,102,2,223,223,1006,224,569,101,1,223,223,1107,226,677,224,102,2,223,223,1005,224,584,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,599,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,614,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,629,101,1,223,223,107,226,677,224,102,2,223,223,1005,224,644,101,1,223,223,8,677,677,224,102,2,223,223,1005,224,659,1001,223,1,223,108,677,677,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226"


def printToLog(out):
	if log:
		print(out)
	return


class IntcodeComputer:
	
	def __init__ (self, program):
		""" Establish execution program """
	
		self.programCode = program.split(",")
		self.currentIndex = 0
		
	def updateLocation(self, location, value):
		self.programCode[location] = str(value)
		return
		
	def getParameters(self, number, mask):
		""" Get the parameters based on 'number' """
		strParameters = self.programCode[self.currentIndex+1 : self.currentIndex + number + 1]
		parameters = list(map(lambda x : int(x), strParameters))
		parms = self.evaluateParms(parameters, mask)
		printToLog("\t\tReturn Parameters: {0}".format(parms))
		return parms
		
	def evaluateParms(self, parms, mask):
		""" Evaluate Parms base on Mask and return real Parameter Values """
		
		printToLog("\t\tPassed Parameters: {0}".format(parms))
		returnParms=[]
		for i in range(len(parms)-1):
			maskCode = mask[0]
			parmValue = parms[i]
			if maskCode == '0':
				printToLog("\t\tGetting Position Value {0} from Position {1}".format(self.programCode[parmValue], parmValue))
				returnParms.append(int(self.programCode[parmValue]))
			elif maskCode == '1':
				printToLog("\t\tGetting Immediate Value {0} ".format(parmValue))
				returnParms.append(parmValue)
			else:
				print("*** ILLEGAL MASK {0} ***".format(mask))
				exit()
			mask = mask[1:]
			
		
# 		Append Location store
		maskCode = mask[0]
		returnParms.append(int(parms[-1]))
 			
		return returnParms
				
		
	def getInstruction(self):
		""" Get the next instruction code"""
		nextInstruction = self.programCode[self.currentIndex].zfill(5)
		printToLog("Received Instruction Code {1} from Position {0}".format(self.currentIndex, nextInstruction))
		mask = nextInstruction[0:3][::-1]
		instruction = int(nextInstruction[3:5])
		return instruction, mask
		
	def returnCode(self, location):
		return int(self.programCode[location])
		
	def execCode(self):
		""" Execute Code """
	
		while True:
		
			printToLog("--------------------------------------------------")
			instruction, mask = self.getInstruction()		
			printToLog("\tExecuting Code: {0} with Mask: {1}".format(instruction, mask))
	
			if instruction not in validInstructions:
				print("** Illegal Instruction Code: {0}".format(instruction))
				exit()
		
			if instruction == 1:
				parms = self.getParameters(3, mask)
				outputLocation = parms[2]
				x, y = parms[0], parms[1]
				a = x + y
				self.updateLocation(outputLocation, a)
				printToLog("\tExecute {0} + {1} with result: {2} and stored in Position: {3}".format(x,y, a, outputLocation))
				self.currentIndex += 4

			
			elif instruction == 2:
				parms = self.getParameters(3, mask)
				outputLocation = parms[2]
				x, y = parms[0], parms[1]
				a = x * y
				self.updateLocation(outputLocation, a)
				printToLog("\tExecute {0} * {1} with result: {2} and stored in Position: {3}".format(x,y, a, outputLocation))
				self.currentIndex += 4
				
			elif instruction == 3:
				parms = self.getParameters(1, mask)
				outputLocation = parms[0]
				x = input("Enter Code: ")
				self.updateLocation(outputLocation,x)
				printToLog("\tReceived Input {0} and stored in Position: {1}".format(x,outputLocation))
				self.currentIndex += 2
			
			elif instruction == 4:
				parms = self.getParameters(1, mask)
				if mask[0] == '0':
					inputLocation = parms[0]
					x = self.returnCode(inputLocation)
				else:
					x = int(parms[0])
					inputLocation = "N/A"
				print("!!! Execution Code: {0}".format(x))
				printToLog("\tPrinted value: {0} from Position: {1}".format(x, inputLocation))
				self.currentIndex += 2
			
			else:
				# Executing Code 99
				break
			
		return

def main():
	
	# part 1
	computer=IntcodeComputer(projectInput)
	computer.execCode()
	
			
if __name__ == "__main__":
	main()

			
