# host the functions and what nots for joy-cardio
# will hopefully make main more cleaner

import keyboard
import pyjoycon
import keyboard
import time

def GrabJoycons():
    pass

def GrabNeutralPositions():
    pass

#function to handle Right joycon joystick inputs
def RightJoyconJoystick(horizontal, vertical, horizontal_neutral, vertical_neutral): 
    if horizontal > horizontal_neutral +400: # move right
        keyboard.press('d')
    else:
        keyboard.release('d')
    if horizontal < horizontal_neutral -400: # move left
        keyboard.press('a')
    else:  
        keyboard.release('a')  
    #if vertical > vertical_neutral + 900: #3 up will fixe later causing stutters right now
    #    keyboard.press('w')
    #else:
    #    keyboard.release('w') 
    if vertical < vertical_neutral - 700: # down
        keyboard.press('s')
    else:
        keyboard.release('s')   
    #print( "Right Joycon vertical values - Veritcal: {}, Vertical neutral: {}".format(vertical, vertical_neutral) )
    #print( "Right Joycon horizontal values - Horizontal: {}, Horizontal neutral: {}".format(horizontal, horizontal_neutral) )

 #function to handle left joycon joystick inputs
 # in this case we are using arrow keys which is camera controls in most games   
def LeftJoyconJoystick(horizontal, vertical, horizontal_neutral, vertical_neutral): 
    if horizontal > horizontal_neutral + 400: # right
        keyboard.press('right arrow')
    else:
        keyboard.release('right arrow')
    if horizontal < horizontal_neutral - 400: # left
        keyboard.press('left arrow')
    else:  
        keyboard.release('left arrow')  
    if vertical > vertical_neutral + 400: # up
        keyboard.press('up arrow')
    else:
        keyboard.release('up arrow') 
    if vertical < vertical_neutral - 400: # down
        keyboard.press('down arrow')
    else:
        keyboard.release('down arrow')   
    #print( "Left Joycon Joystick Values - Horizontal: {}, Vertical: {}".format(horizontal, vertical) )

