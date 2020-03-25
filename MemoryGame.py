# implementation of card game - Memory developed by Sidhant JAIN
# as a mini-project for the course of IIPP-2 on Cousera

import simplegui
import random

#cards = []
#exposed = []

click1 = 0
click2 = 0

# helper function to initialize globals
# States initialized to zero and a list of cards created
# and shuffled
def new_game():
    global state, cards, exposed, turns
    state = 0
    turns = 0
    
    cards = [i%8 for i in range(16)] 
    random.shuffle(cards)
    
    exposed = [False for i in range(16)]
    
    label.set_text('Turns = ' + str(turns))
    

# define event handlers
def mouseclick(pos):
    # Global variables
    global state, cards, exposed, click1, click2, turns
    
# Position of click is determined by the a variable 'choice' which is
# calculated by integer division operator. 
# Example: If the width of mouse click is within the range 0-50, it will be 
# considered as card 1.
    
    choice = pos[0]//50
    
    if state == 0:
        state = 1
        click1 = choice
        exposed[click1] = True
    elif state == 1:
        if not exposed[choice]:
            state = 2
            click2 = choice
            exposed[click2] = True
            turns += 1
    elif state == 2:
        if not exposed[choice]:
            if cards[click1] == cards[click2]:
                pass
            else:
                exposed[click1] = False
                exposed[click2] = False
            
            state = 1
            click1 = choice
            exposed[click1] = True

    label.set_text('Turns = ' + str(turns))                        

# cards are logically 50x100 pixels in size    
def draw(canvas):

    for card_index in range(len(cards)):
        if exposed[card_index]:
            card_pos = 50*card_index
            canvas.draw_text(str(cards[card_index]),[card_pos+10,60],50,"White")
        else:
            canvas.draw_polygon([[50*card_index,0],[50*card_index + 50,0],[50*card_index + 50,100],[50*card_index,100]],3,"Black","Green")
    
# create frame and add a button and labels

frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
