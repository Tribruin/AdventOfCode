import timeit

INPUT_FILE = "Day8-Input.txt"


class Boot_Code:
    def __init__(self, input_file) -> None:

        self.acc = 0
        self.instruction = 0
        with open(INPUT_FILE, mode="r") as f:
            code_lines = f.read().split("\n")
            self.code = [
                (line.split()[0], int(line.split()[1]), False) for line in code_lines
            ]
        self.orig_code = self.code.copy()

    def _reset_code(self):
        self.code = self.orig_code.copy()
        self.instruction = 0
        self.acc = 0

    def exec_code(self):
        while self.instruction < len(self.code):

            op, arg, prev_exec = self.code[self.instruction]
            if prev_exec:
                return False

            if op == "nop":
                self.code[self.instruction] = (op, arg, True)
                self.instruction += 1

            elif op == "acc":
                self.code[self.instruction] = (op, arg, True)
                self.acc += arg
                self.instruction += 1

            elif op == "jmp":
                self.code[self.instruction] = (op, arg, True)
                self.instruction += arg

            else:
                pass

        return True

    def run_code_check(self):

        # Reset Code
        test_cycle = 0

        while True:
            self._reset_code()
            op, arg, prev_exec = self.code[test_cycle]

            if op in ["nop", "jmp"]:
                if op == "nop":
                    self.code[test_cycle] = ("jmp", arg, prev_exec)
                else:
                    self.code[test_cycle] = ("nop", arg, prev_exec)
                result = self.exec_code()
                if result:
                    print(
                        f"Success: {test_cycle} - {self.code[test_cycle]} Acc: {self.acc}"
                    )
                    return
                else:
                    pass
                    # print(
                    #     f"Failure: {test_cycle} - {self.code[test_cycle]} Acc: {self.acc}"
                    # )

            test_cycle += 1


def part1():
    boot_code.exec_code()
    print(boot_code.acc)


def part2():
    boot_code.run_code_check()


boot_code = Boot_Code(INPUT_FILE)
print(timeit.timeit(part1, number=1))
print(timeit.timeit(part2, number=1))
