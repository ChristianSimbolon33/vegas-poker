import card


class Poker():
    def __init__(self):
        self.winnings = [250, 50, 160, 80, 50, 10, 7, 5, 3, 1, 1]

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
    
    def bestHand(self, hand:list[card.Card]):
        sortedHand = sorted(hand, key=lambda p: p.val)
        low4s = [2, 3, 4]
        if(self.isRoyalFlush(hand)):
            return self.winnings[0]
        elif(self.isStraightFlush(hand)):
            return self.winnings[1]
        elif(self.is4s(hand)):
            if (sortedHand[2].val == 1):
                return self.winnings[2]
            elif (sortedHand[2].val in low4s):
                return self.winnings[3]
            else:
                return self.winnings[4]
        elif(self.isFullHouse(hand)):
            return self.winnings[5]
        elif(self.isFlush(hand)):
            return self.winnings[6]
        elif(self.isStraight(hand)):
            return self.winnings[7]
        elif(self.is3s(hand)):
            return self.winnings[8]
        elif(self.is2Pair(hand)):
            return self.winnings[9]
        elif(self.is2s(hand)):
            lowPair = (sortedHand[0].val == sortedHand[1].val)
            lowMidPair = (sortedHand[1].val == sortedHand[2].val)
            highMidPair = (sortedHand[2].val == sortedHand[3].val)
            highPair = (sortedHand[3].val == sortedHand[4].val)
            if(lowPair and (sortedHand[0].val > 10 or sortedHand == 1)):
                return self.winnings[10]
            elif(lowMidPair and sortedHand[1].val > 10 ):
                return self.winnings[10]
            elif(highMidPair and sortedHand[2].val > 10 ):
                return self.winnings[10]
            elif(highPair and sortedHand[3].val > 10 ):
                return self.winnings[10]
        return 0







if __name__ == "__main__":
    hand = [card.Card(7, "clubs"), card.Card(9, "hearts"), card.Card(8, "hearts"), card.Card(9, "clubs"), card.Card(1, "spades")]
    pok = Poker()
    print(pok.bestHand(hand))