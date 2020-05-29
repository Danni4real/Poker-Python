import random
from pokerStateMachine import patternOf
from pokerStateMachine import Pattern

deck = []
lord = []
farmerA = []
farmerB = []
outLastRound = []
PatternLastRound = None
passCount = 0

pokerNames =  ('3','4','5','6','7','8','9','10','J','Q','K','A','2','B','R')
pokerValues = ( 0,  1,  2,  3,  4,  5,  6,  7,   8,  9,  10, 11, 100,200,300)

nameToValue = dict(zip(pokerNames, pokerValues))
valueToName = dict(zip(pokerValues, pokerNames))


def shuffleDeck():
    for i in range(3):
        for c in pokerValues:
            deck.append(c)
        deck.pop()
        deck.pop()

    for c in pokerValues:
        deck.append(c)

    random.shuffle(deck)

def deals(num):
    cards = []    
    for n in range(num):
        cards.append(deck.pop())
    cards.sort()
    return cards

def printCards(values):
    cards = []
    for v in values:
        cards.append(valueToName[v])
    print(''.join(cards))
    
def toCards(string):
    cards = []
    string = string.replace('10', 'T')
    cards = list(string)
    cards = ['10' if c=='T' else c for c in cards]
    for c in cards:
        if not c in pokerNames:
            return None
        
    cards = [nameToValue[c] for c in cards]
    return cards

def delCards(cards, subCards):
    cardsCopy = cards[:]
    
    for c in subCards:
        if c in cardsCopy:
            cardsCopy.remove(c)
        else:
            return False

    for c in subCards:
        cards.remove(c)
    return True
    

if __name__ == '__main__':
    shuffleDeck()
    farmerA = deals(17)
    farmerB = deals(17)
    lord = deals(20)

    activePlay = farmerA

    while True:
        printCards(activePlay)
        inputted = input()
        if not inputted:
            if passCount == 2:
                print('finish the shit you made!')
                continue
            else:
                passCount += 1
                #change player
                if activePlay == farmerA:
                    activePlay = farmerB
                elif activePlay == farmerB:
                    activePlay = lord
                elif activePlay == lord:
                    activePlay = farmerA
                continue
        if passCount == 2:
            outLastRound = []
            PatternLastRound = None
                
                     
        outCards = toCards(inputted)
        if not outCards:
            print('what you input are not poker cards!')
            continue

        pattern = patternOf(outCards)
        if not pattern:
            print('what you input dont have a pattern!')
            continue
        print(pattern)

        if PatternLastRound:
            if PatternLastRound == pattern and len(outLastRound) == len(outCards):
                if outLastRound[0] >= outCards[0]:
                    print('play bigger than last round!')
                    continue
            elif PatternLastRound != pattern and pattern == BOMB:
                pass
            else:
                print('play same pattern as last round or just bomb that mother fucker!')
                continue
        
        if not delCards(activePlay, outCards):
            print('no such cards in hand!')
            continue
        printCards(activePlay)

        passCount = 0
        outLastRound = outCards
        PatternLastRound = pattern
        
        #change player
        if activePlay == farmerA:
            activePlay = farmerB
        elif activePlay == farmerB:
            activePlay = lord
        elif activePlay == lord:
            activePlay = farmerA






    
