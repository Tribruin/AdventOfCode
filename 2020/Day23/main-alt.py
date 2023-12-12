INITAL_LABEL = [2, 1, 9, 3, 4, 7, 8, 6, 5]
# INITAL_LABEL = [3, 8, 9, 1, 2, 5, 4, 6, 7]


class Cup:
    def __init__(self, number):
        self.number = number
        self.next = None

    def insert(self, cards):
        pass


def printCups(currentCup, cups, move):
    cupToPrint = cups[INITAL_LABEL[0]]
    print()
    print("Cups: ", end="")
    for i in range(len(cups)):
        if cupToPrint == currentCup:
            print(f" ({cupToPrint.number})", end="")
        else:
            print(f"  {cupToPrint.number} ", end="")
        cupToPrint = cupToPrint.next
    print()


def play_game(start, cups, moves):

    max_value = len(cups)
    destination = start.number - 1
    for i in range(moves):
        if i % 1000 == 0:
            print(f"Move {i+1:3} - ")
        # printCups(start, cups, i + 1)
        # Get next three cards
        cup1 = start.next
        cup2 = cup1.next
        cup3 = cup2.next
        start.next = cup3.next
        # print(f"pick up: {cup1.number}, {cup2.number}, {cup3.number}")

        cup_values = [cup1.number, cup2.number, cup3.number]
        if destination < 1:
            destination = max_value
        while destination in cup_values:
            destination -= 1
            if destination < 1:
                destination = max_value

        # print(f"destination: {destination}")
        next_cup = cups[destination].next
        cups[destination].next = cup1
        cup1.next = cup2
        cup2.next = cup3
        cup3.next = next_cup
        start = start.next
        destination = start.number - 1

    return cups


def part1():

    cups = dict()
    cups[INITAL_LABEL[0]] = startingCard = previousCard = Cup(INITAL_LABEL[0])

    for number in INITAL_LABEL[1:]:
        cups[number] = Cup(number)
        previousCard.next = cups[number]
        previousCard = cups[number]
    previousCard.next = startingCard

    cups = play_game(startingCard, cups, 100)

    # Score Game
    final_value = list()
    startingCard = cups[1]
    for i in range(len(cups) - 1):
        final_value.append(startingCard.next.number)
        startingCard = startingCard.next
    print(final_value)


def part2():
    cups = dict()
    max_number = max(INITAL_LABEL)
    cups[INITAL_LABEL[0]] = startingCard = previousCard = Cup(INITAL_LABEL[0])

    for number in INITAL_LABEL[1:]:
        cups[number] = Cup(number)
        previousCard.next = cups[number]
        previousCard = cups[number]

    for number in range(max_number + 1, 1000001):
        cups[number] = Cup(number)
        previousCard.next = cups[number]
        previousCard = cups[number]

    previousCard.next = startingCard

    cups = play_game(startingCard, cups, 10000000)

    # Score Game
    startingCard = cups[1]
    print(startingCard.next.number * startingCard.next.next.number)


# part1()
part2()