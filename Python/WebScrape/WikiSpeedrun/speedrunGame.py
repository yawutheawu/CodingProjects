from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
import pyautogui as pg
from pynput import mouse
from pynput import keyboard
import time

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}")

MouseListener = mouse.Listener(
    on_click=on_click)
MouseListener.start()

def on_activate():
    print('Control F Press attempted')
    pg.press("esc")

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+f'),
    on_activate)

hotkey_listener = keyboard.GlobalHotKeys({
    '<ctrl>+f': on_activate
},suppress=True)
hotkey_listener.start()

opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(options=opts)
driver.get("https://en.wikipedia.org/wiki/Special:Random")
goalPageLink = driver.current_url
goalPageName = str(driver.title).replace(" - Wikipedia", "")
print(f"Goal at: {goalPageName} ({str(goalPageLink)})")
driver.close()
pg.alert(text=f"Goal at: {goalPageName} ({str(goalPageLink)}), Press OK to start timer", title="WikiSpeedrun", button="OK")
opts = FirefoxOptions()
driver = webdriver.Firefox(options=opts)
driver.get("https://en.wikipedia.org/wiki/Special:Random")
time.sleep(0.25)
while driver.current_url == goalPageLink:
    driver.get("https://en.wikipedia.org/wiki/Special:Random")
    time.sleep(0.25)
StartTime = time.time()
while driver.current_url != goalPageLink:
    pass
totalTime = time.time() - StartTime
time.sleep(1)
driver.close()
MouseListener.stop()
hotkey_listener.stop()
print(f"Reached {goalPageName} in {totalTime:.2f} seconds")
pg.alert(text=f"Reached {goalPageName} in {totalTime:.2f} seconds", title="WikiSpeedrun", button="OK")