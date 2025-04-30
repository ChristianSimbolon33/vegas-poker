import card


class Poker():
    def __init__(self):
        pass

    def isFlush(self, hand:list[card.Card]):
        sortedHand = sorted(hand, key=lambda p: p.suit )
        if sortedHand[0].suit == sortedHand[-1].suit:
            return True
        return False
    
    def isStraight(self, hand:list[card.Card]):
        sortedHand = sorted(hand, key=lambda p: p.val )
        if(sortedHand[0].val == 1):
            if(sortedHand[1].val == 10 and sortedHand[2].val == 11 and sortedHand[3].val == 12 and sortedHand[4].val == 13):
                return True
            elif(sortedHand[1].val == 2 and sortedHand[2].val == 3 and sortedHand[3].val == 4 and sortedHand[4].val == 5):
                return True
            return False
        else:
            testRank = sortedHand[0].val + 1
            for i in range(1, 5):
                if sortedHand[i].val == testRank:
                    testRank+=1
                else:
                    return False
            return True

    def isStraightFlush(self, hand:list[card.Card]):
        return self.isFlush(hand) and self.isStraight(hand)
    
    def isRoyalFlush(self, hand:list[card.Card]):
        aceInHand = False
        kingInHand = False
        for i in range(len(hand)):
            if hand[i].val == 1:
                aceInHand = True
            if hand[i].val == 13:
                kingInHand = True
        return aceInHand and kingInHand and self.isFlush(hand) and self.isStraight(hand)



if __name__ == "__main__":
    hand = [card.Card(1, "spades"), card.Card(12, "spades"), card.Card(13, "spades"), card.Card(11, "spades"), card.Card(10, "spades")]
    pok = Poker()
    print(pok.isStraight(hand), pok.isFlush(hand), pok.isStraightFlush(hand), pok.isRoyalFlush(hand))