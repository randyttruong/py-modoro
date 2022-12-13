'''
--------------------
Title: pymofocus
Author: Randy Truong (randyttruong)
Date: December 8, 2022 
Description: This is a Pomodoro Timer that is created in python using the tkinter package. 
--------------------
'''


import tkinter, datetime, time, sys
sys.path.insert(0, "./classes")
sys.path.insert(0, "./gui")
from classes import timer, timeConvert, countDown

'''
🚧 TODOS: 
    1. Finish timeConvert.py ✅  
    2. Finish timer.py ✅  
    3. Finish gui.py 🚫 
'''
inputs = sys.argv
minutes = int(inputs[2])
print(inputs)
userTimer = timer.Timer() 

if len(inputs[1:]) >= 1: 
    if len(inputs[1:]) == 1:
        userTimer.timerInit()
    elif len(inputs[1:]) == 2:  
        userTimer.setStudy(minutes)
        userTimer.timerInit()








