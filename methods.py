from PIL.ImageOps import grayscale
from pyautogui import * 
import pyautogui
import time 
import keyboard
import numpy as np 
import random 
import win32api, win32con 
#import pywin32
import tkinter as tk
import threading 
time.sleep(2) 

def click(x,y):
    win32api.SetCursorPos((x,y)) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEVENTF_LEFTUP, 0, 0) 

# Check if the ESC key is pressed to ABORT 
# while keyboard.is_pressed('ESC') == False: 

# Check if Verification popup every 5 second 
def verificationCheck():
    threading.Timer(5.0, verificationCheck).start()

    if pyautogui.locateOnScreen('Verification.png', grayscale=True, confidence=1) != None:
        exit(0)

time.sleep(1)

# Check if Gold Production is ready to be collected
if pyautogui.pixel(1198,880)[0] == 235: 

    # Collect Gold Production
    click(1198,880)

time.sleep(0.3)
# Check if Farm Production is ready to be collected
if pyautogui.pixel(1330,795)[0] == 229: 

    # Collect Farm Production
    click(1330,795) 

time.sleep(0.3)
# Check if Wood Production is ready to be collected
if pyautogui.pixel(922,577)[0] == 224: 

    #Collect Wood Production 
    click(922,577) 

time.sleep(0.3)
# Check if Stone Production is ready to be collected
if pyautogui.pixel(821,694)[0] == 225:

    # Collect Stone Production 
    click(821,694) 

time.sleep(0.3)
# Check if Recruit is available 
if pyautogui.pixel(439, 393)[0] == 143: 

    # Click on Tavern 
    click(504, 523)

    time.sleep(0.3)
    # Click on Recruit Button 
    click(693, 698)

    # Check if Silver Chest is available
    if pyautogui.pixel(346, 870)[0] == 0: 

        time.sleep(0.3) 
        # Click on Silver Chest Button 
        click(346, 870) 

        time.sleep(4) 
        # Click on Confirm Button  # 10+ keys
        click(356, 892)
    
    # Check if Golden Chest is available
    if pyautogui.pixel(857, 874)[0] == 0: 

        time.sleep(0.3) 
        # Click on Golden Chest Button
        click(857, 874) 

        time.sleep(4) 
        # Click on Confirm Button # < 10 keys 
        click(470, 877)

    # Check if Equipment Chest is available 
    if pyautogui.pixel(1382, 863)[0] == 0: 
        
        time.sleep(0.3)
        # Click on Equipment Chest Button
        click(1382, 863) 

        time.sleep(4) 
        # Click on Confirm Button # < 10 keys 
        click(487, 901) 
    
    time.sleep(1) 
    # Close Recruit Window 
    click(81, 87) 

time.sleep(0.3) 
# Check for Alliance Help
if pyautogui.pixel(1755, 693)[2] == 0: 
    click(1755, 693)

