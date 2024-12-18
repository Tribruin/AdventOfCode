from AOC import AOC, getDateYear
from TerminalColors import *

testing = False


def parse_input(codeInput: AOC):
    lines = codeInput.find_all_ints_in_lines()
    a = lines[0][0]
    b = lines[1][0]
    c = lines[2][0]
    program = lines[4]
    return ((a, b, c), program)


def combo(operand, a, b, c) -> int:
    if operand <= 3:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    else:
        raise TypeError("Bad Operand")


def computer(a, b, c, program):
    output = ""
    cycle = 0
    ptr = 0
    while ptr < len(program):
        opcode, operand = program[ptr], program[ptr + 1]
        match opcode:
            case 0:
                # adv - devide A by 2 ^ combo operand power and truncate to int. Store in A
                a = a // (2 ** combo(operand, a, b, c))
                # output += str(a)
            case 1:
                # bxl - Perform a XOR on B and literal operand and store in B
                b = b ^ operand  # ^ is the XOR operation
                # output += str(b)
            case 2:
                # bst - calculat combo mod 8 and store in B
                b = combo(operand, a, b, c) % 8
                # output += str(b)
            case 3:
                # jnz - jump ptr on literal operand if a != 0
                if a != 0:
                    ptr = operand - 2  # jump by operand - 2 as we will add 2 at the end
                    # output += str(b)
            case 4:
                # bxc - perform B XOR C and store in B
                b = b ^ c
                # output += str(b)
            case 5:
                # out - calculate the combo operand mod 8 and output its number
                value = combo(operand, a, b, c) % 8
                # print(f"Outputing {value} at {cycle}")
                output += str(value)
            case 6:
                # bdv - devide A by 2 ^ combo operand power and truncate to int. Store in A
                b = a // (2 ** combo(operand, a, b, c))
                # output += str(b)
            case 7:
                # cdv - devide A by 2 ^ combo operand power and truncate to int. Store in A
                c = a // (2 ** combo(operand, a, b, c))
                # output += str(c)
        ptr += 2
        cycle += 1
    return output


def part1(dataInput):
    (a, b, c), program = dataInput
    output = computer(a, b, c, program)
    final_output = ",".join([x for x in output])
    print(final_output)


def part2(dataInput):
    new_poss_a = [0]
    (a_prime, b, c), program = dataInput
    visual_program = "".join([str(x) for x in program])
    final_output = ""
    count = -1

    while final_output != program:
        poss_a = list()
        for a_prime in new_poss_a:
            for a_temp in range(a_prime, a_prime + 8):
                output = computer(a_temp, b, c, program)
                if output == visual_program[count:]:
                    # print(f"Check A={a_temp} o={output[count:]}")
                    poss_a.append(a_temp)
                    final_output = [int(x) for x in output]
        new_poss_a = [x * 8 for x in poss_a]
        count -= 1
        pass
    lowest_value = sorted(poss_a)[0]
    print(f"Lowest A Value is {lowest_value}")


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
