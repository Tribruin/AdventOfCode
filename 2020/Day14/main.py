import sys
import re
from itertools import permutations, combinations, combinations_with_replacement, product
from typing import List

# sys.path.append("/Users/rblount/Scripts/AdventOfCode/tools")

from AOC import AOC


def parse_input(lines):
    cmds = list()
    for line in lines:
        cmd, value = line.split(" = ")
        if cmd[:3] == "mem":
            cmd, mem = cmd[:3], cmd.split("[")[1][:-1]
            cmds.append([cmd, int(mem), int(value)])
        else:
            cmds.append([cmd, value])
    return cmds


def part1():
    def mask_num_part1(mask, value) -> int:
        # Convert int (value) to 36 digit binary digit
        num_bin = f"{value:036b}"
        masked_value = ""
        for i in range(len(num_bin)):
            if mask[i] == "X":
                masked_value += num_bin[i]
            else:
                masked_value += mask[i]
        return int(masked_value, 2)

    memory = dict()
    for cmd in cmds:
        if cmd[0] == "mask":
            mask = cmd[1]
        else:
            mem, value = cmd[1], cmd[2]
            memory[mem] = mask_num_part1(mask, value)
    print(sum(memory.values()))


def mask_num_part2(mask, memory_position) -> int:
    def flatten(T):
        """
        Flatten mulitple imbeeded tuples
        for example ((1,2), 3) -> (1, 2, 3)
        """
        if type(T) != tuple:
            return (T,)
        elif len(T) == 0:
            return ()
        else:
            return flatten(T[0]) + flatten(T[1:])

    def replace_x(mask) -> list:
        all_numbers = list()
        xs_found = list()
        # Find all the X in the mask in note their position
        for i in range(len(mask)):
            if mask[i] == "X":
                xs_found.append(i)

        # Create a set of tuples of all the combinations of (0,1) * No. of Xs
        # Exmaple if there are 2 Xs, the tuples are (0,0), (0,1), (1,0), (1,1)
        subs = [0, 1]
        for i in range(len(xs_found) - 1):
            subs = product(subs, [0, 1])
            subs = [flatten(i) for i in subs]

        for sub in subs:
            # loop though the mask substiutions and create new masks
            new_mask = mask
            for i in range(len(xs_found)):
                new_mask = (
                    new_mask[0 : xs_found[i]]
                    + f"{sub[i]}"
                    + new_mask[xs_found[i] + 1 :]
                )
            all_numbers.append(new_mask)

        return all_numbers

    # Convert int (value) to 36 digit binary digit
    mem_pos_binary = f"{memory_position:036b}"
    masked_memory_pos = ""
    add_array = list()
    for i in range(len(mem_pos_binary)):
        if mask[i] == "X":
            masked_memory_pos += "X"
        elif mask[i] == "1":
            masked_memory_pos += "1"
        else:
            masked_memory_pos += mem_pos_binary[i]

    return replace_x(masked_memory_pos)


def part2():
    memory = {}
    for cmd in cmds:
        if cmd[0] == "mask":
            mask = cmd[1]
        else:
            inital_mem_address, value = cmd[1], cmd[2]
            mem_addresses = mask_num_part2(mask, inital_mem_address)
            for mem_value in mem_addresses:
                memory[int(mem_value, 2)] = value
    print(sum(memory.values()))
    return


a = AOC(14, test=False)
cmds = parse_input(a.read_lines())
part1()
part2()
