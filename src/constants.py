pokerNames =  ('3','4','5','6','7','8','9','10','J','Q','K','A','2','B','R')
pokerValues = ( 0,  1,  2,  3,  4,  5,  6,  7,   8,  9,  10, 11, 100,200,300)

pokerDict = dict(zip(pokerNames, pokerValues))


def getCardValue(name):
    return pokerDict[name]



if __name__ == '__main__':

    print(getCardValue('3'))
    print(getCardValue('4'))
    print(getCardValue('5'))
    print(getCardValue('6'))
    print(getCardValue('7'))
    print(getCardValue('8'))
    print(getCardValue('9'))
    print(getCardValue('10'))
    print(getCardValue('J'))
    print(getCardValue('Q'))
    print(getCardValue('K'))
    print(getCardValue('A'))
    print(getCardValue('2'))
    print(getCardValue('B'))
    print(getCardValue('R'))
