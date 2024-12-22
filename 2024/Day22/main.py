from functools import cache
from AOC import AOC, getDateYear
from TerminalColors import *


testing = False


def parse_input(codeInput: AOC):
    result = [int(x) for x in codeInput.read_lines()]
    return result


def mix(value, secret_number):
    return value ^ secret_number


def prune(secret_number):
    return secret_number % 16777216


# @cache
def process_section(secret_number):
    # Step 1
    temp = secret_number * 64
    temp = mix(temp, secret_number)
    secret_number = prune(temp)

    # Step 2
    temp = secret_number // 32
    temp = mix(temp, secret_number)
    secret_number = prune(temp)

    # Step 3
    temp = secret_number * 2048
    temp = mix(temp, secret_number)
    secret_number = prune(temp)

    return secret_number


def part1(secret_numbers):
    final_value = 0
    for initial_secret in secret_numbers:
        secret_number = initial_secret
        for step in range(2000):
            secret_number = process_section(secret_number)
        final_value += secret_number
    print(final_value)


def part2(secret_numbers):
    all_sequences = dict()
    for initial_secret in secret_numbers:
        secret_number = process_section(initial_secret)
        prev_price = secret_number % 10
        current_sequence = list()
        current_sequences = dict()
        for _ in range(2000):
            secret_number = process_section(secret_number)
            new_price = secret_number % 10
            diff = new_price - prev_price
            current_sequence.append(diff)
            if len(current_sequence) > 4:
                current_sequence.pop(0)
            sequence_key = ",".join([str(x) for x in current_sequence])
            if (
                len(current_sequence) == 4
                and sequence_key not in current_sequences.keys()
            ):
                current_sequences[sequence_key] = new_price
            prev_price = new_price
        for sequence_key in current_sequences.keys():
            all_sequences[sequence_key] = (
                all_sequences.get(sequence_key, 0) + current_sequences[sequence_key]
            )
    print(max(list(all_sequences.values())))


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    dataInput = parse_input(codeInput)

    # part1(dataInput)
    part2(dataInput)


if __name__ == "__main__":
    main()
