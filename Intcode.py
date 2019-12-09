#!/usr/local/bin/python3

class IntcodeComputer:

	import sys
# 	from itertools import permutations
	
	def __init__ (self, program, logLevel):
		""" Establish execution program """
	
		self.programCode = program.split(",")
		self.currentIndex = 0
		self.steps = 0
		self.inputValues = []
		self.outputValues = []
		self.manualInput = True
		self.manualOutput = True
		self.logLevel = logLevel
		self.validInstructions = [1,2,3,4,5,6,7,8,99]
		
	def __printToLog(self, level, out):
		if level <= self.logLevel :
			print(out, file = sys.stderr)
		return
		
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
		self.__printToLog(1, "\t\tReturn Parameters: {0}".format(parms))
		return parms
		
	def evaluateParms(self, parms, mask):
		""" Evaluate Parms base on Mask and return real Parameter Values """
		
		self.__printToLog(1, "\t\tPassed Parameters: {0}".format(parms))
		returnParms=[]
		for i in range(len(parms)-1):
			maskCode = mask[0]
			parmValue = parms[i]
			if maskCode == '0':
				self.__printToLog(2, "\t\tGetting Position Value {0} from Position {1}".format(self.programCode[parmValue], parmValue))
				returnParms.append(int(self.programCode[parmValue]))
			elif maskCode == '1':
				self.__printToLog(2, "\t\tGetting Immediate Value {0} ".format(parmValue))
				returnParms.append(parmValue)
			else:
				self.__printToLog(0, "*** ILLEGAL MASK {0} ***".format(mask))
				exit()
			mask = mask[1:]
					
# 		Append Location store
		maskCode = mask[0]
		returnParms.append(int(parms[-1]))
 			
		return returnParms
				
		
	def getInstruction(self):
		""" Get the next instruction code"""
		nextInstruction = self.programCode[self.currentIndex].zfill(5)
		self.__printToLog(1,"Received Instruction Code {1} from Position {0}".format(self.currentIndex, nextInstruction))
		mask = nextInstruction[0:3][::-1]
		instruction = int(nextInstruction[3:5])
		return instruction, mask
		
	def returnCode(self, location):
		return int(self.programCode[location])
		
	def execCode(self):
		""" Execute Code """
	
		while True:
		
			self.steps += 1
			self.__printToLog(1,"--------------------------------------------------")
			self.__printToLog(3, self.programCode)
			instruction, mask = self.getInstruction()		
			self.__printToLog(2, "\tExecuting Code: {0} with Mask: {1}".format(instruction, mask))
	
			if instruction not in self.validInstructions:
				print(0, "** Illegal Instruction Code: {0} at Position: {1} and Step: {2}".format(instruction, self.currentIndex, self.steps))
				exit()
		
			if instruction == 1:
				parms = self.getParameters(3, mask)
				x, y, outputLocation = parms
				a = x + y
				self.updateLocation(outputLocation, a)
				self.__printToLog(2, "\tExecute {0} + {1} with result: {2} and stored in Position: {3}".format(x,y, a, outputLocation))
				self.currentIndex += 4

			
			elif instruction == 2:
				parms = self.getParameters(3, mask)
				x, y, outputLocation = parms
				a = x * y
				self.updateLocation(outputLocation, a)
				self.__printToLog(2, "\tExecute {0} * {1} with result: {2} and stored in Position: {3}".format(x,y, a, outputLocation))
				self.currentIndex += 4
				
			elif instruction == 3:
				parms = self.getParameters(1, mask)
				outputLocation = parms[-1]
				x = input()
				self.updateLocation(outputLocation,x)
				self.__printToLog(2, "\tReceived Input {0} and stored in Position: {1}".format(x,outputLocation))
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
				self.__printToLog(2, "\tPrinted value: {0} from Position: {1}".format(x, inputLocation))
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
				self.__printToLog(2, "\tValue {0} is {1}, jumping to Position: {2}".format(valueToCheck, (valueToCheck != 0), newLocation))
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
				self.__printToLog(2, "\tValue {0} is {1}, jumping to Position: {2}".format(valueToCheck, not (valueToCheck != 0), newLocation))
				self.currentIndex = int(newLocation)

			elif instruction == 7:
				parms = self.getParameters(3, mask)
				valueToCheck1, valueToCheck2, outputLocation = parms
				result = (valueToCheck1 < valueToCheck2)
				self.updateLocation(outputLocation, int(result))
				self.__printToLog(2, "\tValue {0} > {1} is {2}, storing {3} in Position: {2}".format(valueToCheck1, valueToCheck2, result, int(result)))
				self.currentIndex += 4
			
			elif instruction == 8:
				parms = self.getParameters(3, mask)
				valueToCheck1, valueToCheck2, outputLocation = parms
				result = (valueToCheck1 == valueToCheck2)
				self.updateLocation(outputLocation, int(result))
				self.__printToLog(2, "\tValue {0} > {1} is {2}, storing {3} in Position: {2}".format(valueToCheck1, valueToCheck2, result, int(result)))
				self.currentIndex += 4				
				
			
			else:
				self.__printToLog(1, "BREAK-BREAK-BREAK")
				# Executing Code 99
				break
			
		return
		
