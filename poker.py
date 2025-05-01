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
    
    def is4s(self, hand:list[card.Card]):
        sortedHand = sorted(hand, key=lambda p: p.val )
        low4s = (sortedHand[0].val == sortedHand[1].val == sortedHand[2].val == sortedHand[3].val)
        high4s = (sortedHand[1].val == sortedHand[2].val == sortedHand[3].val == sortedHand[4].val)
        return low4s or high4s

    def isFullHouse(self, hand:list[card.Card]):
        sortedHand = sorted(hand, key=lambda p: p.val )
        lowFullHouse = (sortedHand[0].val == sortedHand[1].val == sortedHand[2].val and sortedHand[3].val == sortedHand[4].val)
        highFullHouse = (sortedHand[4].val == sortedHand[3].val == sortedHand[2].val and sortedHand[1].val == sortedHand[0].val)
        return lowFullHouse or highFullHouse
    
    def is3s(self, hand:list[card.Card]):
        if (self.is4s(hand) or self.isFullHouse(hand)):
            return False
        sortedHand = sorted(hand, key=lambda p: p.val )
        low3s = (sortedHand[0].val == sortedHand[1].val == sortedHand[2].val)
        middle3s = (sortedHand[1].val == sortedHand[2].val == sortedHand[3].val)
        high3s = (sortedHand[2].val == sortedHand[3].val == sortedHand[4].val)
        return low3s or middle3s or high3s
    
    def is2Pair(self, hand:list[card.Card]):
        if(self.is4s(hand) or self.isFullHouse(hand) or self.is3s(hand)):
            return False
        sortedHand = sorted(hand, key=lambda p: p.val )
        lowPairs = (sortedHand[0].val == sortedHand[1].val and sortedHand[2] == sortedHand[3])
        splitPairs = (sortedHand[0].val == sortedHand[1].val and sortedHand[3] == sortedHand[4])
        highPairs = (sortedHand[1].val == sortedHand[2].val and sortedHand[3] == sortedHand[4])
        return lowPairs or splitPairs or highPairs
    
    def is2s(self, hand:list[card.Card]):
        if(self.is4s(hand) or self.isFullHouse(hand) or self.is3s(hand) or self.is2Pair(hand)):
            return False
        sortedHand = sorted(hand, key=lambda p: p.val )
        lowPair = (sortedHand[0].val == sortedHand[1].val)
        lowMidPair = (sortedHand[1].val == sortedHand[2].val)
        highMidPair = (sortedHand[2].val == sortedHand[3].val)
        highPair = (sortedHand[3].val == sortedHand[4].val)
        return lowPair or lowMidPair or highMidPair or highPair




if __name__ == "__main__":
    hand = [card.Card(10, "spades"), card.Card(1, "spades"), card.Card(10, "spades"), card.Card(10, "spades"), card.Card(2, "spades")]
    pok = Poker()
    #print(pok.isStraight(hand), pok.isFlush(hand), pok.isStraightFlush(hand), pok.isRoyalFlush(hand))
    print(pok.is3s(hand))