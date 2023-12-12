#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC
from collections import deque

testing = True


class ALU:
    def __init__(self, code: list, input_val: list) -> None:
        self.registers = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
        self.reg_keys = self.registers.keys()
        self.code = code
        self.input_val = deque(input_val)
        self.bad_code = False

    def run_code(self):
        for line in self.code:
            cmd = line[0]
            reg1 = line[1]
            if len(line) == 3:
                if line[2] in self.reg_keys:
                    reg2 = self.registers[line[2]]
                else:
                    reg2 = int(line[2])

            if cmd == "inp":
                self.registers[reg1] = int(self.input_val.popleft())

            elif cmd == "add":
                self.registers[reg1] = self.registers[reg1] + reg2

            elif cmd == "mod":
                if self.registers[reg1] < 0 or reg2 < 0:
                    return False
                self.registers[reg1] = self.registers[reg1] % reg2

            elif cmd == "div":
                if reg2 == 0:
                    return False
                self.registers[reg1] = self.registers[reg1] // reg2

            elif cmd == "mul":
                self.registers[reg1] = self.registers[reg1] * reg2

            else:
                if self.registers[reg1] == reg2:
                    self.registers[reg1] = 1
                else:
                    self.registers[reg1] = 0

        # print(self.registers)
        return (self.registers['z'] == 0)


def parse_input(data_input):
    result = list()
    for line in data_input:
        line_split = line.split()
        result.append(line_split)
    return result


def split_string(text: str) -> list:
    list = [x for x in text]
    return list


def part1(data_input):
    top_code = ""
    for i in range(99999999999999, 0, -1):
        input_text = split_string(str(i).zfill(14))
        if not ('0' in input_text):
            alu = ALU(data_input, input_text)
            print("".join(input_text))
            if alu.run_code():
                print("".join(input_text))


def part2(data_input):
    pass


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    # global data
    code_data = AOC(codeDate, codeYear, test=testing)
    data_input = code_data.read_lines()
    data_input = parse_input(data_input)

    part1(data_input)
    part2(data_input)


if __name__ == "__main__":
    main()
