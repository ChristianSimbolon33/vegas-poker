import poker
import deck
import card
import itertools

def generate_combination(a:list, n:int, prevarray:list=[]):
    if(len(prevarray) == n):
        return [prevarray]
    combs = []
    for i, val in enumerate(a):
        prevarrayextended = prevarray.copy()
        prevarrayextended.append(val)
        combs += generate_combination(a[i+1:], n, prevarrayextended)
    return combs


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

        avgRewards = []
        seenHands = []


        for move in self.moves:
            hand = self.__hand.copy()
            numOfReplacements = 0

            for i in range(len(move)):
                if(move[i] == "0"):
                    numOfReplacements +=1
            
            totRewards = 0
            combinations = generate_combination(currentDeck, numOfReplacements)
            for comb in combinations:
                j = 0
                for i, val in enumerate(move):
                    if(val == "0"):
                        hand[i] = comb[j]
                        j += 1
                totRewards += self.__pok.bestHand(hand)
            avgRewards.append(totRewards/len(combinations))

        index = 0
        max = 0
        for i in range(len(avgRewards)):
            print((self.moves[i], avgRewards[i]))
        for i, val in enumerate(avgRewards):
            if val > max:
                max = val
                index = i
        return self.moves[index]


if __name__ == "__main__":
    bot = pokerBot()
    currentDeck = deck.Deck()
    currentDeck.shuffle()
    hand = []
    for i in range(5):
        hand.append(currentDeck.deal())
        
    bot.setHand(hand)
    for card in bot.getHand():
        print(card)
    print(bot.move(currentDeck))

    # for comb in itertools.combinations([1,2,3,4],3):
    #     print(comb)
    #print(generate_combination())



