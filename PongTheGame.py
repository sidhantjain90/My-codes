# Implementation of classic arcade game Pong by Sidhant JAIN
# as a part of mini project in the course "An Introduction to Interactive 
# Programming in Python (Part 1)" by COURSERA

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0, 1] # pixels per update (1/60 seconds)

#Paddles
paddle1_pos = HEIGHT/2.5
paddle2_pos = HEIGHT/2.5
paddle1_vel = 0
paddle2_vel = 0
paddle_vel = 5


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel[0] = -random.randrange(120,240)/100
    if direction == True:
        ball_vel[0] *= -1
    ball_vel[1] = -random.randrange(60,180)/100
       

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos # these are numbers
    global score1, score2  # these are ints
    
    score1 = 0
    score2 = 0
    spawn_ball(0)
    paddle1_pos = HEIGHT/2.5
    paddle2_pos = HEIGHT/2.5
    
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
        
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # Checking the side + ball touches pads or gutters:-
    
    # 1. If ball touches pad or gutter x-velocity is reversed
    # 2. In right side, if ball touches gutter, score1 is updated by a point
    # 3. In left side, if ball touches gutter, score2 is updated by a point
    # 4. If ball touches pad, x-veclocity is increased by 10% in addition to reversing(already in 1)
    
    
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH) or ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS):
        ball_vel[0] *= -1
        
        if (ball_pos[0] > WIDTH/2):
            if ball_pos[1] < paddle2_pos or ball_pos[1] > (PAD_HEIGHT + paddle2_pos):
                score1 += 1
                spawn_ball(LEFT)
                
            else:
                ball_vel[0] += .1*ball_vel[0]
                
        elif (ball_pos[0] < WIDTH/2):
            if ball_pos[1] < paddle1_pos or ball_pos[1] > (PAD_HEIGHT + paddle1_pos):
                score2 += 1
                spawn_ball(RIGHT)
                
            else:
                ball_vel[0] += .1*ball_vel[0]
               
    
    # Checking if ball touches top and bottom
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] *= -1
        
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    
    if (paddle1_pos <= (HEIGHT - PAD_HEIGHT) and paddle1_vel > 0) or (paddle1_pos >= 0 and paddle1_vel < 0):
        paddle1_pos += paddle1_vel
    
    elif (paddle2_pos <= (HEIGHT - PAD_HEIGHT) and paddle2_vel > 0) or (paddle2_pos >= 0 and paddle2_vel < 0):
        paddle2_pos += paddle2_vel
        
    
    # draw paddles
    canvas.draw_polygon([[0,paddle1_pos],[PAD_WIDTH,paddle1_pos],[PAD_WIDTH,(PAD_HEIGHT+paddle1_pos)],[0,(PAD_HEIGHT+paddle1_pos)]],12,"Red")
    canvas.draw_polygon([[WIDTH,paddle2_pos],[WIDTH-PAD_WIDTH,paddle2_pos],[WIDTH-PAD_WIDTH, PAD_HEIGHT+paddle2_pos],[WIDTH,PAD_HEIGHT+paddle2_pos]],12,"Red")
    
    
    # draw scores
    canvas.draw_text(str(score1), [225, 100], 60, "Green")    
    canvas.draw_text(str(score2), [350, 100], 60, "Green")
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle_vel
    
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = paddle_vel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -paddle_vel
        
        
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -paddle_vel
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = paddle_vel
        
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
        
        
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
        

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",new_game, 200)


# start frame
new_game()
frame.start()
