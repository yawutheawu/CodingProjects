import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyautogui as pg

import undetected_chromedriver as uc

import time


if __name__ == "__main__":
    
    beta_chrome_path = r"C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
    
    website = "https://play.blooket.com/play"

    gameIDXPATH = r"/html/body/main/div/form/div[1]/div/div/input"
    gameIDSubmitXPATH = r"/html/body/main/div/form/div[1]/div/button"
    nicknameXPATH = r"/html/body/div/div/div/div[2]/div/form/div[2]/div[1]/input"
    nicknameSubmitXPATH = r"/html/body/div/div/div/div[2]/div/form/div[2]/div[2]"
    errorXPATH = r"/html/body/section/div/div/div[1]"

    def getGameID():
        gameID = ""
        while type(gameID) != int:
            try:
                user_input = str(pg.prompt(text='Input Blooket Game ID', title='Input Game ID', default='')).strip()
                gameID = int(user_input)
            except:
                pg.alert(text="Please enter a valid game ID", title='Invalid Input', button='OK')
        return gameID

    gameID = getGameID()
    verifiedGameID = False
    
    options = uc.ChromeOptions()
    
    driver = uc.Chrome(browser_executable_path=beta_chrome_path,
                       options=options)

    wait = WebDriverWait(driver, 10)

    driver.get(website)

    ID_SubmitButton = wait.until(EC.element_to_be_clickable((By.XPATH, gameIDSubmitXPATH)))
    ID_input_box = driver.find_element(By.XPATH, gameIDXPATH)
    ID_input_box.clear()
    for char in str(gameID):
        ID_input_box.send_keys(char)
        time.sleep(0.2)
    ID_SubmitButton.click()
    
    nickname = "HelloHa"
    
    Nickname_SubmitButton = wait.until(EC.element_to_be_clickable((By.XPATH, nicknameSubmitXPATH)))
    Nickname_input_box = driver.find_element(By.XPATH, nicknameXPATH)
    Nickname_input_box.clear()
    for char in str(nickname):
        Nickname_input_box.send_keys(char)
        time.sleep(0.2)
    Nickname_SubmitButton.click()
    
    time.sleep(5)
    
    driver.quit()

