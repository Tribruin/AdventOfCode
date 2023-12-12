from timeit import timeit

# Test input
# DOOR_PUB_KEY = 17807724
# CARD_PUB_KEY = 5764801

# # Puzzle Input
DOOR_PUB_KEY = 12092626
CARD_PUB_KEY = 4707356


def one_loop(key, subject):
    return (key * subject) % 20201227


def part1():

    new_door_key = new_card_key = 1
    card_loop = door_loop = None
    i = 0
    while not (card_loop or door_loop):
        i += 1
        new_door_key = one_loop(new_door_key, 7)
        new_card_key = one_loop(new_card_key, 7)
        if new_card_key == CARD_PUB_KEY:
            card_loop = i

        elif new_door_key == DOOR_PUB_KEY:
            door_loop = i

    if not door_loop:
        loop = card_loop
        subject = DOOR_PUB_KEY
        values = ("Card", "Door")
    else:
        loop = door_loop
        subject = CARD_PUB_KEY
        values = ("Door", "Card")

    enc_key = pow(subject, loop, 20201227)
    print(f"Encryption Key: {enc_key} via {values[0]} PK / {values[1]} Loop")


print(timeit(part1, number=1))
