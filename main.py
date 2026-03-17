import deck
import poker
import card

def printHand(hand:list[card.Card]):
    print("Your hand is: ", end="")
    for i in range(len(hand)):
        if(i == len(hand)-1):
            print(hand[i])
        else:
            print(hand[i], end=", ")

def getHighestCard(hand:list[card.Card]):
    maxcard = hand[0]
    for i in range(len(hand)):
        if(hand[i].getVal() == 1):
            return hand[i]
        if(hand[i].getVal() > maxcard.getVal()):
            maxcard = hand[i]
    return maxcard


def main():
    pok = poker.Poker()
    currentDeck = deck.Deck()

    credits = 100
    cont = "Y"
    print(f"Current credits: {credits}")
 
    while cont != "N" and credits>0:
        bet = int(input("Enter bet (1-5): "))
        while bet not in [1,2,3,4,5] or bet > credits:
            print("Invalid bet")
            bet = int(input("Enter bet (1-5): "))
            
        currentDeck.shuffle()
        credits -= bet
        hand = []
        for i in range(5):
            hand.append(currentDeck.deal())
        
        printHand(hand)
        highestcard = getHighestCard(hand)
        print("Highest Card =", highestcard)
        if(highestcard.getVal() == 1 or highestcard.getVal() >= 11):
            mult = 1
        else:
            mult = 12 - highestcard.getVal()
        print("Current multiplier =", mult)

        holds = input("Enter holds: ")
        for i in range(len(holds)):
            if holds[i] != "1":
                hand[i] = currentDeck.deal()
        printHand(hand)
        winnings = bet * pok.bestHand(hand) * mult
        credits += winnings
        print(f"You've won {winnings}")
        print(f"Current credits: {credits}")
        cont = input("Continue (Y/N)?")
        


    return





if __name__ == "__main__":
    main()