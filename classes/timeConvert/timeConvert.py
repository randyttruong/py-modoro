import tkinter
import datetime 
import time 

class minutesSeconds():
    def __init__(self, minutes=25, seconds=0): 
        self.minutes = minutes
        self.seconds = seconds

    def getMinutesSeconds(self):
        minutes, seconds = (input('How many minutes/seconds would you like to study?').split())
        return self.minutes, self.seconds  

    def timeConvert(minutes: int, seconds: int):
        minutes = ( minutes * 60 )
        finalTime = minutes + seconds 
        return finalTime 


    
