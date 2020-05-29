import random
import constants
from card import Card

class Cards:
    def __init__(self):
        self.cards = []

    def __str__(self):
        cardsStr = []
        for c in self.cards:
            cardsStr.append(c.name)
        return ''.join(cardsStr)

    def __getitem__(self, index):
        return self.cards[index]

    def pop(self, index=-1):
        return self.cards.pop(index)

    def cardValue(card):
        return card.getValue()

    def size(self):
        return len(self.cards)

    def count(self, card):
        count = 0;
        for c in self.cards:
            if c == card:
                count += 1
        return count

    def sort(self):
        self.cards.sort(key = Cards.cardValue)

    def shuffle(self):
        random.shuffle(self.cards)
        
    def add(self, card):
        self.cards.append(card)
        
    def addAll(self, otherCards):
        self.cards.extend(otherCards.cards)

    def remove(self, card):
        self.cards.remove(card)
      
    def removeAll(self, subCards):
        for c in subCards.cards:
            self.cards.remove(c)

def strToCards(string):
    cardsString = string.replace('10', 'T')
    cardsList = list(cardsString)
    cardsList = ['10' if i == 'T' else i for i in cardsList]

    cards = Cards()
    
    for c in cardsList:
        if c in constants.pokerNames:
            cards.add(Card(c))
        else:
            return None

    cards.sort()
    return cards
    

if __name__ == '__main__':

    a = Card('3')
    b = Card('4')
    c = Card('5')
    d = Card('6')

    e = Card('7')
    f = Card('8')
    g = Card('9')
    h = Card('10')

    cs = Cards()
    cs.add(b)
    cs.add(a)
    cs.add(c)
    cs.add(d)
    print(cs)

    css = Cards()
    css.add(f)
    css.add(h)
    css.add(g)
    css.add(e)
    print(css)
    
    css.addAll(cs) 
    print(css)

    css.shuffle()
    print(css)

    css.removeAll(cs)
    print(css)

    cards = strToCards('10987654')
    print(cards)

    cards = strToCards('78899910101010')
    print(cards)

    print(cards.size())
    print(cards[6])

    print(cards.count(Card('7')))
    print(cards.count(Card('8')))
    print(cards.count(Card('9')))
    print(cards.count(Card('10')))
    

