from AOC import AOC, getDateYear
from TerminalColors import *

testing = True


def parse_input(codeInput: AOC):
    lines = codeInput.read_lines()
    registers = {}
    for idx, line in enumerate(lines):
        if line == "":
            break
        else:
            register, value = line.split(": ")
            registers[register] = int(value)

    operations = [x.split() for x in lines[idx + 1 :]]
    return (registers, operations)


def process_operation(registers, operations):
    while operations:
        opereration = operations.pop(0)
        reg1, operand, reg2, _, reg3 = opereration
        reg1_value = registers.get(reg1, None)
        reg2_value = registers.get(reg2, None)
        if reg2_value is None or reg1_value is None:
            print(
                f"Skipping operation {opereration} as one of the registers is not initialized"
            )
            operations.append(opereration)
            continue
        else:
            match operand:
                case "AND":
                    print(
                        f"{reg1_value} & {reg2_value} = {reg1_value & reg2_value} -> {reg3}"
                    )
                    registers[reg3] = reg1_value & reg2_value
                case "OR":
                    print(
                        f"{reg1_value} | {reg2_value} = {reg1_value | reg2_value} -> {reg3}"
                    )
                    registers[reg3] = reg1_value | reg2_value
                case "XOR":
                    print(
                        f"{reg1_value} ^ {reg2_value} = {reg1_value ^ reg2_value} -> {reg3}"
                    )
                    registers[reg3] = reg1_value ^ reg2_value
    return registers


def register_values(registers, leading_char):
    outut_regsiters = [x for x in registers if x.startswith(leading_char)]
    binary_number = ""
    for idx in range(99, -1, -1):
        zvalue = f"{leading_char}{idx:02}"
        if zvalue in outut_regsiters:
            binary_number += str(registers[zvalue])
            print(f"{zvalue} = {registers[zvalue]}")
    return int(binary_number, 2)


def part1(dataInput):
    original_registers, operations = dataInput
    registers = original_registers.copy()
    registers = process_operation(registers, operations)
    print(register_values(registers, "z"))


def find_all_ops_with_reg(operations, register):
    operations_with_register = []
    for operation in operations:
        reg1, operand, reg2, _, reg3 = operation
        if register == reg3:
            for register1 in [reg1, reg2]:
                if register1[0] in ["x", "y"]:
                    operations_with_register += [register1]
                else:
                    result = find_all_ops_with_reg(operations, register1)
                    operations_with_register += [register1] + result

    return list(set(operations_with_register))


def part2(dataInput):
    original_registers, operations = dataInput
    for idx in range(0, 45):
        reg = f"z{idx:02}"
        print(f"Register: {reg} - ", end="")
        print(find_all_ops_with_reg(operations, reg))


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    dataInput = parse_input(codeInput)

    # part1(dataInput)
    part2(dataInput)


if __name__ == "__main__":
    main()
