#!/usr/bin/env python
import sys


class IntcodeComputer:
    """ Special Intcode Computer for Advent of Code """

    # 	from itertools import permutations

    def __init__(self, program, logLevel):
        """ Establish execution program """

        self.programCode = program.split(",")
        self.initialProgramCode = self.programCode
        self.currentIndex = 0
        self.steps = 0
        self.relativeBase = 0
        self.inputValues = []
        self.outputValues = []
        self.manualInput = True
        self.manualOutput = True
        self.logLevel = logLevel
        self.validInstructions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 99]

    def __printToLog(self, level, out):
        if level == 0:
            out = "*** ERROR: " + out + "***"
            print(out, file=sys.stderr)
        if level <= self.logLevel:
            out = "  " * (level - 1) + out
            print(out, file=sys.stderr)
        return

    def resetCode(self):
        self.initialProgramCode = self.programCode
        self.currentIndex = 0
        self.steps = 0
        self.relativeBase = 0

    def updateLog(self, level):
        self.logLevel = level
        return

    def __extendCode(self, location):
        self.__printToLog(
            4,
            "Extending Program Code by: {0} steps".format(
                location - len(self.programCode) + 1
            ),
        )
        self.__printToLog(
            4, "New Program Code Lenght: {0}".format(len(self.programCode))
        )
        self.programCode.extend((location - len(self.programCode) + 1) * ["0"])

    def writeLocation(self, locValue, value):
        checkValue, mask = locValue
        if mask == "0":
            location = checkValue
        elif mask == "2":
            location = self.relativeBase + checkValue
        else:
            self.__printToLog(0, "*** ILLEGAL MASK {0} ***".format(mask))

        self.__printToLog(3, "Storing {0} in Location: {1}".format(value, location))
        if location > len(self.programCode) - 1:
            self.__extendCode(location)
        self.programCode[location] = str(value)
        return location

    def readFromLocation(self, locValue):
        checkValue, mask = locValue
        if mask == "0":
            location = checkValue
            if location > len(self.programCode) - 1:
                self.__extendCode(location)
            x = self.programCode[location]
            self.__printToLog(
                3, "Getting Position Value {0} from Position {1}".format(x, location)
            )
        elif mask == "1":
            self.__printToLog(3, "Getting Immediate Value {0} ".format(checkValue))
            return checkValue, "N/A"
        elif mask == "2":
            location = self.relativeBase + checkValue
            if location > len(self.programCode) - 1:
                self.__extendCode(location)
            x = self.programCode[location]
            self.__printToLog(
                3,
                "Getting Relative Value {0} from Position {1} using Relative Base: {2} and Offset: {3}".format(
                    x, location, self.relativeBase, checkValue
                ),
            )
        else:
            self.__printToLog(0, "ILLEGAL MASK {0}".format(mask))

        # Check to see if location is outside current program, if so extend
        self.__printToLog(3, "Reading from Location: {0}".format(location))
        if location > len(self.programCode) + 1:
            self.__printToLog(
                3,
                "Extending Program Code by: {0} steps".format(
                    location - len(self.programCode) + 1
                ),
            )
            self.programCode.extend((location - len(self.programCode) + 1) * ["0"])
        x = self.programCode[location]
        self.__printToLog(3, "Return Value: {0}".format(x))
        return x, location

    def getParameters(self, number, mask):
        """ Get the parameters based on 'number' of parameters"""
        strParameters = self.programCode[
            self.currentIndex + 1 : self.currentIndex + number + 1
        ]
        parameters = list(map(lambda x: int(x), strParameters))
        parms = self.evaluateParms(parameters, mask)
        self.__printToLog(2, "Return Parameters: {0}".format(parms))
        return parms

    def evaluateParms(self, parms, mask):
        """ Evaluate Parms base on Mask and return real Parameter Values """
        self.__printToLog(2, "Passed Parameters: {0}".format(parms))
        lenOfParms = len(parms)
        returnParms = []
        for i in range(lenOfParms - 1):
            maskCode = mask[i]
            parmValue = parms[i]
            outValue = (parmValue, maskCode)
            value, location = self.readFromLocation(outValue)
            returnParms.append(int(value))

        # 		Append Location store
        maskCode = mask[lenOfParms - 1]
        returnParms.append(int(parms[-1]))
        return returnParms

    def receiveInput(self):
        x = input()
        return x

    def printValue(self, value):
        print(value)
        return

    def getInstruction(self):
        """ Get the next instruction code"""
        nextInstruction = self.programCode[self.currentIndex].zfill(5)
        self.__printToLog(
            1,
            "Step: {2} - Received Instruction Code {1} from Position {0}".format(
                self.currentIndex, nextInstruction, self.steps
            ),
        )
        mask = nextInstruction[0:3][::-1]
        instruction = int(nextInstruction[3:5])
        return instruction, mask

    def execCode(self):
        """ Execute Code """

        while True:

            self.steps += 1
            self.__printToLog(1, "--------------------------------------------------")
            self.__printToLog(5, str(self.programCode))
            instruction, mask = self.getInstruction()
            self.__printToLog(
                2, "Executing Code: {0} with Mask: {1}".format(instruction, mask)
            )

            if instruction not in self.validInstructions:
                self.__printToLog(
                    0,
                    "Illegal Instruction Code: {0} at Position: {1} and Step: {2}".format(
                        instruction, self.currentIndex, self.steps
                    ),
                )
                exit()

            if instruction == 1:
                parms = self.getParameters(3, mask)
                x, y, outputLoc = parms
                a = x + y
                outputArray = (outputLoc, mask[2])
                outputLocation = self.writeLocation(outputArray, a)
                self.__printToLog(
                    1,
                    "Execute {0} + {1} with result: {2} and stored in Position: {3}".format(
                        x, y, a, outputLocation
                    ),
                )
                self.currentIndex += 4

            elif instruction == 2:
                parms = self.getParameters(3, mask)
                x, y, outputLoc = parms
                a = x * y
                outputArray = (outputLoc, mask[2])
                outputLocation = self.writeLocation(outputArray, a)
                self.__printToLog(
                    1,
                    "Execute {0} * {1} with result: {2} and stored in Position: {3}".format(
                        x, y, a, outputLocation
                    ),
                )
                self.currentIndex += 4

            elif instruction == 3:
                parms = self.getParameters(1, mask)
                outputLoc = (int(parms[0]), mask[0])
                x = self.receiveInput()
                outputLocation = self.writeLocation(outputLoc, x)

                self.__printToLog(
                    1,
                    "Received Input {0} and stored in Position: {1}".format(
                        x, outputLocation
                    ),
                )
                self.currentIndex += 2

            elif instruction == 4:
                parms = self.getParameters(1, mask)
                outputLoc = (parms[0], mask[0])
                location = parms[0]
                x, inputLocation = self.readFromLocation(outputLoc)
                self.printValue(x)
                self.__printToLog(
                    1, "Printed value: {0} from Position: {1}".format(x, inputLocation)
                )
                self.currentIndex += 2

            elif instruction == 5:
                parms = self.getParameters(2, mask)
                valueToCheck, locValue = parms
                outputLoc = (locValue, mask[1])
                newLocation, inputLocation = self.readFromLocation(outputLoc)
                if valueToCheck:
                    self.currentIndex = int(newLocation)
                else:
                    newLocation = self.currentIndex + 3
                self.__printToLog(
                    1,
                    "Value {0} != 0 is {1}, jumping to Position: {2}".format(
                        valueToCheck, (valueToCheck != 0), newLocation
                    ),
                )
                self.currentIndex = int(newLocation)

            elif instruction == 6:
                parms = self.getParameters(2, mask)
                valueToCheck, locValue = parms
                outputLoc = (locValue, mask[1])
                newLocation, inputLocation = self.readFromLocation(outputLoc)
                if not valueToCheck:
                    self.currentIndex = newLocation
                else:
                    newLocation = self.currentIndex + 3
                self.__printToLog(
                    1,
                    "Value {0} = 0 is {1}, jumping to Position: {2}".format(
                        valueToCheck, not (valueToCheck != 0), newLocation
                    ),
                )
                self.currentIndex = int(newLocation)

            elif instruction == 7:
                parms = self.getParameters(3, mask)
                valueToCheck1, valueToCheck2, locValue = parms
                outputLoc = (locValue, mask[2])
                result = valueToCheck1 < valueToCheck2
                location = self.writeLocation(outputLoc, int(result))
                self.__printToLog(
                    1,
                    "Value {0} < {1} is {2}, storing {3} in Position: {4}".format(
                        valueToCheck1, valueToCheck2, result, int(result), location
                    ),
                )
                self.currentIndex += 4

            elif instruction == 8:
                parms = self.getParameters(3, mask)
                valueToCheck1, valueToCheck2, locValue = parms
                outputLoc = (locValue, mask[2])
                result = valueToCheck1 == valueToCheck2
                outputLocation = self.writeLocation(outputLoc, int(result))
                self.__printToLog(
                    1,
                    "Value {0} == {1} is {2}, storing {3} in Position: {4}".format(
                        valueToCheck1,
                        valueToCheck2,
                        result,
                        int(result),
                        outputLocation,
                    ),
                )
                self.currentIndex += 4

            elif instruction == 9:
                parms = self.getParameters(1, mask)
                outputLoc = (parms[0], mask[0])
                baseUpdate, location = self.readFromLocation(outputLoc)
                self.relativeBase += int(baseUpdate)
                self.__printToLog(
                    1,
                    "Updating RELATIVEBASE by {0} to {1}".format(
                        baseUpdate, self.relativeBase
                    ),
                )
                self.currentIndex += 2

            else:
                self.__printToLog(
                    1,
                    "**********************\n*** END OF PROGRAM ***\n**********************",
                )
                # Executing Code 99
                break

        return

