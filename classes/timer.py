import tkinter, sys, datetime, time 
from timeConvert import timeConvert 
from countDown import countDown as cd 

sys.path.insert(0, "./classes/timeConvert")
sys.path.insert(0, "./gui")
sys.path.insert(0, "./classes/npyscreen")

class Timer():
    # Create Timer()
    def __init__(self, shortStudyTime=25, 
                 shortRestTime=5, longRestTime=15, 
                 numberOfSessions=0, remainingTime=0):
        self.shortStudyTime = shortStudyTime 
        self.shortRestTime = shortRestTime 
        self.longRestTime = longRestTime 
        self.numberOfSessions = numberOfSessions 

        self.remainingTime = remainingTime
        return None 

    # Start Timer 
    def timerInit(self):
        cd.countDown(self.shortStudyTime)
        self.numberOfSessions += 1 # Log full session 
        print(f"Study Timer complete. You have now completed {self.numberOfSessions} sessions! Good job and take a break.")
        self.startShortRestTime()

    # Start Short-Rest Timer 
    def startShortRestTime(self):
        cd.countDown(self.shortRestTime)
        print("Short Rest complete. Get back to work!")
        return True 

    # Start Long-Rest Timer 
    def startLongRestTime(self):
        cd.countDown(self.longRestTime)
        print("Long Rest complete. Get back to work! ")
        return True

    # Set Study Time 
    def setStudy(self, newMinutes=0):
        self.shortStudyTime = newMinutes
        print(f"Your study timer value has been set to {newMinutes} minutes.")

    def setSRest(self, newMinutes=0):
        self.shortRestTime = newMinutes
        print(f"Your short rest time value has been set to {newMinutes} minutes.")

    def setLRest(self, newMinutes=0):
        self.longRestTime = newMinutes
        print(f"Your long rest time value has been set to {newMinutes} minutes.")
        
