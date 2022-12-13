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
inputs = sys.argv[1]

if inputs == "start": 
    timer = timer.Timer() 
    timer.timerInit()











