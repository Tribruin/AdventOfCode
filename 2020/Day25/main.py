from timeit import timeit

# Test input
# DOOR_PUB_KEY = 17807724
# CARD_PUB_KEY = 5764801

# Puzzle Input
DOOR_PUB_KEY = 12092626
CARD_PUB_KEY = 4707356


def one_loop(key, subject):
    return (key * subject) % 20201227


def part1():

    new_door_key = 1
    new_card_key = 1
    card_loop = door_loop = None
    i = 0
    while not (card_loop and door_loop):
        i += 1
        new_door_key = one_loop(new_door_key, 7)
        new_card_key = one_loop(new_card_key, 7)
        # print(f"Loop: {i} - Door: {new_door_key} - Card: {new_card_key}")
        if new_card_key == CARD_PUB_KEY:
            card_loop = i

        elif new_door_key == DOOR_PUB_KEY:
            door_loop = i

    print(f"Found Card Loop: {card_loop} & Door Loop: {door_loop}")
    enc_key = 1
    for x in range(1, door_loop + 1):
        enc_key = one_loop(enc_key, CARD_PUB_KEY)
        # print(f"Loop: {x} - Encrytion Key: {enc_key}")
    print(f"Encryption Key: {enc_key} via Card PK / Door Loop")

    # enc_key = 1
    # for x in range(1, card_loop + 1):
    #     enc_key = one_loop(enc_key, DOOR_PUB_KEY)
    #     # print(f"Loop: {x} - Encrytion Key: {enc_key}")
    # print(f"Encryption Key: {enc_key} via Door PK / Card Loop")


print(timeit(part1, number=1))
