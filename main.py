import deck



def main():
    currentDeck = deck.Deck()
    currentDeck.shuffle()
    hand = []
    for i in range(5):
        hand.append(currentDeck.deal())
    
    for i in range(len(hand)):
        print(hand[i])

    return





if __name__ == "__main__":
    main()