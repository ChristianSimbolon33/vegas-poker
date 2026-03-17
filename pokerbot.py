import poker
import deck
import card
import itertools

def printHand(hand:list[card.Card]): # type: ignore
    print("Your hand is: ", end="")
    for i in range(len(hand)):
        if(i == len(hand)-1):
            print(hand[i])
        else:
            print(hand[i], end=", ")

def generate_combination(a:list, n:int, prevarray:list=[]):
    if(len(prevarray) == n):
        return [prevarray]
    combs = []
    for i, val in enumerate(a):
        prevarrayextended = prevarray.copy()
        prevarrayextended.append(val)
        combs += generate_combination(a[i+1:], n, prevarrayextended)
    return combs

def getHighestCard(hand:list[card.Card]):
    maxcard = hand[0]
    for i in range(len(hand)):
        if(hand[i].getVal() == 1):
            return hand[i]
        if(hand[i].getVal() > maxcard.getVal()):
            maxcard = hand[i]
    return maxcard

class pokerBot():
    def __init__(self):
        self.__hand = []
        self.__pok = poker.Poker()
        self.moves = []
        self.mult = 1
        for i in range(32):
            self.moves.append(format(i, '05b'))

    def getHand(self):
        return self.__hand
    
    def setHand(self, hand:list[card.Card]):
        self.__hand = hand
    
    def getMult(self):
        highestcard = getHighestCard(self.__hand)
        if(highestcard.getVal() == 1 or highestcard.getVal() >= 11):
            self.mult = 1
        else:
            self.mult = 12 - highestcard.getVal()
        

    def move(self, deck:deck.Deck) -> str:
        currentDeck = deck.getCards()
        self.getMult()

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
                totRewards += (self.__pok.bestHand(hand) * self.mult)
            avgRewards.append(totRewards/len(combinations))

        index = 0
        max = 0
        for i, val in enumerate(avgRewards):
            if val > max:
                max = val
                index = i
        return self.moves[index]


if __name__ == "__main__":
    bot = pokerBot()
    currentDeck = deck.Deck()
    pok = poker.Poker()
    winnings = 0

    for index in range(10):
        currentDeck.shuffle()
        hand = []
        for i in range(5):
            hand.append(currentDeck.deal())      
        bot.setHand(hand)
        move = bot.move(currentDeck)
        for i in range(len(move)):
            if move[i] != "1":
                hand[i] = currentDeck.deal()

        highestcard = getHighestCard(hand)
        if(highestcard.getVal() == 1 or highestcard.getVal() >= 11):
            mult = 1
        else:
            mult = 12 - highestcard.getVal()
        winnings+=pok.bestHand(hand) * mult
    print(winnings/10.0)

    # for comb in itertools.combinations([1,2,3,4],3):
    #     print(comb)
    #print(generate_combination())



