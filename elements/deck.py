from card import Card, Suit, CardValue
from random import shuffle


#
# General top class that represents a sequence of cards
#
class CardSequence(object):
    def __init__(self, cards=[]):
        self.cards = cards

    @property
    def numcards(self):
        return len(self.cards)

    def addcard(self,card):
        self.cards.append(card)

    def dealcard(self, numcards=1):
        # Get the list of cards
        deltcards = self.cards[-numcards:]

        # Remove them from the list
        self.cards = [i for i in self.cards if i not in deltcards]
        return deltcards

    def __unicode__(self):
        output = unicode()
        for i,card in enumerate(self.cards):
            output = output + unicode(card)
            if (i+1) < self.numcards:
                output = output + ','
        return output

    def __str__(self):
        return unicode(self).encode('utf-8')

#
# Card sequence containing all 52 cards and shuffled
#

class Deck(CardSequence):
    def __init__(self):
        super(Deck, self).__init__()
        for value in range(CardValue.MINCARDVALUE,CardValue.MAXCARDVALUE+1):
            for suit in Suit.suites:
                self.cards.append(Card(value, suit))
        shuffle(self.cards)



#
# Stacks represent a group of cards that can be added on top of
# In general they must accept a card to be added and decide if it is legal
# or not to add it. They must also provide the cards in the same order as added
#

class Stack(CardSequence):
    def __init__(self):
        self.cards = []

    @property
    def empty(self):
        return len(self.cards) == 0

    def dealcard(self, numcards=1):
        # stacks can never deal multiple cards
        pass

    def gettopcard(self):
        return self.cards.pop()

    def addcard(self, card):
        if self._legal(card):
            self.cards.append(card)
            return True
        else:
            return False

    def _legal(self, card):
        return True

#
# Stack which accepts a card of value-1 and opposite color
#
class AltStack(Stack):
    def __init__(self):
        super(AltStack, self).__init__()

    def _legal(self, card):
        if self.empty:
            valuecrit = card.value != CardValue.ACE
            colorcrit = True
        else:
            topcard = self.cards[-1]
            valuecrit = card.value == topcard.value-1 and \
                        card.value != CardValue.ACE
            colorcrit = card.suit.color != topcard.suit.color

        return True if valuecrit and colorcrit else False

#
# Stack for which the first card must be an ace and then after
# that a card must be value+1 and same suit
#

class AceStack(Stack):
    def __init__(self, suit):
        super(AceStack, self).__init__()
        self.suit = Suit(suit)

    def gettopcard(self):
        # cannot remove cards from ace stack once they are added
        pass

    def _legal(self, card):
        if self.empty:
            valuecrit = card.value == CardValue.ACE
        else:
            topcard = self.cards[-1]
            valuecrit = card.value == topcard.value + 1
        suitcrit = card.suit == self.suit

        return True if valuecrit and suitcrit else False


#
# Same suit stack but doesn't have to start with an ace.
# Will be used for trash + small piles
#
class SuitStack(Stack):
    def __init__(self):
        super(SuitStack, self).__init__()

    def _legal(self, card):
        if self.empty:
            return True
        else:
            topcard = self.cards[-1]
            valuecrit = card.value == topcard.value + 1
            suitcrit = card.suit == topcard.suit
            return True if valuecrit and suitcrit else False
