import random
import time
from selenium import webdriver

driver = webdriver.Firefox()

def GetRandomGPSLoc(waitTime = 10,zoom = 15):
    baseLink = "https://www.google.com/maps/@"

    randLink = baseLink + str(random.uniform(-90, 90)) + "," + str(random.uniform(-180, 180)) + f",{zoom}z"
    print(randLink)
    driver.get(randLink)
    time.sleep(waitTime)

for i in range(100):
    GetRandomGPSLoc(3,7)

driver.close()