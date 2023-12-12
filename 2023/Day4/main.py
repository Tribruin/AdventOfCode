from AOC import AOC, getDateYear
from TerminalColors import *

testing = False


def parse_input(codeInput: AOC):
    cards = codeInput.split_line_re("[\|\:]")
    result = [(x[0].split()[1], list(x[1].split()), list(x[2].split())) for x in cards]
    return result


def part1(cards):
    total = 0
    for card in cards:
        winning_nums = set(card[1])
        my_nums = set(card[2])
        matches = winning_nums.intersection(my_nums)
        if len(matches) > 0:
            total += 2 ** (len(matches) - 1)
            # print(f"Card # {card[0]} - {2 ** (len(matches) - 1)}")
        else:
            pass
            # print(f"Card {card[0]} - No Points")
    print(total)


def part2(cards):
    totalCards = [1] * len(cards)
    for cardNum, card in enumerate(cards):
        winning_nums = set(card[1])
        my_nums = set(card[2])
        matches = len(winning_nums.intersection(my_nums))
        if matches > 0:
            for i in range(cardNum + 1, cardNum + 1 + matches):
                totalCards[i] += totalCards[cardNum]
            # winning_points_on_card = 2 ** (matches - 1)
            # winning_points = winning_points_on_card * totalCards[cardNum]
        # print(f"Card # {card[0]} - Total Cards {totalCards[cardNum]}")

    print(sum(totalCards))


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    dataInput = parse_input(codeInput)

    part1(dataInput)
    part2(dataInput)


if __name__ == "__main__":
    main()
