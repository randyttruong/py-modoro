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
sys.path.insert(0, "./classes/npyscreen")
from classes import timer, timeConvert
from gui import mainWindow
import npyscreen

'''
🚧 TODOS: 
    1. Finish timeConvert.py ✅  
    2. Finish timer.py 
    3. Finish gui.py 
'''

class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="py-mofocus version 1.0.0", lines=20, columns=60, draw_line_at=16)
        self.addForm("FORM2", MenuForm2, name="py-mofocus Options", lines=20, columns=60, draw_line_at=16)

# Main Menu Form 
class MainForm(npyscreen.ActionForm, npyscreen.SplitForm, npyscreen.FormWithMenus):
    def create(self):
        self.startTimer = self.add(npyscreen.Button, name="Start", value_changed_callback = self.startInit)
        self.stopTimer = self.add(npyscreen.Button, name="Stop", value_changed_callback = self.stopInit) 
        self.optionsButton = self.add(npyscreen.Button, name="Options", value_changed_callback = self.optionsInit) 
        # self.title = self.add(npyscreen.SelectOne, values=["Start"], rely=(2*y)//3, max_height=2)
        # self.title = self.add(npyscreen.SelectOne, values=["Stop"], max_height=2)
        # self.title = self.add(npyscreen.SelectOne, values=["Options"], max_height=2)
        # self.title = self.add(npyscreen.TitleMultiSelect, begin_entry_at=20, use_two_lines=None, name="Study Options", values=["Change Study Time", "Change Short Break Interval", "Change Long Break Interval"], scroll_exit= True)
    def startInit(self):
        return None 
    def stopInit(self):
        return None 
    def optionsInit(self):
        return None 
    def timer(self): 
        return None 
    def on_ok(self):
        self.parentApp.setNextForm(None)
    def on_cancel(self):
        self.title.value = "Hello World!"
    def buttonPress(self, widget):
        npyscreen.notify_confirm("BUTTON PRESSED!", title="Woot!", wrap=True, wide=True, editw=1)
        self.parentApp.switchForm('FORM2')


# Options Menu Form 
class MenuForm2(npyscreen.ActionForm, npyscreen.SplitForm, npyscreen.FormWithMenus):
    def create(self): 
        return None 

MyApp = App()
MyApp.run()




