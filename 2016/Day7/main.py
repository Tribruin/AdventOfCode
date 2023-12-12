#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python

import sys
import os
from timeit import timeit

# sys.path.append("/Users/rblount/Scripts/AdventOfCode/tools")

from AOC import AOC

testing = False


class IP_Address:
    def __init__(self, input_string: str) -> None:
        self.input_string = input_string
        self._split_address()

    def _split_address(self) -> None:
        self.address_parts = list()
        self.hypernet_parts = list()
        string = self.input_string
        while string.find("[") >= 0:
            address = string[0 : string.find("[")]
            hypernet = string[string.find("[") + 1 : string.find("]")]
            self.address_parts.append(address)
            self.hypernet_parts.append(hypernet)
            string = string[string.find("]") + 1 :]
        if len(string) > 0:
            self.address_parts.append(string)
        return

    def check_for_abba_hypernet(self):
        for part in self.hypernet_parts:
            for i in range(len(part) - 3):
                if (
                    part[i] == part[i + 3]
                    and part[i + 1] == part[i + 2]
                    and part[i] != part[i + 2]
                ):
                    return True
        return False

    def check_for_abba(self) -> bool:
        for part in self.address_parts:
            for i in range(len(part) - 3):
                if (
                    part[i] == part[i + 3]
                    and part[i + 1] == part[i + 2]
                    and part[i] != part[i + 2]
                ):
                    if not self.check_for_abba_hypernet():

                        return True
        return False

    def check_for_aba(self) -> bool:
        def check_for_bab(aba) -> bool:
            a = aba[0]
            b = aba[1]
            for part in self.hypernet_parts:
                for i in range(len(part) - 2):
                    if part[i] == b and part[i + 1] == a and part[i + 2] == b:
                        return True
            return False

        for part in self.address_parts:
            for i in range(len(part) - 2):
                if part[i] == part[i + 2] and part[i] != part[i + 1]:
                    aba = part[i : i + 3]
                    if check_for_bab(aba):
                        return True
        return False


def part1():
    valid_ip_addresses = 0
    for ip_address in ip_addresses:
        if ip_address.check_for_abba():
            valid_ip_addresses += 1
    print(valid_ip_addresses)


def part2():
    valid_ip_addresses = 0
    for ip_address in ip_addresses:
        if ip_address.check_for_aba():
            valid_ip_addresses += 1
    print(valid_ip_addresses)


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=testing)
    global ip_addresses
    ip_addresses = list()
    for line in data.read_lines():
        ip_addresses.append(IP_Address(line))

    print(f"Time for Part One: {timeit(part1, number=1)}")
    print(f"Time for Part Two: {timeit(part2, number=1)}")


if __name__ == "__main__":
    main()
