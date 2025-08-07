'''
Maykl Yakubovsky (MC Intern Summer of 2025)
Date Created: 06/06/2025
Last Edit: 06/20/2025
Title/Function: Support function for measuring click positions for macro development
'''

import pyautogui as pg
import openpyxl as xsl
from pynput import mouse
import time
import pyperclip as clip
import os

clicks = 0
max_clicks = 2
clicksList = []

def on_click(x, y, button, pressed):
    global clicks
    print((x, y))
    clicksList.append((x,y))
    clicks += 1
    if clicks >= max_clicks:
        clip.copy(clicksList)
        listener.stop() #creates an error stopping the code which works for me

with mouse.Listener(
        on_click=on_click
       ) as listener:
    listener.join()
