import poker
import deck
import card


class pokerBot():
    def __init__(self):
        self.__hand = []
        self.__pok = poker.Poker()
        self.moves = []
        for i in range(32):
            self.moves.append(format(i, '05b'))


    def getHand(self):
        return self.__hand
    
    def setHand(self, hand:list[card.Card]):
        self.__hand = hand

    def move(self, deck:deck.Deck) -> str:
        currentDeck = deck
        
        for move in self.moves:



if __name__ == "__main__":
    print()



