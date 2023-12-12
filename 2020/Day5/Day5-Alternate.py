from timeit import timeit

test_value = "FBFBBFFRLR"


def read_file(input_file):
    with open(input_file) as f:
        return f.readlines()


def decode_boarding_pass(code):
    row_code, seat_code = code[:7], code[7:10]
    rows = 128
    row_low, row_high = 0, rows
    seats = 8
    seats_low, seats_high = 0, seats

    for letter in row_code:
        rows = rows // 2
        if letter == "F":
            row_high = row_low + rows
        else:
            row_low = row_high - rows

    for letter in seat_code:
        seats = seats // 2
        if letter == "L":
            seats_high = seats_low + seats
        else:
            seats_low = seats_high - seats
    # print(rows[0], seats[0])
    return row_low * 8 + seats_low


def part1():
    best_value = max(
        [decode_boarding_pass(boarding_pass) for boarding_pass in boarding_passes]
    )
    print(best_value)


def part2():
    seat_values = [
        decode_boarding_pass(boarding_pass) for boarding_pass in boarding_passes
    ]
    seat_values.sort()
    for i in range(1, len(seat_values) - 1):
        if (seat_values[i] == seat_values[i - 1] + 1) and (
            seat_values[i] == seat_values[i + 1] - 1
        ):
            pass
        else:
            print(seat_values[i] + 1)
            break
    # print(seat_values)


boarding_passes = read_file("Day5-Input.txt")
print(timeit(part1, number=1))
print(timeit(part2, number=1))