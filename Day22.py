#!/usr/local/bin/python3

deckSize = 10007
checkValue = 2019


class Deck:
    def __init__(self, sizeOfDeck):
        self.deck = list(range(sizeOfDeck))
        return

    # def size(self):
    #     return len(self.deck)

    def printDeck(self):
        print(self.deck)

    def reverseShuffle(self):
        print("Reversing Deck")
        self.deck.reverse()

    def cutN(self, n):
        print(f"Cutting Deck at {n}")
        if n > 0:
            x = n
        else:
            x = len(self.deck) + n
        tempCut = self.deck[0:x]
        tempCut2 = self.deck[x:]
        self.deck = tempCut2 + tempCut

    def incrementN(self, n):
        print(f"Dealing with Increment {n}")
        newDeck = list(range(len(self.deck)))
        pos = 0
        for i in range(len(self.deck)):
            newDeck[pos] = self.deck[i]
            pos += n
            if pos > len(self.deck):
                pos = pos - len(self.deck)
        self.deck = newDeck

    def findValue(self, value):
        return self.deck.index(value)


def main():
    deck = Deck(deckSize)
    r = open("Day22-Input.txt", "r")
    for line in r:
        if line[0:3] == "cut":
            n = int(line[4:])
            deck.cutN(n)
        elif line[0:9] == "deal into":
            deck.reverseShuffle()
        else:
            n = int(line[20:])
            deck.incrementN(n)
    # deck.printDeck()
    print(deck.findValue(checkValue))


if __name__ == "__main__":
    main()
