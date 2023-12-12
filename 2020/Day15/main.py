class Number:
    def __init__(self, number, last_spoken) -> None:

        self.number = number
        self.previous_spoken = None
        self.last_spoken = last_spoken

    def update(self, postion):
        self.previous_spoken = self.last_spoken
        self.last_spoken = postion


def find_last(array, check):
    for n, i in enumerate(array[::-1]):
        if i == check:
            return n


def play_game(count):
    words_spoke = input.split(",")
    for i in range(len(words_spoke), count):
        if (i % 1000) == 0:
            print(i)
        last_word = words_spoke[-1]
        if last_word not in words_spoke[:-1]:
            words_spoke.append("0")
        else:
            last_spoken = find_last(words_spoke[:-1], words_spoke[-1])
            words_spoke.append(str(last_spoken + 1))
    print(words_spoke[-1])


def play_game_alt(count):
    all_numbers = {}
    words_spoke = [int(x) for x in input.split(",")]
    for n, number in enumerate(words_spoke):
        all_numbers[number] = Number(number, n + 1)

    last_number = words_spoke[-1]
    for x in range(len(words_spoke), count):
        last_postion = all_numbers.get(last_number, None)

        if last_postion.previous_spoken == None:
            new_number = 0
            all_numbers[0].update(x + 1)
            last_number = 0

        else:
            new_number = last_postion.last_spoken - last_postion.previous_spoken
            if all_numbers.get(new_number, None) == None:
                all_numbers[new_number] = Number(new_number, x + 1)
            else:
                all_numbers[new_number].update(x + 1)
            last_number = new_number

        # print(f"Round: {x} - Next Number: {last_number}")
    print(new_number)


# a = AOC({{INT}}), test=True)
# input = "0,3,6"
input = "9,19,1,6,0,5,4"
# play_game_alt(2020)
play_game_alt(30000000)
