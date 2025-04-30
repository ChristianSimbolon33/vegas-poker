import card
from enum import Enum
import random

class Suit(Enum):
    clubs: str = "clubs"
    hearts: str = "hearts"
    diamonds: str = "diamond"
    spades: str = "spades"


class Deck():
    def __init__(self):
        self.__cards = []
        self.deck = []
        self.__populateCards()

    def __populateCards(self):
        for i in range(13):
            for j in range(len(Suit._member_names_)):
                self.__cards.append(card.Card(i+1 ,Suit._member_names_[j]))

    def shuffle(self):
        self.deck.clear()
        while len(self.__cards) > 0:
            num = random.randint(0, len(self.__cards)-1)
            self.deck.append(self.__cards.pop(num))
        self.__populateCards()
        return
    
    def deal(self):
        return self.deck.pop()

    def getCards(self):
        return self.__cards
    
    def getDeck(self):
        return self.deck