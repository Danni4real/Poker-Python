from constants import getCardValue

class Card:
    def __init__(self, name):
        self.name = name
        self.value = getCardValue(name)
        
    def __str__(self):
        return self.name
    
    def __gt__(self, otherCard):
        return self.value > otherCard.value
    
    def __lt__(self, otherCard):
        return self.value < otherCard.value
    
    def __eq__(self, otherCard):
        return self.value == otherCard.value

    def getValue(self):
        return self.value

    def nextTo(self, otherCard):
        if self.value - otherCard.value == 1:
            return True
        return False



if __name__ == '__main__':

    three = Card('3')
    four = Card('4')

    print(four.nextTo(three))
