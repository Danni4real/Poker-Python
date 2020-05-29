import deck
from cards import strToCards


deck.newDeck()
john = deck.deals(17)
mary = deck.deals(17)
lord = deck.deals(20)

print(john)
print(mary)
print(lord)


inputString = input("play: ")

inputCards = strToCards(inputString)

if not inputCards:
    print("Err: input are not cards!")


