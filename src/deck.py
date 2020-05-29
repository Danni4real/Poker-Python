from card import Card
from cards import Cards
from constants import pokerNames

deck = Cards()

def newDeck():
    for i in range(4):
        for n in pokerNames:
            deck.add(Card(n))

    for i in range(3):
        deck.remove(Card('B'))
        deck.remove(Card('R'))
            
    deck.shuffle()
    

def deals(num):
    cards = Cards()

    for i in range(num):
        cards.add(deck.pop())

    cards.sort()
    return cards


if __name__ == '__main__':

    newDeck()
    print(deals(17))
    print(deals(17))
    print(deals(20))
