from collections import deque
from copy import deepcopy

INITAL_LABEL = deque([2, 1, 9, 3, 4, 7, 8, 6, 5])
# INITAL_LABEL = deque([3, 8, 9, 1, 2, 5, 4, 6, 7])


def play_game(game, moves):
    for i in range(moves):
        if i % 1000 == 0:
            print(i)
        cup = game[0]
        game.rotate(-1)
        cups_removed = [game.popleft() for _ in range(1, 4)]
        destination = cup - 1
        while destination not in game:
            destination -= 1
            if destination <= 0:
                destination = max(game)
        insert_point = game.index(destination)
        for x in range(0, 3):
            game.insert(insert_point + x + 1, cups_removed[x])
    return game


def part1():

    game1 = deepcopy(INITAL_LABEL)
    game1 = play_game(game1, 100)

    # Score Game
    one_position = game1.index(1)
    game1.rotate(-1 * one_position)
    game1.popleft()
    final_answer = "".join([str(x) for x in game1])
    print(f"{final_answer}")


def part2():
    game2 = deepcopy(INITAL_LABEL) + deque(range(10, 1000001))
    # game2 = play_game(game2, 100)
    game2 = play_game(game2, 10000000)

    one_position = game2.index(1)
    game2.rotate(-1 * one_position)
    game2.popleft()
    cup1 = game2.popleft()
    cup2 = game2.popleft()
    print(cup1 * cup2)


# part1()
part2()