import random

class Card(object):
    """When you make an instance of Card, python runs the init block, so this block
    automatically gives an instance of Card a rank and a suit"""
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_value = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9,
         10:10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11 }
        self.value = self.rank_value[self.rank]

    """This makes the card readable, when you type print or use str()"""
    def __str__(self):
        return '%s of %s' % (self.rank, self.suit)

    """This also does that but differently, in every other context"""
    def __repr__(self):
        return self.__str__()

class Deck(object):
    rank_names = [2, 3, 4, 5, 6, 7, 8, 9, 'Ace', 'Jack', 'Queen', 'King']
    suit_names = ['Clubs', 'Spades', 'Diamonds', 'Hearts']

    def __init__(self):
        self.cards = []
        for suit in self.suit_names:
            for rank in self.rank_names:
                mycard = Card(rank, suit)
                self.cards.append(mycard)
        random.shuffle(self.cards)

class Hand(object):
    def __init__(self, deck):
        self.cards = []
        self.deck = deck

    def draw_hand(self):
        self.cards.append(self.deck.cards.pop(0))
        self.cards.append(self.deck.cards.pop(0))

    def hand_value(self):
        total_value = 0
        for card in self.cards:
            total_value += card.value
            if total_value > 21:
                print 'more than 21, so ur a LOSER!!!'
                return False
        return total_value

    def hit_card(self):
        self.new_hand= []
        self.new_hand.append(self.cards)
        self.cards.append(self.deck.cards.pop(0))
        return '%s' % (self.new_hand)

    def stay(self):
        self.cards = self.cards
        return self.cards

class Player(object):
    def __init__(self, deck):
        self.hands = [Hand(deck)]
        self.deck = deck

    '''def split(self):
        self.hands.append(Hand(self.deck))
        card = self.hands[0].cards.pop(0)
        self.hands[1].cards.appened(card)'''


class Dealer(object):
    pass


##Interphase section
answer = raw_input('Hello! Welcome to blackjack! Would you like to play? Yes (y) or no (n)')
if answer == 'n':
    print 'Wow OK ur a loser!!!!! hahahahhahahahahahhaa'
elif answer == 'y':

    mydeck = Deck()
    myhand = Hand(mydeck)
    myplayer = Player(mydeck)
    myhand.draw_hand()
    print 'good answer (sunglasses face emoji). Here are the two cards you have been dealt:'
    print myhand.cards
    print 'That makes your total value:' , myhand.hand_value()
    while myhand.hand_value() <= 21:
        hit_or_stay = raw_input('Would you like to hit (h) or stay (s)?')
        if hit_or_stay == 's':
            print 'Alright, so here is your final hand:', myhand.cards
            print 'That makes your total value:' , myhand.hand_value()
            break
        elif hit_or_stay == 'h':
            myhand.hit_card()
            print 'Oooohhh a daredevil... Alright. Your new hand is:' , myhand.cards
            print 'That makes your new total value:' , myhand.hand_value()
