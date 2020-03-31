# Mini-project #6 - Blackjack developed by Sidhant JAIN as 
# a mini-project part of IIPP-2 course on Coursera 

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = "Hit or Stand?"
player_score = 0
dealer_score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        str_card = ""
        for card in self.cards:
            str_card += " " + card.__str__()
            
        return "Hand contains" + str_card
    
    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    # compute the value of the hand, see Blackjack video
        value = 0
        contains_ace = False
    
        for card in self.cards:
            rank = card.get_rank()
            value += VALUES[rank]
            
            if(rank == 'A'):
                contains_ace = True
            
        if(value < 11 and contains_ace):
            value += 10
             
        return value
                    
        
    def draw(self, canvas, pos):
        for card in self.cards:
            card.draw(canvas,pos)
            pos[0] += 80
        
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal_card(self):
        return self.cards.pop(0)



#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, player_score, dealer_score

    if(in_play == True):
        outcome = "You hit deal twice! New deal?"
        dealer_score = 0
        player_score = 0
        in_play = False   
    else:
        deck = Deck()
        outcome = "New deal! Hit or Stand?"
        deck.shuffle()
    
        player_hand = Hand()
        dealer_hand = Hand()
    
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
    
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
    
        print "Player: %s" % player_hand
        print "Dealer: %s" % dealer_hand
    
        in_play = True

def hit():
    global outcome, in_play
    
    if in_play:
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())
        
        print "Player's hand %s"  % player_hand
        
        if player_hand.get_value() > 21:
            outcome = "You have busted! New Deal?"
            in_play = False
            print "You have busted"
            
def stand():
    global outcome, player_score, in_play, dealer_score
    
    in_play = False
    print "You have busted. New Deal?"
        
    while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
            
    print "Dealer: %s" % dealer_hand
        
    if dealer_hand.get_value() > 21:
        outcome = "Dealer Busted. Congrats! You win"
        print "Dealer Busted. Player wins"
        player_score +=1
            
    else:
        if dealer_hand.get_value() >= player_hand.get_value() or player_hand.get_value() > 21:
            outcome = "Dealer Wins !"
            print "Dealer Wins ! New Deal?"
            dealer_score += 1
        else:
            outcome = "You Win !"
            print "Player Wins. New Deal?"
            player_score += 1

#draw handler            
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global outcome, in_play, card_back, player_score, dealer_score
    
    canvas.draw_text("BlackJack", [220,50], 50, "Aqua")
    
    
    player_hand.draw(canvas, [100,300])
    dealer_hand.draw(canvas, [100,150])
    
    canvas.draw_text(outcome, [10,100], 30, "White")
    
    canvas.draw_text("Player's score: " + str(player_score), [10,275], 20, "White")
    canvas.draw_text("Dealer's score: " + str(dealer_score), [10,135], 20, "White")

    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (136,199), CARD_BACK_SIZE)
                     
    
#   card = Card("S", "A")
#   card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
