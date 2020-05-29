from enum import Enum
class Pattern(Enum):
    SINGLExN = 1
    BOMB = 2
    BOMB_PLUS = 3
    Qx3 = 4
    Qx2 = 5
    Q = 6
    PLANE_SINGLE=7
    PLANE_PAIR=8

stateToPatternDict = {1: Pattern.SINGLExN, 5: Pattern.Q, 6: Pattern.SINGLExN, 10: Pattern.Qx2, 11: Pattern.SINGLExN,
                      12: Pattern.BOMB, 14: Pattern.BOMB_PLUS, 17: Pattern.BOMB_PLUS, 18:Pattern.PLANE_SINGLE, 19: Pattern.PLANE_PAIR,
                      20: Pattern.Qx3, 23:Pattern.PLANE_SINGLE, 24: Pattern.PLANE_PAIR, 25: Pattern.PLANE_SINGLE, 26: Pattern.PLANE_PAIR}
pathNext = {1:2,2:3,3:4,4:5,5:5,6:7,8:9,10:9,11:18,12:13,13:14,15:16,20:21,21:99,22:99}
pathEq = {1:6,7:8,9:10,6:11,11:12,13:15,16:17,18:19,19:20,21:22,22:20,23:24}
pathOther = {11:23,12:13,13:14,15:16,20:99,21:99,22:99}
finalState = {1,5,6,10,11,12,14,17,18,19,20,23,24,25,26}

class PokerStateMachine:
    def __init__(self):
        self.cardsValueList = []
        self.currentState = 1

    def setCardsValueList(self, cardsValueList):
        self.cardsValueList = cardsValueList

    def state99Handler(self):
        index = 0
        breakFlag = False
        
        for n in range(6):
            for i in range(2):
                index += 1
                if index == len(self.cardsValueList) or self.cardsValueList[index] != self.cardsValueList[index-1]:
                    breakFlag = True
                    break
            if(breakFlag):
                break
            index += 1
            
        print('3s', n)

        notTripleIndex = n*3

        if len(self.cardsValueList) == n*4:
            for i in range(n):
                if i == 0:
                    continue
                if self.cardsValueList[notTripleIndex+i] == self.cardsValueList[notTripleIndex+i-1]:
                    return None
            self.currentState = 25

        if len(self.cardsValueList) == n*5:
            for i in range(n):           
                if i%2 == 0:
                    continue
                if self.cardsValueList[notTripleIndex+i] != self.cardsValueList[notTripleIndex+i-1]:
                    return None
            self.currentState = 26
        
        return None

        
                    
    def getPattern(self):
        for index in range(len(self.cardsValueList)):
            if index == 0:
                continue
            if self.cardsValueList[index] == self.cardsValueList[index-1]:
                self.currentState = pathEq.get(self.currentState, 0)
            elif self.cardsValueList[index] == self.cardsValueList[index-1] + 1:
                self.currentState = pathNext.get(self.currentState, 0)
            else:
                self.currentState = pathOther.get(self.currentState, 0)

            #print(self.currentState)
            if(self.currentState == 99):
                self.state99Handler()
                break
            if(self.currentState == 0):
                break
            
        if self.currentState in finalState:
            return stateToPatternDict[self.currentState]
        else:
            return None

def patternOf(cards):
    machine = PokerStateMachine()
    machine.setCardsValueList(cards)
    return machine.getPattern()
            
                    
if __name__ == '__main__':
    p = patternOf([3,4,5,6,7])
    print(p)




    
