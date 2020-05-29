from enum import Enum
from cards import Cards
from cards import strToCards
from collections import Counter

class CardsPattern(Enum):
    SIMPLE = 1
    BOMB = 2
    BOMB_PLUS = 3
    Q = 4
    Qx2 = 5
    Qx3 = 6


def rerangedCards(cards):
    cardsAfterRerange = Cards()
    
    for i in range(cards.size()):
        if(cards.count(cards[i]) == 4):
            cardsAfterRerange.add(cards[i])
                
    for i in range(cards.size()):
        if(cards.count(cards[i]) == 3):
            cardsAfterRerange.add(cards[i])

    for i in range(cards.size()):
        if(cards.count(cards[i]) == 2):
            cardsAfterRerange.add(cards[i])
    
    for i in range(cards.size()):
        if(cards.count(cards[i]) == 1):
            cardsAfterRerange.add(cards[i])   
    
    return cardsAfterRerange


def isSimple(cards):
    for i in range(cards.size()):
        if cards[0] != cards[i]:
            return None

    if cards.size() == 4:
        return CardsPattern.BOMB

    return CardsPattern.SIMPLE

def isBombPlus(cards):
    for i in range(4):
        if cards[0] != cards[i]:
            return None

    if cards.size() == 6:
        return CardsPattern.BOMB_PLUS

    if cards.size() == 8:
        if cards[4] == cards[5] and cards[6] == cards[7]:
            return CardsPattern.BOMB_PLUS

    return None
        
def isQ(cards):
    for i in range(cards.size()):
        if i == 0:
            continue
        if not cards[i].nextTo(cards[i-1]):
            return None       
    return CardsPattern.Q

def isQx2(cards):
    if cards.size()<6 or cards.size()%2!=0:
        return None
    
    for i in range(cards.size()):
        if i == 0:
            continue
        if i%2 == 0:
            if not cards[i].nextTo(cards[i-1]):
                return None
        if i%2 == 1:
            if not cards[i] == cards[i-1]:
                return None
            
    return CardsPattern.Qx2

def isQx3(cards):
    if cards.size()<6 or cards.size()%3!=0:
        return None
    
    for i in range(cards.size()):
        if i == 0:
            continue
        if i%3 == 0:
            if not cards[i].nextTo(cards[i-1]):
                return None
        if i%3 == 1:
            if not cards[i] == cards[i-1]:
                return None
            
    return CardsPattern.Qx3

def getPattern(cards):
    if isSimple(cards):
        return isSimple(cards)
    if isBombPlus(cards):
        return isBombPlus(cards)
    if isQ(cards):
        return isQ(cards)
    if isQx2(cards):
        return isQx2(cards)

if __name__ == '__main__':
    cards = strToCards('3')
    cards = rerangedCards(cards)
    print(getPattern(cards))
    cards = strToCards('33')
    cards = rerangedCards(cards)
    print(getPattern(cards))
    cards = strToCards('333')
    cards = rerangedCards(cards)
    print(getPattern(cards))
    cards = strToCards('3333')
    cards = rerangedCards(cards)
    print(getPattern(cards))
    cards = strToCards('333345')
    cards = rerangedCards(cards)
    print(getPattern(cards))
    cards = strToCards('33334455')
    cards = rerangedCards(cards)
    print(getPattern(cards))
    cards = strToCards('33334')
    cards = rerangedCards(cards)
    print(getPattern(cards))
    cards = strToCards('33334456')
    cards = rerangedCards(cards)
    print(getPattern(cards))
    cards = strToCards('345678')
    cards = rerangedCards(cards)
    print(getPattern(cards))
    cards = strToCards('34567810')
    cards = rerangedCards(cards)
    print(getPattern(cards))
    cards = strToCards('3344')
    cards = rerangedCards(cards)
    print(getPattern(cards))
    cards = strToCards('334455')
    cards = rerangedCards(cards)
    print(getPattern(cards))
