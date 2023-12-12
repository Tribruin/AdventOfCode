#!/usr/local/bin/python3

# log = True
log = False

validInstructions = [1, 2, 99]

# Test Input
# input = "1,1,1,4,99,5,6,0,99"

# Real Input
input = "1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,6,27,1,9,27,31,1,31,10,35,2,13,35,39,1,39,10,43,1,43,9,47,1,47,13,51,1,51,13,55,2,55,6,59,1,59,5,63,2,10,63,67,1,67,9,71,1,71,13,75,1,6,75,79,1,10,79,83,2,9,83,87,1,87,5,91,2,91,9,95,1,6,95,99,1,99,5,103,2,103,10,107,1,107,6,111,2,9,111,115,2,9,115,119,2,13,119,123,1,123,9,127,1,5,127,131,1,131,2,135,1,135,6,0,99,2,0,14,0"
testValue = 19690720


def printToLog(out):
    if log:
        print(out)
    return


class IntcodeComputer:

    def __init__(self, program):
        """ Establish execution program """

        self.programCode = program.split(",")
        self.currentIndex = 0

    def updateLocation(self, location, value):
        self.programCode[location] = str(value)
        return

    def getParameters(self, number, mask):
        """ Get the parameters based on 'number' """
        strParameters = self.programCode[self.currentIndex+1: self.currentIndex + number + 1]
        parameters = list(map(lambda x: int(x), strParameters))
        parms = self.evaluateParms(parameters, mask)
        printToLog("\tReturn Parameters: {0}".format(parms))
        return parms

    def evaluateParms(self, parms, mask):
        """ Evaluate Parms base on Mask and return real Parameter Values """

        printToLog("\tPassed Parameters: {0}".format(parms))
        returnParms = []
        for i in range(len(parms)-1):
            if mask[i] == '0':
                returnParms.append(int(self.programCode[parms[i]]))
            elif mask[i] == '1':
                returnParms.append(parms[i])
            else:
                print("*** ILLEGAL MASK {0} ***".format(mask))
        # Append Location store
        returnParms.append(int(parms[-1]))
        return returnParms

    def getInstruction(self):
        """ Get the next instruction code"""
        printToLog("Getting Instruction Code from Position {0}".format(self.currentIndex))
        nextInstruction = self.programCode[self.currentIndex].zfill(5)
        mask = nextInstruction[0:3][::-1]
        instruction = int(nextInstruction[3:5])
        printToLog("\tReturning Code: {0} with mask: {1}".format(instruction, mask))
        return instruction, mask

    def returnCode(self, location):
        return int(self.programCode[location])

    def execCode(self):
        """ Execute Code """

        while True:
            instruction, mask = self.getInstruction()

            printToLog("Executing Code: {0} with Mask: {1}".format(instruction, mask))

            if instruction not in validInstructions:
                print("** Illegal Instruction Code: {0}".format(instruction))
                exit()

            if instruction == 1:
                parms = self.getParameters(3, mask)
                outputLocation = parms[2]
                x, y = parms[0], parms[1]
                a = x + y
                self.updateLocation(outputLocation, a)
                printToLog("\tExecute {0} + {1} with result: {2} and stored in Position: {3}".format(x, y, a, outputLocation))
                self.currentIndex += 4

            elif instruction == 2:
                parms = self.getParameters(3, mask)
                outputLocation = parms[2]
                x, y = parms[0], parms[1]
                a = x * y
                self.updateLocation(outputLocation, a)
                printToLog("\tExecute {0} * {1} with result: {2} and stored in Position: {3}".format(x, y, a, outputLocation))
                self.currentIndex += 4

            else:
                # Executing Code 99
                break

        return


def testComputer():

    for noun in range(0, 99):
        for verb in range(0, 99):

            testInput = input
            computer = IntcodeComputer(testInput)
            computer.updateLocation(1, noun)
            computer.updateLocation(2, verb)
            computer.execCode()
            if computer.returnCode(0) == testValue:
                return noun, verb

    return 0, 0


def main():

    # part 1
    computer = IntcodeComputer(input)
    computer.execCode()
    print("Part 1 Return Code: {0}".format(computer.returnCode(0)))

    # Part 2
    noun, verb = testComputer()
    print("Noun: {0}, Verb: {1}, Result Code: {2}".format(noun, verb, noun*100 + verb))


if __name__ == "__main__":
    main()
