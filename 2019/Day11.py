#!/usr/local/bin/python3

from Intcode import IntcodeComputer
import sys
from os import system
from io import StringIO
import numpy as np

logLevel = 0
directions = ["^" , "<", "V", ">"]
up, left, down, right = 0, 1, 2, 3
leftTurn, rightTurn = 0, 1
colorLabels = ["black", "white"]
black, white = 0, 1
xSize, ySize = 100, 50
panelDataType = np.dtype([('color', 'b'), ('touches', 'b')])
panels = np.zeros(xSize * ySize, dtype=panelDataType).reshape(xSize, ySize)
computerCode = "3,8,1005,8,326,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,28,2,1104,14,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,55,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,77,2,103,7,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,102,1006,0,76,1,6,5,10,1,1107,3,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,135,1,1002,8,10,2,1101,3,10,1006,0,97,1,101,0,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,172,1006,0,77,1006,0,11,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,201,1006,0,95,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,1002,8,1,226,2,3,16,10,1,6,4,10,1006,0,23,1006,0,96,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,261,1,3,6,10,2,1006,3,10,1006,0,78,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,101,0,8,295,1006,0,89,1,108,12,10,2,103,11,10,101,1,9,9,1007,9,1057,10,1005,10,15,99,109,648,104,0,104,1,21102,1,838365918100,1,21102,343,1,0,1106,0,447,21102,387365315476,1,1,21102,354,1,0,1106,0,447,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,0,179318254811,1,21102,401,1,0,1106,0,447,21102,1,97911876839,1,21101,0,412,0,1106,0,447,3,10,104,0,104,0,3,10,104,0,104,0,21101,838345577320,0,1,21101,435,0,0,1106,0,447,21102,1,838337188628,1,21101,0,446,0,1105,1,447,99,109,2,21202,-1,1,1,21101,40,0,2,21102,478,1,3,21101,0,468,0,1106,0,511,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,473,474,489,4,0,1001,473,1,473,108,4,473,10,1006,10,505,1102,1,0,473,109,-2,2106,0,0,0,109,4,2102,1,-1,510,1207,-3,0,10,1006,10,528,21101,0,0,-3,21202,-3,1,1,22101,0,-2,2,21101,1,0,3,21102,1,547,0,1106,0,552,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,575,2207,-4,-2,10,1006,10,575,22102,1,-4,-4,1105,1,643,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21101,0,594,0,1105,1,552,21201,1,0,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,613,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,635,22102,1,-1,1,21101,635,0,0,106,0,510,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0"

class RobotComputer(IntcodeComputer):

    def __init__ (self, program, logLevel):
        super().__init__(program, logLevel)
        self.outputArray = []
        self.robot = Robot()

    def receiveInput(self):
        x, y = self.robot.x, self.robot.y
        value = panels[x,y]['color']
        return value

    def printValue(self, value):
        self.outputArray.append(int(value))
        if len(self.outputArray) == 2:
            # Once we have two output values, use the robot to color and move
            self.robot.colorAndMove(self.outputArray[0], self.outputArray[1])
            self.outputArray=[]
            # self.robot.printArray(True)
            print("Step {0}".format(self.steps))
        return

class Robot:
    def __init__(self):
        self.x = xSize // 4
        self.y = ySize // 2
        # self.location = (self.x, self.y)
        self.orientation = up

    def __str__(self):

        return ("Position: ({0}, {1})\tOrientation: {2}\tPanel Color:{3}".format(self.x, self.y, directions[self.orientation], "black"))

    def colorAndMove(self, color, turn):
        # Paint panel
        panels[self.x, self.y]['color'] = color
        panels[self.x, self.y]['touches'] = True
        # Update Orientation
        if turn == leftTurn:
            self.orientation = self.orientation + 1 - (4 * (self.orientation == 3))
        elif turn == rightTurn:
            self.orientation = self.orientation - 1 + (4 * (self.orientation == 0))
        else:
            pass

        # Move Robot
        if self.orientation == up:
            self.y -= 1
        elif self.orientation == down:
            self.y += 1
        elif self.orientation == left:
            self.x -= 1
        elif self.orientation == right:
            self.x += 1
        else:
            pass

        return 

    def printArray(self, printRobot):
        # chars = [32,9632]
        chars = [ord("."), ord("#")]
        system('clear')
        for y in range(ySize):
            for x in range(xSize):
                if (x == self.x)  and (y == self.y) and (printRobot):
                    print(directions[self.orientation], end='')
                else:
                    pixel=panels[x,y]['color']
                    print(chr(chars[pixel]), end = '')
            print()
        print()
        return

    def countTouches(self):
        return np.count_nonzero(panels['touches'] == True)
               


def main():

    # oldStdOut = sys.stdout 
	# oldStdIn = sys.stdin
	
    computer = RobotComputer(computerCode, logLevel)
    computer.execCode()
    computer.robot.printArray(False)
    print(computer.robot.countTouches())


if __name__ == "__main__":
    main()
