


class Card():
    def __init__(self, value, suit):
        self.val = value
        self.suit = suit
        self.name = ""
        if self.val == 1:
            self.name = "Ace"
        elif self.val == 11:
            self.name = "Jack"
        elif self.val == 12:
            self.name = "Queen"
        elif self.val == 13:
            self.name = "King"
        else:
            self.name = str(self.val)

    def getVal(self):
        return self.val
    
    def getSuit(self):
        return self.suit
    
    def __str__(self):
        return self.name + " of " + self.suit
    
    def __eq__(self, value):
        if(type(value) != Card):
            return False
        return (value.val == self.val and value.suit == self.suit)