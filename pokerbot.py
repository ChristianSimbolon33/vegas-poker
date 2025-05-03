import poker
import deck
import card
import itertools

# def generate_combination(a:list, n:int, prevarray:list=[]):
#     if(len(prevarray) == n):
#         return [prevarray]
#     combs = []
#     for i, val in enumerate(a):
#         prevarrayextended = prevarray.copy()
#         prevarrayextended.append(val)
#         combs += generate_combination(a[i+1:], n, prevarrayextended)
#     return combs


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
        seenhands = []

        for move in self.moves:
            hand = self.__hand.copy()
            for i in range(len(move)):
                if(move[i] == "0"):
                    for card in currentDeck:
                        hand[i] = card

        
        
        
        




if __name__ == "__main__":
    bot = pokerBot()
    currentDeck = deck.Deck()
    currentDeck.shuffle()
    hand = []
    for i in range(5):
        hand.append(currentDeck.deal())
        
    bot.setHand(hand)
    bot.move(currentDeck)

    for comb in itertools.combinations([1,2,3,4],3):
        print(comb)
    #print(generate_combination())



