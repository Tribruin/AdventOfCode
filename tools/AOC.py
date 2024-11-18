import requests
import sys
import subprocess
import re
from os import path
from datetime import datetime
from TerminalColors import RED, ENDCOLOR

# Login in to Advent of Code and get the session cookie. Cookies last one month,
# so will need to reset every year
# Update .env file with new SessionID
# response = subprocess.run(
#     ["op", "items", "get", "AOCSessionID", "--fields", "SessionID"],
#     stdout=subprocess.PIPE,
#     check=True,
#     text=True
# )
# SESSION_ID = str(response.stdout).strip()


class AOC:
    def __init__(self, day, year, test=True):
        self.day = int(day)
        self.year = int(year)
        self.test_file = test
        self.script_path = path.dirname(sys.argv[0])
        if self.test_file:
            self.input_file = f"{self.script_path}/Day{self.day}-Input-Test.txt"
            print("Using test data from existing input file")
            if not path.exists(self.input_file):
                raise FileNotFoundError("Test Input File does not exist")
        else:
            self.input_file = f"{self.script_path}/Day{self.day}-Input.txt"
            # self._pull_input_data_from_aoc()
        self.file = self._read_file()
        self.lines = self._read_file_as_lines()

    def _read_file_as_lines(self):
        with open(self.input_file, "r") as f:
            lines = f.read().splitlines()
        return lines

    def _read_file(self):
        with open(self.input_file, "r") as f:
            file = f.read()
        return file

    # def _pull_input_data_from_aoc(self):
    #     if not path.exists(self.input_file):
    #         print(f"Pulling Input from AOC Website for Day: {self.day}")
    #         aoc_input_url = f"https://adventofcode.com/{self.year}/day/{self.day}/input"
    #         cookies = dict(session=SESSION_ID)
    #         response = requests.get(url=aoc_input_url, cookies=cookies)

    #         txt = response.text
    #         with open(self.input_file, "w") as f:
    #             f.write(txt)

    def read_int(self):
        array = [int(x) for x in self.lines]
        return array

    def read_file(self):
        return self.file

    def read_lines_no_strip(self):
        array = [x for x in self.lines]
        return array

    def read_int_in_line(self):
        array = [int(x) for x in self.lines[0].split(",")]
        return array

    def read_lines(self):
        array = [x.strip() for x in self.lines]
        return array

    def split_line(self, delimiter=","):
        line = self.lines[0]
        array = [x.strip() for x in line.split(delimiter)]
        return array

    def split_lines(self, delimeter=","):
        line_array = list()
        for line in self.lines:
            array = [x.strip() for x in line.split(delimeter)]
            line_array.append(array)
        return line_array

    def split_line_re(self, regex=","):
        array = [re.split(regex, x) for x in self.read_lines()]
        return array

    def split_line_re_int(self, regex=","):
        array = self.split_line_re(regex)
        array = [list(map(int, x)) for x in array]
        return array

    def find_all_in_lines(self, regex="-?\d+"):
        array = [re.findall(regex, x) for x in self.read_lines()]
        return array

    def find_all_ints_in_lines(self):
        array = self.find_all_in_lines()
        array = [[int(x) for x in y] for y in array]
        return array


def addTuples(a: tuple, b: tuple) -> tuple:
    """Add two tuples togeter. Tuples must be the same length"""

    if len(a) != len(b):
        raise TypeError("Tuple lenghts must be the same")

    temp = [a[i] + b[i] for i in range(len(a))]
    return tuple(temp)


def subtractTuples(a: tuple, b: tuple) -> tuple:
    """Add two tuples togeter. Tuples must be the same length"""

    if len(a) != len(b):
        raise TypeError("Tuple lenghts must be the same")

    temp = [a[i] - b[i] for i in range(len(a))]
    return tuple(temp)


def manhattan_dist(a: tuple, b: tuple) -> int:
    dist = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return dist


def getDateYear() -> tuple:
    codePath = path.dirname(sys.argv[0])
    absCodePath = path.abspath(codePath)
    codeDate = int(absCodePath.split("/")[-1][3:])
    codeYear = int(absCodePath.split("/")[-2])
    print(
        f"Running Advent of Code for Year: {RED}{codeYear}{ENDCOLOR} - Day {RED}{codeDate}{ENDCOLOR}"
    )
    return (codeDate, codeYear)


def findLenXLenY(locs: list) -> (tuple, tuple):
    minx = min([x[0] for x in locs])
    miny = min([x[1] for x in locs])
    maxx = max([x[0] for x in locs])
    maxy = max([x[1] for x in locs])
    return (minx, miny), (maxx, maxy)


def main():
    day = datetime.now().day
    if day > 25:
        day = 25
    a = AOC(day, False)
    test = a.read_lines()
    print(test)


if __name__ == "__main__":
    main()
