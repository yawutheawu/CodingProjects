'''
Maykl Yakubovsky (MC Intern Summer of 2025)
Date Created: 07/22/2025
Last Edit: 07/23/2025
Title/Function: Automatically install Python libraries for SCAN Macros by Maykl Yakubovsky

To-Do:

Complete:

'''

import time

StartTime = time.time()

import subprocess
import sys
import traceback

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

reqLibs = ["pyautogui","openpyxl","pyperclip","datetime","pynput","pandas"]

for i in reqLibs:
    try:
        install(i)
    except:
        print(traceback.format_exc())

print("Done!")
print(f"Total runtime was {round(time.time() - StartTime,2)} seconds, or {round((time.time() - StartTime)/60,2)} minutes")