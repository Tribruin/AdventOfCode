import re
import timeit

INPUT_FILE = "day4-Input.txt"
HCL_MATCH = "#[a-f0-9]{6}"
ECL_MATCH = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def read_file():
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
    count = 0
    for passport in passports:
        valid = True
        if len(passport) == 8 or (len(passport) == 7 and "cid" not in passport.keys()):
            for key, value in passport.items():
                if key == "byr":
                    if 1920 <= int(value) <= 2002:
                        pass
                    else:
                        valid = False
                        break
                elif key == "iyr":
                    if 2010 <= int(value) <= 2020:
                        pass
                    else:
                        valid = False
                        break
                elif key == "eyr":
                    if 2020 <= int(value) <= 2030:
                        pass
                    else:
                        valid = False
                        break
                elif key == "hgt":
                    hgt_m = value[-2:]
                    try:
                        hgt_v = int(value[:-2])
                    except ValueError:
                        hgt_v = 0
                    if (hgt_m == "cm" and (150 <= hgt_v <= 193)) or (
                        hgt_m == "in" and (59 <= hgt_v <= 76)
                    ):
                        pass
                    else:
                        valid = False
                        break
                elif key == "hcl":
                    if re.search(HCL_MATCH, value) != None:
                        pass
                    else:
                        valid = False
                        break
                elif key == "ecl":
                    if value in ECL_MATCH:
                        pass
                    else:
                        valid = False
                        break
                elif key == "pid":
                    if len(value) == 9:
                        pass
                    else:
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
