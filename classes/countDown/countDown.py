import tkinter, sys, datetime, time

def countDown(seconds: int): 
    seconds = seconds + 1 
    for i in range(1, seconds): 
        print(seconds - i)
        time.sleep(1)
    print("Timer Finished!")
    return True 


