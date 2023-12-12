from timeit import timeit

test_value = "FBFBBFFRLR"


def read_file(input_file):
    with open(input_file) as f:
        return f.readlines()


def decode_boarding_pass(code):
    row_code, seat_code = code[:7], code[7:10]
    rows = range(128)
    seats = range(8)

    for letter in row_code:
        if letter == "F":
            rows = rows[0 : len(rows) // 2]

        else:
            rows = rows[len(rows) // 2 : len(rows)]

    for letter in seat_code:
        if letter == "L":
            seats = seats[0 : len(seats) // 2]

        else:
            seats = seats[len(seats) // 2 : len(seats)]
    # print(rows[0], seats[0])
    return rows[0], seats[0]


def part1():
    best_value, best_s, best_r = 0, 0, 0
    for boarding_pass in boarding_passes:
        r, s = decode_boarding_pass(boarding_pass)
        value = 8 * r + s
        if value > best_value:
            best_value, best_r, best_s = value, r, s
    print(best_value, best_r, best_s)


def part2():
    seat_values = [i for i in range(8 * 128)]
    # found_seat_values = []
    for boarding_pass in boarding_passes:
        r, s = decode_boarding_pass(boarding_pass)
        value = 8 * r + s
        seat_values.remove(value)
    for i in range(1, len(seat_values) - 1):
        if (seat_values[i] == seat_values[i - 1] + 1) or (
            seat_values[i] == seat_values[i + 1] - 1
        ):
            pass
        else:
            print(seat_values[i])
    # print(seat_values)


boarding_passes = read_file("Day5-Input.txt")
print(timeit(part1, number=1))
print(timeit(part2, number=1))