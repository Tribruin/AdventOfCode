#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from collections import OrderedDict
from timeit import timeit

# sys.path.append("/Users/rblount/Scripts/AdventOfCode/tools")

from AOC import AOC


class Room:
    def __init__(self, room_info: str) -> None:
        self.room_info = room_info
        self.checksum = room_info[room_info.find("[") + 1 : room_info.find("]")]
        self.room_number = int(
            room_info[room_info.rfind("-") + 1 : room_info.find("[")]
        )
        self.enc_name = room_info[0 : room_info.rfind("-")]
        self.checksum_dict = self._compute_checksum_dict()
        self.computed_checksum = "".join(list(self.checksum_dict.keys())[0:5])
        self.enc_shift = self.room_number % 26

    def _compute_checksum_dict(self) -> dict:

        checksum_dict = OrderedDict()
        for char in self.enc_name:
            if not char == "-":
                if char in checksum_dict.keys():
                    checksum_dict[char] += 1
                else:
                    checksum_dict[char] = 1

        new_dict = OrderedDict()
        for key in sorted(checksum_dict.keys()):
            new_dict[key] = checksum_dict[key]

        return dict(sorted(new_dict.items(), key=lambda x: x[1], reverse=True))

    def check_if_real_room(self) -> bool:

        if self.checksum == self.computed_checksum:
            return True

        return False

    def unencrypt_name(self) -> str:

        unenc_name = ""
        for char in self.enc_name:
            if char == "-":
                unenc_name += " "
            else:
                new_char = ord(char) + self.enc_shift
                if new_char > ord("z"):
                    new_char -= 26
                unenc_name += chr(new_char)

        return unenc_name


def parse_input(data: AOC) -> list:
    result = list()
    lines = data.read_lines()
    for line in lines:
        room = Room(line)
        result.append(room)

    return result


def part1():
    room_sum = 0
    for line in input:
        if line.check_if_real_room():
            room_sum += line.room_number
        # print(f"{line.room_info} {line.checksum_dict} {line.check_if_real_room()}")
    print(room_sum)


def part2():
    for line in input:
        result = line.unencrypt_name()
        if "north" in result:
            print(f"{result} - {line.room_number}")


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=False)
    global input
    input = parse_input(data)

    print(f"Time for Part One: {timeit(part1, number=1)}")
    print(f"Time for Part Two: {timeit(part2, number=1)}")


if __name__ == "__main__":
    main()
