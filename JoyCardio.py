'''
Joy-Cardio 
Use your joycons to control a virtual gamepad for cardio exercise

This is specifically the keyboard version. Later version will emulate an xbox controller

JoyconLeft is the joycon strapped onto your leg
JoyconRight is the joycon held in your hand

Made by: @superlouis64.bsky.social
YouTube: https://www.youtube.com/@superlouis64

Keyboard library: https://pypi.org/project/keyboard/
joycon library: https://pypi.org/project/pyjoycon/
'''

import pyjoycon
import keyboard
import icesucks
import customtkinter
import sys

#variables 
canContinue = False # check if joycons are detected
leftJoyConDetected = False
rightJoyConDetected = False
attempts = 0
bikeThreshold = 40  # threshold to activate bike riding input, can be changed by user
runCheck = 0  # variable to check when to run or not
isBikeing = True # if false user is on the treadmill
noJoyconDetected = 'No joycons detected, restart program'
JoyConDetcted = True

# variables that will be updated with joycon values
joyConLeftStick_Horizontal = 0
joyConLeftStick_Horizontal_Neutral = 0
joyConLeftStick_Vertical = 0
joyConLeftStick_Vertical_Neutral = 0

joyConRightStick_Horizontal = 0
joyConRightStick_Horizontal_Neutral = 0
joyConRightStick_Vertical = 0
joyConRightStick_Vertical_Neutral = 0

