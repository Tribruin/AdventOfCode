from collections import deque
from copy import deepcopy


def score_hand(cards):
    score = 0
    for pos, card in enumerate(cards[::-1]):
        score += (pos + 1) * card
    return score


def play_combat_game(deck1, deck2):
    i = 1
    while len(deck1) != 0 and len(deck2) != 0:
        print(f"\nRound: {i}")
        # print(cards1)
        # print(cards2)
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if card1 > card2:
            deck1 += [card1, card2]
        else:
            deck2 += [card2, card1]
        i += 1
    return deck1, deck2


def part1():
    deck1 = deepcopy(orig_cards1)
    deck2 = deepcopy(orig_cards2)
    deck1, deck2 = play_combat_game(deck1, deck2)

    if len(deck1) != 0:
        print(deck1)
        print(score_hand(deck1))
    else:
        print(deck2)
        print(score_hand(deck2))


def play_recursive_game(deck1, deck2, game):

    i = 1
    previous_hands = []
    while len(deck1) != 0 and len(deck2) != 0:
        print()
        print(f"-- Round {i} - Game {game} --")
        print(f"Player 1: {deck1}")
        print(f"Player 2: {deck2}")
        if (deck1, deck2) in previous_hands:
            print(
                f"Found Hands {(deck1, deck2)} at postion: {previous_hands.index((deck1, deck2))}"
            )
            return 1

        previous_hands += [(deepcopy(deck1), deepcopy(deck2))]
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if card1 <= len(deck1) and card2 <= len(deck2):
            winner = play_recursive_game(deck1[:card1], deck2[:card2], game + 1)
            if winner == 1:
                print(f"Player 1 Wins Sub-Game")
                deck1 += [card1, card2]
            else:
                print(f"Player 2 wins Sub-Game")
                deck2 += [card2, card1]
        elif card1 > card2:
            deck1 += [card1, card2]
            print(f"Player 1 Wins {card1} > {card2}")
        else:
            deck2 += [card2, card1]
            print(f"Player 2 Wins {card2} > {card1}")
        i += 1
    if len(deck1) > 0:
        return 1
    else:
        return 2


def part2():
    deck1 = deepcopy(orig_cards1)
    deck2 = deepcopy(orig_cards2)
    winner = play_recursive_game(deck1, deck2, 1)
    if winner == 1:
        print(score_hand(deck1))
    else:
        print(score_hand(deck2))


# orig_cards1 = [int(x) for x in "9,2,6,3,1".split(",")]
# orig_cards2 = [int(x) for x in "5,8,4,7,10".split(",")]
orig_cards1 = [
    int(x)
    for x in "42,29,12,40,47,26,11,39,41,13,8,50,44,33,5,27,10,25,17,1,28,22,6,32,35".split(
        ","
    )
]
orig_cards2 = [
    int(x)
    for x in "19,34,38,21,43,14,23,46,16,3,36,31,37,45,30,15,49,48,24,9,2,18,4,7,20".split(
        ","
    )
]
# part1()
part2()
