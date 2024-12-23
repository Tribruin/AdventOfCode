import requests
import sys
import subprocess
import re
from os import path
from datetime import datetime
from TerminalColors import RED, ENDCOLOR
from collections import OrderedDict

# Move offsets assuming a (y,x) coordinate system.
moveOffets = OrderedDict()
moveOffets["^"] = (-1, 0)
moveOffets[">"] = (0, 1)
moveOffets["v"] = (1, 0)
moveOffets["<"] = (0, -1)


class AOC:
    """
    Class for initializing an AOC day
    """

    def __init__(self, day, year, test=True):
        """Initialize the AOC clase

        Args:
            day (int): Day to run
            year (int): Year to run
            test (bool, optional): Whether to run with Test input or Actual Input. Defaults to True.

        Raises:
            FileNotFoundError: If the Input file does not exist.
        """
        self.day = int(day)
        self.year = int(year)
        self.test_file = test
        self.absCodePath = path.abspath(path.dirname(sys.argv[0]))

        if self.test_file:
            self.input_file = f"{self.absCodePath}/Day{self.day}-Input-Test.txt"
            print("Using test data input file")
            if not path.exists(self.input_file):
                raise FileNotFoundError("Test Input File does not exist")
        else:
            self.input_file = f"{self.absCodePath}/Day{self.day}-Input.txt"
            print("Using actual data input file.")
            if not path.exists(self.input_file):
                raise FileNotFoundError("Input File does not exist")

        # Read teh data a single file and a list of lines
        self.file = self._read_file()
        self.lines = self._read_file_as_lines()

    def _read_file_as_lines(self) -> list:
        """Read the input file as list string. One per line.

        Returns:
            list: list of strints
        """
        with open(self.input_file, "r") as f:
            lines = f.read().splitlines()
        return lines

    def _read_file(self) -> str:
        """Return a single string with contents of the input file

        Returns:
            str: Input file as a stirng
        """
        with open(self.input_file, "r") as f:
            file = f.read()
        return file

    def read_file(self) -> str:
        """Return the full input as single sting

        Returns:
            str: Input file as a stirng
        """
        return self.file

    def read_lines(self) -> list:
        """Return the input file as a list of strings.
        Strip any non printable characters before returning.

        Returns:
            list: Input file as a list with each line a string
        """
        array = [x.strip() for x in self.lines]
        return array

    def read_lines_no_strip(self) -> list:
        """Return the input file as a list of strings.
        Do not strip any characters.

        Returns:
            list: Input file as a list with each line a string
        """
        array = [x for x in self.lines]
        return array

    def read_int(self) -> list:
        """Returns list a integers. Works with input that is a single of integers

        Returns:
            list: list of integers
        """
        array = [int(x) for x in self.lines]
        return array

    def read_int_in_line(self, delimeter=","):
        """Read the file and split line by"""

        array = [int(x) for x in self.lines[0].split(",")]
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

    def split_line_re(self, regex=",") -> list:
        """Split all lines in the input using a regular expression

        Args:
            regex (str, optional): Regular Expression to use as seperator. Defaults to ",".

        Returns:
            list: List of list of Strings
        """
        array = [re.split(regex, x) for x in self.read_lines()]
        return array

    def split_line_re_int(self, regex=",") -> list:
        """Split all lines in the input using a regular expression and return them as integers

        Args:
            regex (str, optional): Regular Expression to use as seperator. Defaults to ",".

        Returns:
            list: List of list of Integers
        """
        array = self.split_line_re(regex)
        array = [list(map(int, x)) for x in array]
        return array

    def find_all_in_lines(self, regex=r"-?\d+") -> list:
        """Split all lines in the input file using a Regular Expression

        Args:
            regex (str, optional): The Regular Expression. Defaults to r"-?\d+" with finds all integers

        Returns:
            list: List of lists of strings
        """
        array = [re.findall(regex, x) for x in self.read_lines()]
        return array

    def find_all_ints_in_lines(self) -> list:
        """Find all the integers in the Input File by line.

        Returns:
            list: List of list of integers
        """
        array = self.find_all_in_lines()
        array = [[int(x) for x in y] for y in array]
        return array

    def read_graph_as_coordinates(self) -> dict:
        """Reads the input file of a 2D grid and returns a dictionary of the graph

        Returns:
            dict: Dictionary with characters as keys and values as a list of coordinates
                    Note: coordinates are (y,x)
        """
        graph = dict()
        for y, line in enumerate(self.lines):
            for x, chr in enumerate(line):
                graph[chr] = graph.get(chr, []) + [(y, x)]
        return graph

    def read_graph_as_values(self) -> dict:
        """Reads the input file of a 2D grid and returns a dictionary of the graph

        Returns:
            dict: Dictionary with coordinates as keys and values as the character in the grid
                    Note: coordinates are (y,x)
        """
        graph = dict()
        for y, line in enumerate(self.lines):
            for x, chr in enumerate(line):
                graph[(y, x)] = chr
        return graph


