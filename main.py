from pyautogui import * 
import pyautogui
import time 
import keyboard
import numpy as np 
import random 
#import win32api, win32con 
import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('Automation Bot')

        first_label = tk.Label(self, text = "Educational Bot Project", font=10)  
        first_label.pack(pady=2, padx=2)

        first_button = tk.Button(self, text = "Button", command = test)
        first_button.pack(pady=5, padx=5)

def test():
    print("Testing")
app = Application()
app.mainloop()