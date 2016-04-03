
class Card:
    def __init__(self, value, suit):
        self.value = CardValue(value)
        self.suit = Suit(suit)

    def __unicode__(self):
        return unicode(self.value) + unicode(self.suit)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __eq__(self, other):
        return (self.value == other.value) and \
               (self.suit == other.suit)


class CardValue:
    MAXCARDVALUE = 13
    MINCARDVALUE = 1
    ACE = 1
    JACK = 11
    QUEEN = 12
    KING = 13
    def __init__(self, value):
        self.value = value
        if self.value < self.MINCARDVALUE or self.value > self.MAXCARDVALUE:
            raise Exception('Improper card value')

    def __str__(self):
        strlist = [str(x) for x in range(2,11)]
        strlist = ['A'] + strlist + ['J', 'Q', 'K']
        return strlist[self.value-1]

    def __eq__(self, other):
        return self.value == other.value

class Suit:
    suites = ['hearts', 'diamonds', 'spades', 'clubs']
    colors = {'hearts':'red', 'diamonds':'red',
              'spades':'black','clubs':'black'}
    unicodes = {'hearts':u'\u2665', 'diamonds':u'\u2666',
                'spades':u'\u2660', 'clubs':u'\u2663'}

    def __init__(self, suit):
        self.suit = str.lower(suit)
        if self.suit not in self.suites:
            raise Exception('Invalid suit')

    @property
    def color(self):
        return self.colors[self.suit]

    @property
    def symbol(self):
        return unicode(self)

    def __unicode__(self):
        return self.unicodes[self.suit]

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __eq__(self, other):
        return self.suit == other.suit





