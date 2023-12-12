#!/usr/local/bin/python3

import sys
from io import StringIO
from itertools import permutations

projectInput = "3,8,1001,8,10,8,105,1,0,0,21,46,59,84,93,110,191,272,353,434,99999,3,9,101,2,9,9,102,3,9,9,1001,9,5,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,102,5,9,9,4,9,99,3,9,1001,9,4,9,1002,9,2,9,101,2,9,9,102,2,9,9,1001,9,3,9,4,9,99,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,1001,9,5,9,1002,9,3,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99"
basePhaseSettings = ['0','1','2','3','4']

# Turn on logging (printed to STDERR)
logLevel = 0


validInstructions = [1,2,3,4,5,6,7,8,99]


def printToLog(level, out):
	if level <= logLevel :
		print(out, file = sys.stderr)
	return


class IntcodeComputer:
	
	def __init__ (self, program):
		""" Establish execution program """
	
		self.programCode = program.split(",")
		self.currentIndex = 0
		self.steps = 0
		self.inputValues = []
		self.outputValues = []
		self.manualInput = True
		self.manualOutput = True
		
	def updateLocation(self, location, value):
		self.programCode[location] = str(value)
		return
		
	def readFromFile(self, inputFileName):
		self.manualInput = False
		self.inFile = open(inputFileName, 'r')


	def getParameters(self, number, mask):
		""" Get the parameters based on 'number' """
		strParameters = self.programCode[self.currentIndex+1 : self.currentIndex + number + 1]
		parameters = list(map(lambda x : int(x), strParameters))
		parms = self.evaluateParms(parameters, mask)
		printToLog(1, "\t\tReturn Parameters: {0}".format(parms))
		return parms
		
	def evaluateParms(self, parms, mask):
		""" Evaluate Parms base on Mask and return real Parameter Values """
		
		printToLog(1, "\t\tPassed Parameters: {0}".format(parms))
		returnParms=[]
		for i in range(len(parms)-1):
			maskCode = mask[0]
			parmValue = parms[i]
			if maskCode == '0':
				printToLog(2, "\t\tGetting Position Value {0} from Position {1}".format(self.programCode[parmValue], parmValue))
				returnParms.append(int(self.programCode[parmValue]))
			elif maskCode == '1':
				printToLog(2, "\t\tGetting Immediate Value {0} ".format(parmValue))
				returnParms.append(parmValue)
			else:
				printToLog(0, "*** ILLEGAL MASK {0} ***".format(mask))
				exit()
			mask = mask[1:]
					
