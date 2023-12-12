inputfile = "/Users/rblount/Scripts/AdventOfCode/2015/Day23.txt"


class Computer:
    def __init__(self, code):
        self.register = {}
        self.register["a"] = 0
        self.register["b"] = 0
        self.code = code

    def run(self):
        step = 0
        lastStep = len(self.code)
        while step < lastStep:
            nextInstruction = self.code[step]["instruct"]
            nextRegister = self.code[step]["register"]
            if nextInstruction == "hlf":
                self.register[nextRegister] = self.register[nextRegister] // 2
                step += 1
            elif nextInstruction == "tpl":
                self.register[nextRegister] = self.register[nextRegister] * 3
                step += 1
            elif nextInstruction == "inc":
                self.register[nextRegister] += 1
                step += 1
            elif nextInstruction == "jmp":
                step += int(nextRegister)
            elif nextInstruction == "jie":
                if (self.register[nextRegister] % 2) == 0:
                    step += self.code[step]["offset"]
                else:
                    step += 1
            elif nextInstruction == "jio":
                if (self.register[nextRegister] % 2) != 0:
                    step += self.code[step]["offset"]
                else:
                    step += 1
            else:
                pass


def readInput(name):
    codeLines = []
    f = open(name, "r")
    for line in f.readlines():
        codeLine = {}
        lineSplit = line.split(" ")
        codeLine["instruct"] = lineSplit[0].strip()
        codeLine["register"] = lineSplit[1].strip().strip(",")
        if len(lineSplit) == 3:
            codeLine["offset"] = int(lineSplit[2].strip())
        codeLines.append(codeLine)

    return codeLines


def part1():
    code = readInput(inputfile)
    computer = Computer(code)
    computer.run()
    print(computer.register["a"])
    print(computer.register["b"])


part1()