def addTuples(a: tuple, b: tuple) -> tuple:
    """Add two tuples together:
    e.g. (a,b) + (c,d) = (a+c, b+d)

    Args:
        a (tuple): Tuple 1
        b (tuple): Tuple 2

    Raises:
        TypeError: Tuples are not the same length

    Returns:
        tuple: Sum of the two tuples
    """

    if len(a) != len(b):
        raise TypeError("Tuple lenghts must be the same")

    temp = [a[i] + b[i] for i in range(len(a))]
    return tuple(temp)


def subtractTuples(a: tuple, b: tuple) -> tuple:
    """Subtract two tuples
    e.g. (a,b) - (c-d) = (a-c, b-d)

    Args:
        a (tuple): Tuple 1
        b (tuple): Tuple 2

    Raises:
        TypeError: Tuples are not the same length

    Returns:
        tuple: Difference between the two tuples.
    """

    if len(a) != len(b):
        raise TypeError("Tuple lenghts must be the same")

    temp = [a[i] - b[i] for i in range(len(a))]
    return tuple(temp)


def multiplyTuple(tup: tuple, multiplier: int) -> tuple:
    """Multiple a tuple by a mulitplier

    Args:
        tup (tuple): Tuple to apply the multiplier
        multiplier (int): Multiplier

    Returns:
        tuple: Resulting tuple
    """
    return tuple(x * multiplier for x in tup)


def manhattan_dist(a: tuple, b: tuple) -> int:
    """Get the manhattan distance between two points in a x,y coordinate system
        manhattan distance = | x1 - x2 | + | y1 - y2 |

    Args:
        a (tuple): Point 1 (x1, y1)
        b (tuple): Point 2 (x2, y2)

    Returns:
        int: Total manhattan distance
    """
    dist = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return dist


def insideGrid(pos, max, min=(0, 0)) -> bool:
    """Determine if a pos (x,y) is inside a grid

    Args:
        pos (tuple): Position to check (x,y)
        max (tuple): Maximum x and y values of the grid.
        min (tuple, optional): Minimum x and y values of the grid. Defaults to (0, 0).

    Returns:
        bool: True if pos is inside the Grid, else False
    """
    y, x = pos
    min_y, min_x = min
    max_y, max_x = max
    return min_y <= y < max_y and min_x <= x < max_x


def getMaxYMaxX(matrix: list) -> (int, int):
    """Get the maximum y and maximum x values of a 2x2 matrix"""
    y_max, x_max = len(matrix), len(matrix[0])
    return (y_max, x_max)


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
    """Provide a list of x,y coordinates as list of Tuples
    e.g. [(0,0), (1,1), (0,1), etc]
    Return the min (x,y) coordinate and the max (x,y) coordinate"""
    minx = min([x[0] for x in locs])
    miny = min([x[1] for x in locs])
    maxx = max([x[0] for x in locs])
    maxy = max([x[1] for x in locs])
    return (minx, miny), (maxx, maxy)


def increaseCountOfDict(dictionary: dict, key: any, count: int):
    """Increase the value of specified dictionary key by count. If the
        key does not exist, it will be created and the inital value will
        be set as count

    Args:
        dictionary (dict): dictionary to update
        key (any): key in the dictionary to update
        count (int): amount to increase the count
    """
    new_value = dictionary.get(key, 0) + count
    dictionary.update({key: new_value})


def main():
    day = datetime.now().day
    if day > 25:
        day = 25
    a = AOC(day, False)
    test = a.read_lines()
    print(test)


if __name__ == "__main__":
    main()