# 		Append Location store
		maskCode = mask[0]
		returnParms.append(int(parms[-1]))
 			
		return returnParms
				
		
	def getInstruction(self):
		""" Get the next instruction code"""
		nextInstruction = self.programCode[self.currentIndex].zfill(5)
		printToLog(1,"Received Instruction Code {1} from Position {0}".format(self.currentIndex, nextInstruction))
		mask = nextInstruction[0:3][::-1]
		instruction = int(nextInstruction[3:5])
		return instruction, mask
		
	def returnCode(self, location):
		return int(self.programCode[location])
		
	def execCode(self):
		""" Execute Code """
	
		while True:
		
			self.steps += 1
			printToLog(1,"--------------------------------------------------")
			printToLog(3, self.programCode)
			instruction, mask = self.getInstruction()		
			printToLog(2, "\tExecuting Code: {0} with Mask: {1}".format(instruction, mask))
	
			if instruction not in validInstructions:
				print(0, "** Illegal Instruction Code: {0} at Position: {1} and Step: {2}".format(instruction, self.currentIndex, self.steps))
				exit()
		
			if instruction == 1:
				parms = self.getParameters(3, mask)
				x, y, outputLocation = parms
				a = x + y
				self.updateLocation(outputLocation, a)
				printToLog(2, "\tExecute {0} + {1} with result: {2} and stored in Position: {3}".format(x,y, a, outputLocation))
				self.currentIndex += 4

			
			elif instruction == 2:
				parms = self.getParameters(3, mask)
				x, y, outputLocation = parms
				a = x * y
				self.updateLocation(outputLocation, a)
				printToLog(2, "\tExecute {0} * {1} with result: {2} and stored in Position: {3}".format(x,y, a, outputLocation))
				self.currentIndex += 4
				
			elif instruction == 3:
				parms = self.getParameters(1, mask)
				outputLocation = parms[-1]
				x = input()
				self.updateLocation(outputLocation,x)
				printToLog(2, "\tReceived Input {0} and stored in Position: {1}".format(x,outputLocation))
				self.currentIndex += 2
			
			elif instruction == 4:
				parms = self.getParameters(1, mask)
				if mask[0] == '0':
					inputLocation = parms[0]
					x = self.returnCode(inputLocation)
				else:
					x = int(parms[0])
					inputLocation = "N/A"
				print(x)
				printToLog(2, "\tPrinted value: {0} from Position: {1}".format(x, inputLocation))
				self.currentIndex += 2

			elif instruction == 5:
				parms = self.getParameters(2, mask)
				valueToCheck = parms[0]
				if mask[1] == '0':
					newLocation = self.programCode[parms[1]]
				else:
					newLocation = parms[1]
				if valueToCheck:
					self.currentIndex = int(newLocation)
				else: 
					newLocation = self.currentIndex + 3
				printToLog(2, "\tValue {0} is {1}, jumping to Position: {2}".format(valueToCheck, (valueToCheck != 0), newLocation))
				self.currentIndex = int(newLocation)
				
			elif instruction == 6:
				parms = self.getParameters(2, mask)
				valueToCheck = parms[0]
				if mask[1] == '0':
					newLocation = self.programCode[parms[1]]
				else:
					newLocation = parms[1]
				if not valueToCheck:
					self.currentIndex = newLocation
				else: 
					newLocation = self.currentIndex + 3
				printToLog(2, "\tValue {0} is {1}, jumping to Position: {2}".format(valueToCheck, not (valueToCheck != 0), newLocation))
				self.currentIndex = int(newLocation)

			elif instruction == 7:
				parms = self.getParameters(3, mask)
				valueToCheck1, valueToCheck2, outputLocation = parms
				result = (valueToCheck1 < valueToCheck2)
				self.updateLocation(outputLocation, int(result))
				printToLog(2, "\tValue {0} > {1} is {2}, storing {3} in Position: {2}".format(valueToCheck1, valueToCheck2, result, int(result)))
				self.currentIndex += 4
			
			elif instruction == 8:
				parms = self.getParameters(3, mask)
				valueToCheck1, valueToCheck2, outputLocation = parms
				result = (valueToCheck1 == valueToCheck2)
				self.updateLocation(outputLocation, int(result))
				printToLog(2, "\tValue {0} > {1} is {2}, storing {3} in Position: {2}".format(valueToCheck1, valueToCheck2, result, int(result)))
				self.currentIndex += 4				
				
			
			else:
				printToLog(1, "BREAK-BREAK-BREAK")
				# Executing Code 99
				break
			
		return
		
def checkInputs(phaseSettingsSeed):

	ampInputSignal = '0'
	
	for phaseSetting in phaseSettingsSeed:
		# reset the stdin/STDOUT
		myStdIn = StringIO()
		myStdOut = StringIO()
		
		# Seed the input feed
		sys.stdout = myStdIn
		print(str(phaseSetting))
		print(str(ampInputSignal)) 
		printToLog(1, "\n===================================================")
		printToLog(1, "Excecuting Program with Phase {0} and Amp {1}".format(phaseSetting, ampInputSignal))
			
		# Reset Input File and redirect Stdin
		sys.stdin = myStdIn	
		myStdIn.seek(0)
		sys.stdout = myStdOut
		
		# Execute the program
		computer=IntcodeComputer(projectInput)
		computer.execCode()
		
		# Now get the output 		
		myStdOut.seek(0)
		ampInputSignal = str(myStdOut.getvalue().split()[0]).zfill(5)
		printToLog(1, "Amp Out Signal: {0}".format(ampInputSignal))
		myStdIn.flush()
		myStdOut.flush()
		
	return ampInputSignal

def main():
	
	oldStdOut = sys.stdout 
	oldStdIn = sys.stdin
	
	phaseSettingsArray = list(permutations(basePhaseSettings, len(basePhaseSettings)))
	bestOutput = 0
	bestCombo = []

	for phaseSetting in phaseSettingsArray:
		ampOutput =  int(checkInputs(phaseSetting))
		if ampOutput > bestOutput:
			bestOutput = ampOutput
			bestCombo = phaseSetting
	
	sys.stdout = oldStdOut
	sys.stdin = oldStdIn

	print(bestOutput)	
	printToLog(1, bestCombo)
	
			
if __name__ == "__main__":
	main()
