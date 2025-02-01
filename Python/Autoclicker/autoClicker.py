import pyautogui as mouse
import time as t

clickFor = 10000

ScreenSize = mouse.size()

print("Move Mouse")
t.sleep(5)

print("Clicking")
for i in range(0,clickFor):
    clickerPos = mouse.position()
    mouse.click(clickerPos.x,clickerPos.y, button='left')
