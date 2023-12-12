import re
import timeit

INPUT_FILE = "day4-Input.txt"
HCL_MATCH = "#[a-f0-9]{6}"
ECL_MATCH = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
RANGE_VALUES = {
    "byr": (1920, 2002),
    "iyr": (2010, 2020),
    "eyr": (2020, 2030),
    "cm": (150, 193),
    "in": (59, 76),
}


def read_file():
    """Read the input file and generate the list of passports

    Returns:
        List: A list of passport dictionaries
    """
    with open(INPUT_FILE) as f:
        lines = f.readlines()

    passport_split = []
    passport_data = []
    for line in lines:
        if line == "\n":
            passport_split.append(passport_data)
            passport_data = []
        else:
            line_split = line.split()
            passport_data += line_split

    passports = []
    for passport in passport_split:
        passport = {i.split(":")[0]: i.split(":")[1] for i in passport}
        passports.append(passport)

    return passports


def valid_passports_part1(passports):
    count = 0
    for passport in passports:
        if len(passport) == 8 or (len(passport) == 7 and "cid" not in passport.keys()):
            count += 1
    return count


def valid_passports_part2(passports):
    """Check for a valid passports in Part2 of the solutions

    Args:
        passports (List): passports is a list of dictionaries generated from the input file

    Returns:
        Int: Count of valid passports
    """

    def check_value_range(value, range):
        low, high = range
        if low <= value <= high:
            return True
        else:
            return False

    count = 0
    for passport in passports:
        valid = True
        if len(passport) == 8 or (len(passport) == 7 and "cid" not in passport.keys()):
            for key, value in passport.items():
                if key in RANGE_VALUES.keys():
                    if not check_value_range(int(value), RANGE_VALUES[key]):
                        valid = False
                        break
                elif key == "hgt":
                    hgt_m = value[-2:]
                    if hgt_m in ["cm", "in"]:
                        hgt_v = int(value[:-2])
                        if check_value_range(hgt_v, RANGE_VALUES[hgt_m]):
                            pass
                        else:
                            valid = False
                            break
                    else:
                        valid = False
                        break
                elif key == "hcl":
                    if not re.search(HCL_MATCH, value) != None:
                        valid = False
                        break
                elif key == "ecl":
                    if not value in ECL_MATCH:
                        valid = False
                        break
                elif key == "pid":
                    # if re.match("^[0-9]{9}$", value) == None:
                    if len(value) == 9:
                        valid = False
                        break
                else:  # key == "cid"
                    pass
        else:
            valid = False
        if valid:
            count += 1
    return count


def part1():
    print(valid_passports_part1(all_passports))


def part2():
    print(valid_passports_part2(all_passports))


all_passports = read_file()
print(timeit.timeit(part1, number=1))
print(timeit.timeit(part2, number=1))
