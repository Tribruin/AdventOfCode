#!/usr/local/bin/python3

import sys
from io import StringIO
from itertools import permutations
from Intcode import IntcodeComputer

# Turn on logging (printed to STDERR)
logLevel = 1

projectInput = "3,8,1001,8,10,8,105,1,0,0,21,46,59,84,93,110,191,272,353,434,99999,3,9,101,2,9,9,102,3,9,9,1001,9,5,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,102,5,9,9,4,9,99,3,9,1001,9,4,9,1002,9,2,9,101,2,9,9,102,2,9,9,1001,9,3,9,4,9,99,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,1001,9,5,9,1002,9,3,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99"
basePhaseSettings = ['0', '1', '2', '3', '4']


def printToLog(level, out):
    if level <= logLevel:
        print(out, file=sys.stderr)
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
        computer = IntcodeComputer(projectInput, logLevel)
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
        ampOutput = int(checkInputs(phaseSetting))
        if ampOutput > bestOutput:
            bestOutput = ampOutput
            bestCombo = phaseSetting

    sys.stdout = oldStdOut
    sys.stdin = oldStdIn

    print(bestOutput)
    printToLog(1, bestCombo)


if __name__ == "__main__":
    main()
