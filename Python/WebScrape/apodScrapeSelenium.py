import os
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
import time

def resetDir():
    """ Sets current working directory to the folder containing the script
        (For Relative Pathing)
    """
    fileName = __file__
    if type(fileName.split("\\")) == list and len(fileName.split("\\"))>1:
        fileName = fileName.split("\\")[-1]
        filePath = __file__.replace(fileName,"")
    else:
        fileName = fileName.split("/")[-1]
        filePath = __file__.replace(fileName,"")
    os.chdir(filePath)
    return os.path.abspath(filePath)

resetDir()

website = "https://apod.nasa.gov/apod/astropix.html"

opts = FirefoxOptions()

opts.add_argument("--headless")

driver = webdriver.Firefox(options=opts)

driver.get(website)

title = driver.find_element(By.XPATH,"/html/body/center[2]/b[1]").text.strip()
driver.find_element(By.XPATH,"/html/body/center[1]/p[2]/a/img").click()
time.sleep(1)
img = driver.find_element(By.TAG_NAME,"img")
with open(f"images/SELENIUM_{title}.png","wb") as f:
    f.write(img.screenshot_as_png)
driver.quit()
print(f"Got image ({title}) of the day!")