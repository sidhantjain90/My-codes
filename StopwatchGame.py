# "Stopwatch: The Game" created by Sidhant JAIN on 13.03.19
#  as a part of mini project for the online course: 
# "An Introduction to Interactive Programming in Python"


#Importing libraries
import simplegui

# define global variables
tick = 0
str_time = ""
total_stops = 0
success_stops = 0
first_stop = True


# Define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global tick, str_time
    
    A = tick//600
    B = tick//10%60//10
    C = tick//10%60%10
    D = tick%10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
# Define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global first_stop
    first_stop = False
    timer.start()
        
        
        
def stop():
    global tick, total_stops, success_stops 
    if first_stop == False:
        if tick%10 == 0 and tick !=0:
            success_stops += 1
            total_stops += 1
            
        else:
            total_stops += 1
       
    timer.stop()

    
def reset():
    global tick, success_stops, total_stops
    tick = 0
    success_stops = 0
    total_stops = 0
    timer.stop()
    
    
    

# Define event handler for timer with 0.1 sec interval
def timer():
    global tick
    tick += 1


# Define draw handler: 
# Two handlers created:-
# 1. To display the watch in M:SS.(MiliSec) format
# 2. To display the game of wins from total stops
def draw(canvas):
    canvas.draw_text(format(tick), [100,100], 20, "White")
    canvas.draw_text(str(success_stops) + "/" + str(total_stops), [50,50], 10, "Green")
    
# Create frame

frame = simplegui.create_frame("Stop Watch", 200, 200)

# Register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
timer = simplegui.create_timer(100, timer)


# Start frame

frame.start()
reset()