joyConRightAccel_X = 0
joyConRightAccel_Y = 0 
joyConRightAccel_Z = 0
joyConLeftAccel_X = 0
joyConLeftAccel_Y = 0 
joyConLeftAccel_Z = 0


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x300")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.title("Joy-Cardio Ver 0.1 - by SuperLouis64")
        self._set_appearance_mode("dark")

        # labels for the top of the app
        self.label = customtkinter.CTkLabel(self, text="Joy-Cardio Control Panel", text_color= "white", fg_color="gray", font=customtkinter.CTkFont(size=24, weight="bold"))
        self.label.grid(row=0, column=1, padx=0, pady=0, sticky="nsew") 
        self.labelWarning = customtkinter.CTkLabel(self, text="Make sure both Joycons are detected before continuing!", text_color="red")
        self.labelWarning.grid(row=1, column=1, padx=5, pady=10)
        self.labelCheckExercise = customtkinter.CTkLabel(self, text = "Exercise not Detected", text_color="red")
        self.labelCheckExercise.grid(row=1, column=2, padx=5, pady=10)

        #buttons for bike mode or treadmill 
        self.buttonBike = customtkinter.CTkButton(self, text="Using a bike", command=self.button_isBikeing)
        self.buttonBike.grid(row=2, column=1, padx=0, pady=10)
        self.buttonTreadmill = customtkinter.CTkButton(self, text="Using a treadmill", command=self.button_isTreadmill)
        self.buttonTreadmill.grid(row=3, column=1, padx=0, pady=10)
        self.butttonExit = customtkinter.CTkButton(self, text="Exit Program", command=self.button_exit)
        self.butttonExit.grid(row=5, column=1, padx=0, pady=5)

        # Show the user what lever they're on
        self.labelThreshouldLevel = customtkinter.CTkLabel(self, text="Exercise Lvl: " + str(bikeThreshold/10), text_color="white", fg_color="gray", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.labelThreshouldLevel.grid(row=2, column=2, padx=0, pady=10)
        self.button = customtkinter.CTkButton(self, text="Increase Workout", command=self.button_Thresholdup)
        self.button.grid(row=3, column=2, padx=0, pady=10)
        self.button2 = customtkinter.CTkButton(self, text="Decrease Workout", command=self.button_Thresholddown)
        self.button2.grid(row=4, column=2, padx=0, pady=5)



    def button_Thresholdup(self):
        global bikeThreshold
        if bikeThreshold >= 80:
            bikeThreshold = 80 
        else:
            bikeThreshold += 10   
        self.labelThreshouldLevel.configure(text="Exercise Lvl: " + str(bikeThreshold/10))
        print("Threshold increaded, threshold is " + str(bikeThreshold))
    
    def button_Thresholddown(self):
        global bikeThreshold
        if bikeThreshold <= 10:
            bikeThreshold = 10
        else:
            bikeThreshold -= 10
        self.labelThreshouldLevel.configure(text="Exercise Lvl " + str(bikeThreshold/10))
        print("Threshold decreased, bike threshold is " + str(bikeThreshold))
    
    def button_isBikeing(self):
        global isBikeing
        isBikeing = True
        print("User is bikeing")
    def button_isTreadmill(self):
        global isBikeing
        isBikeing = False
        print("User is on treadmill")

    # close the app
    def button_exit(self): 
        sys.exit()


# def update text in label
def updateLabelText():
    if JoyConDetcted == False:
        app.labelWarning.configure(text = 'One or both Joycons not detected, please reconnect and restart program.', text_color='red')
    else:
        app.labelWarning.configure(text = 'Both Joycons Detected', text_color='green')
    
def updateExerciseText(isExercising):
    if isExercising:
        app.labelCheckExercise.configure(text = 'Exercise Detected', text_color='green')
    else:
        app.labelCheckExercise.configure(text = 'Exercise not Detected', text_color ='red')

# console stuff
print('Joy-Cardio version 0.1 - by SuperLouis64')
print('For more information check out https://controllerbending.com/joy-cardio/')
print('Checking for Joycons')

# declare Left joycon and map values
joyconL_id = pyjoycon.get_L_id()
if joyconL_id[0] != None:
    joyConLeft = pyjoycon.JoyCon(*joyconL_id)
    leftJoyConDetected = True
    print('Left JoyCon Detected')
else:
    JoyConDetcted = False
    print('Program does not detect Left Joycon')

# declare right joycons and map values
joyconR_id = pyjoycon.get_R_id()
if joyconR_id[0] != None:
    print(joyconR_id)
    joyConRight = pyjoycon.JoyCon(*joyconR_id)
    rightJoyConDetected = True
    print('Right JoyCon Detected')
else:
    JoyConDetcted = False
    print('Program does not detect Right Joycon')


#grab the neutral values if both joycons are detected
if leftJoyConDetected and rightJoyConDetected:
    canContinue = True
    joyConRightStick_Horizontal_Neutral = joyConRight.get_stick_right_horizontal() #grab the neutral values
    joyConRightStick_Vertical_Neutral = joyConRight.get_stick_right_vertical()
    joyConLeftStick_Horizontal_Neutral = joyConLeft.get_stick_left_horizontal() #grab the neutral values
    joyConLeftStick_Vertical_Neutral = joyConLeft.get_stick_left_vertical()
else:
    pass
    print('Both JoyCons need to be detected to continue. Restart the program.')
    #exit()



#functions to grab all of the buttons from the right joycon
def RightJoyconButtons(): #currently set up for FFXIV will change later
    if joyConRight.get_button_x() == True:
        keyboard.press('page up')
    else:
        keyboard.release('page up')
    if joyConRight.get_button_a() == True:
        keyboard.press('num 0') 
    else:
        keyboard.release('num 0')
    if joyConRight.get_button_b() == True:
        keyboard.press('escape')
    else:
        keyboard.release('escape')
    if joyConRight.get_button_y() == True:
        keyboard.press('page down')
    else:
        keyboard.release('page down')
    if joyConRight.get_button_plus() == True:
        pass
    if joyConRight.get_button_home() == True:
        pass
    if joyConRight.get_button_r() == True:
        pass
    #print('zr value: ' + str(joyConRight.get_button_zr()))

#function to grab all of the buttons for the left joycon
def LeftJoyconButtons():
    if joyConLeft.get_button_left() == True:
        pass
    if joyConLeft.get_button_down() == True:
        pass
    if joyConLeft.get_button_up() == True:
        pass
    if joyConLeft.get_button_right() == True:
        pass
    if joyConLeft.get_button_minus() == True:
        pass
    if joyConLeft.get_button_capture() == True:
        pass    
    if joyConLeft.get_button_l() == True:
        pass
    #print('zl value: ' + str(joyConLeft.get_button_zl()))

#function to make riding a bike input W keyboard press
def RideBike(x, z): 
    global runCheck 
    updatedX = int(x /100) # we'll be using X axis for this
    updatedZ = int(z /100) # the z axis to prevent false positives from standing still
    #print('Accel X: ' + str(updatedX) + ' Y: ' + ' Z: ' + str(updatedZ))

    if(updatedX >= 40 ): #if above pace keep the runcheck maxed out
        if (updatedZ > 20): # to prevent a bug where standing can activate the input too
            runCheck = 100

    if(updatedX < 40 or updatedZ < 0): # if below pace decrease runcheck
        runCheck -= 2
        if runCheck < 0:
            runCheck = 0
 
    
    if(runCheck >= bikeThreshold): # if above threshold, press W
        keyboard.press('w')
    else:
        keyboard.release('w')
    #print('Current runcheck is: ' + str(runCheck))
    #print('Bike Threshold is: ' + str(bikeThreshold))

# Function that handles the bike riding 
# made so it can work with the mainloop of tkinter
def BikeExercise():
    joyConLeftStick_Horizontal = joyConLeft.get_stick_left_horizontal() 
    joyConLeftStick_Vertical = joyConLeft.get_stick_left_vertical() 
    joyConRightStick_Horizontal = joyConRight.get_stick_right_horizontal() 
    #print(joyConRightStick_Horizontal)
    joyConRightStick_Vertical = joyConRight.get_stick_right_vertical()
    joyConLeftAccel_X = joyConLeft.get_accel_x()
    joyConLeftAccel_Z = joyConLeft.get_accel_z()

    #getting and passing joystick values to keyboard
    #RightJoyconStick(joyConRightStick_Horizontal, joyConRightStick_Vertical)
    #LeftJoyconStick(joyConLeftStick_Horizontal, joyConLeftStick_Vertical)

    #use the imported function to handle the joycon -> keyboard inputs
    icesucks.RightJoyconJoystick(joyConRightStick_Horizontal, joyConRightStick_Vertical, joyConRightStick_Horizontal_Neutral, joyConRightStick_Vertical_Neutral)
    icesucks.LeftJoyconJoystick(joyConLeftStick_Horizontal, joyConLeftStick_Vertical, joyConLeftStick_Horizontal_Neutral, joyConLeftStick_Vertical_Neutral)

    RightJoyconButtons()
    #LeftJoyconButtons()

    RideBike(joyConLeftAccel_X, joyConLeftAccel_Z)

    if(isBikeing):
        app.after(100, BikeExercise) # run every X ms
    else:
        app.after(100, TreadmillExercise) # switch to treadmill exercise



# Treadmill function which should be the same as the bike but an updated method
def WalkTreadmill(JoyConY, JoyConZ):
    global runCheck
    updatedY = int(JoyConY /100) # make the units easier to read
    updatedZ = int(JoyConZ /100) 
    #print('Accel Y: ' + str(updatedY) + ' Z: ' + str(updatedZ))
    
    if(updatedY >= 8 ): #if above pace keep the runcheck maxed out
        if (updatedZ > 0): # to prevent a bug where standing can activate the input too
            runCheck = 100
            

    if(updatedY < 9 or updatedZ < -9): # if below pace decrease runcheck
        runCheck -= 3
        if runCheck < 0:
            runCheck = 0
    
    if(runCheck >= bikeThreshold): # if above threshold, press W
        keyboard.press('w')
        updateExerciseText(True)
    else:
        keyboard.release('w')
        updateExerciseText(False)
    #print('Current runcheck is: ' + str(runCheck))
    #print('Bike Threshold is: ' + str(bikeThreshold))



#Treadmill function
# the left joycon will be more vertical so it has to be a different type of dectecting it
def TreadmillExercise():
    joyConLeftStick_Horizontal = joyConLeft.get_stick_left_horizontal() 
    joyConLeftStick_Vertical = joyConLeft.get_stick_left_vertical() 
    joyConRightStick_Horizontal = joyConRight.get_stick_right_horizontal() 
    joyConRightStick_Vertical = joyConRight.get_stick_right_vertical()
    joyConLeftAccel_X = joyConLeft.get_accel_x()
    joyConLeftAccel_Y = joyConLeft.get_accel_y()
    joyConLeftAccel_Z = joyConLeft.get_accel_z()

    WalkTreadmill(joyConLeftAccel_Y, joyConLeftAccel_Z)
 
    #print(' Y: ' + str(joyConLeftAccel_Y) + ' Z: ' + str(joyConLeftAccel_Z))
    # seems like we'll use the y and z axis for detecting walking

    # pass the right joycon joystick and make keyboard inputs with them
    icesucks.RightJoyconJoystick(joyConRightStick_Horizontal, joyConRightStick_Vertical, joyConRightStick_Horizontal_Neutral, joyConRightStick_Vertical_Neutral)
    icesucks.LeftJoyconJoystick(joyConLeftStick_Horizontal, joyConLeftStick_Vertical, joyConLeftStick_Horizontal_Neutral, joyConLeftStick_Vertical_Neutral)


    if(isBikeing):
        app.after(100, BikeExercise) # run every X ms
    else:
        app.after(100, TreadmillExercise) # switch to treadmill exercise


# main app loop
app = App()
updateLabelText()
app.after(100, BikeExercise)
app.mainloop()

