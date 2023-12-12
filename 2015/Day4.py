from hashlib import md5

# secretKey = "abcdef"
# secretKey = "pqrstuv"
secretKey = "iwrupvqb"


def generateHash(input):
    result = md5(input.encode())
    return result.hexdigest()


def part1():
    i = 0
    while True:
        code = secretKey + str(i)
        result = generateHash(code)
        if result[:5] == "00000":
            return str(i)
        i += 1
    return


def part2():

    i = 0
    while True:
        code = secretKey + str(i)
        result = generateHash(code)
        if result[:6] == "000000":
            return str(i)
        # if i % 1000 == 0:
            # print(f"Check in the {i} range")
        i += 1
    return


print(part1())
print(part2())
