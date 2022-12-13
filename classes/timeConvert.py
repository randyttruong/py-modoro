import sys, tkinter, datetime, time 
sys.path.insert(0, "../countDown/")
from countDown import countDown as cd 

class minutesSeconds():
    def __init__(self, minutes=25, seconds=0): 
        self.minutes = minutes
        self.seconds = seconds

    def getMinutesSeconds(self):
        minutes, seconds = (input('How many minutes/seconds would you like to study?').split())
        return self.minutes, self.seconds  

    def totalTime(minutes: int, seconds: int):
        minutes = ( minutes * 60 )
        finalTime = minutes + seconds 
        return finalTime 

