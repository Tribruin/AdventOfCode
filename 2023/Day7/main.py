from AOC import AOC, getDateYear
from TerminalColors import *


testing = False
cardRanks_1 = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

cardRanks_2 = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def parse_input(codeInput: AOC):
    hands = codeInput.split_lines(" ")
    result = list()
    for hand in hands:
        cards = [x for x in hand[0]]
        bid = int(hand[1])
        result.append((cards, bid))
    return result


def scoreHand(cards: list):
    cardSet = set(cards)
    cardMatch = [cards.count(x) for x in cardSet]
    match (len(cardSet), max(cardMatch)):
        case (1, 5):
            # print(f"{cards} - Five of a Kind")
            return 7
        case (2, 4):
            # if 4 in cardMatch:
            # print(f"{cards} - Foun of a Kind")
            return 6
        case (2, 3):
            # print(f"{cards} - Full House")
            return 5
        case (3, 3):
            # if 3 in cardMatch:
            # print(f"{cards} - Three of a Kind")
            return 4
        case (3, 2):
            # print(f"{cards} - Two Pair")
            return 3
        case (4, 2):
            # print(f"{cards} - One Pair")
            return 2
        case (5, 1):
            # print(f"{cards} - High Card")
            return 1


def compareHands(hand1, hand2, cardRanks):
    # for x in range(len(hand1)):
    for card1, card2 in zip(hand1, hand2):
        if cardRanks[card1] < cardRanks[card2]:
            # Cards are sorted
            return True
        elif cardRanks[card1] > cardRanks[card2]:
            # cards are not sorted
            return False
    # If hands are equal, don't resort
    return True


def rankHandResults(hands, cardRanks):
    rankedHands = hands
    validSort = False
    while not validSort:
        validSort = True
        for k in range(len(rankedHands) - 1):
            cards1, cards2 = rankedHands[k][0], rankedHands[k + 1][0]
            if not compareHands(cards1, cards2, cardRanks):
                rankedHands[k], rankedHands[k + 1] = rankedHands[k + 1], rankedHands[k]
                validSort = False

    return rankedHands


def part1(hands):
    def calculateValue(hand):
        handResult = str(scoreHand(hand))
        for card in hand:
            handResult += f"{cardRanks_1[card]:02}"
        # print(handResult)
        return int(handResult)

    handResults = list()

    for hand in hands:
        handScore = calculateValue(hand[0])
        handResults.append({"score": handScore, "cards": hand[0], "bid": hand[1]})
        # print(handScore, hand[0])

    sortedHandResults = sorted(handResults, key=lambda x: x["score"])
    # print(sortedHandResults)
    score = 0
    for count, hand in enumerate(sortedHandResults):
        # print(count + 1, hand["bid"], (count + 1) * hand["bid"])
        score += (count + 1) * hand["bid"]

    print(score)


def part2(hands):
    def calculateValue(origHand, subbedHand):
        handResult = str(scoreHand(subbedHand))
        for card in origHand:
            handResult += f"{cardRanks_2[card]:02}"
        # print(handResult)
        return int(handResult)

    def getBestHandWithJoker(hand: list):
        handCards = list(set(hand))
        bestHand = 0
        bestHardCards = []
        if hand == ["J"] * 5:
            bestHand = calculateValue(hand, hand)
            bestHardCards = hand

        else:
            handCards.pop(handCards.index("J"))
            for card in handCards:
                testHand = [x if x != "J" else card for x in hand]
                handValue = calculateValue(hand, testHand)
                if handValue > bestHand:
                    bestHand = handValue
                    bestHardCards = testHand
        # print(bestHand, hand, sorted(bestHardCards))
        return bestHand

    handResults = list()
    for hand in hands:
        if "J" in hand[0]:
            handScore = getBestHandWithJoker(hand[0])
        else:
            handScore = calculateValue(hand[0], hand[0])
        handResults.append({"score": handScore, "cards": hand[0], "bid": hand[1]})
        # print(handScore, hand[0])

    sortedHandResults = sorted(handResults, key=lambda x: x["score"])
    # print(sortedHandResults)
    score = 0
    for count, hand in enumerate(sortedHandResults):
        # print(count + 1, hand["bid"], (count + 1) * hand["bid"])
        score += (count + 1) * hand["bid"]

    print(score)


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
