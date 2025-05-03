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
        currentDeck = deck.getCards()

        for card in self.__hand:
            currentDeck.remove(card)

        avgrewards = []

        for move in self.moves:
            hand = self.__hand.copy()
            

        
        
        
        




if __name__ == "__main__":
    bot = pokerBot()
    currentDeck = deck.Deck()
    currentDeck.shuffle()
    hand = []
    for i in range(5):
        hand.append(currentDeck.deal())
        
    bot.setHand(hand)
    bot.move(currentDeck)



