import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyautogui as pg

import undetected_chromedriver as uc

import time
import traceback
import random as r

numberBots = 350

if __name__ == "__main__":
    firstWordList = ["Blue","Cool", "Epic", "Sussy", "Big", "Small", "Fast", "Slow", 
                     "Smart", "Dumb", "Happy", "Sad", "Angry", "Lazy", "Active", "Brave", 
                     "Shy", "Loud", "Quiet", "Bright", "Dark", "Funny", "Serious", "Friendly", 
                     "Mean", "Kind", "Rude", "Lucky", "Unlucky", "Rich", "Poor", "Strong", 
                     "Weak", "Tall", "Short", "Hot", "Cold", "Soft", "Hard", "Light", "Heavy", 
                     "Clean", "Dirty", "New", "Old", "Young", "Ancient", "Modern", "Beautiful", 
                     "Ugly", "Good", "Bad", "Fast", "Slow", "Happy", "Sad", "Angry", "Lazy", 
                     "Active", "Brave", "Shy", "Loud", "Quiet", "Bright", "Dark", "Funny", 
                     "Serious", "Friendly", "Mean", "Kind", "Rude", "Lucky", "Unlucky", 
                     "Rich", "Poor", "Strong", "Weak", "Tall", "Short", "Hot", "Cold", 
                     "Soft", "Hard", "Light", "Heavy", "Funky", "Silly", "Crazy", "Weird", 
                     "Strange", "Boring", "Exciting", "Interesting", "Dull", "Vibrant", "Colorful", 
                     "Dull", "Bright", "Disturbed", "Calm", "Energetic", "Lazy", "Active", "Brave", 
                     "Shy", "Loud", "Quiet", "Bright", "Dark", "Funny", "Serious", "Friendly", "Mean", 
                     "Kind", "Rude", "Lucky", "Unlucky", "Rich", "Poor"]
    secondWordList = ["Cat", "Dog", "Fish", "Bird", "Monkey", "Lion", "Tiger", "Bear", "Shark", "Whale", 
                      "Dolphin", "Elephant", "Giraffe", "Zebra", "Panda", "Kola", "Kangaroo", "Rabbit", 
                      "Squirrel", "Fox", "Wolf", "Deer", "Horse", "Cow", "Pig", "Sheep", "Goat", "Chicken", 
                      "Duck", "Turkey", "Frog", "Snake", "Lizard", "Turtle", "Soda", "Juice", "Water", "Milk", 
                      "Coffee", "Tea", "Lemonade", "Smoothie", "Soda", "Energy Drink", "Herbert"]
    usedNames = []
    
    def generateNickname():
        nickname = r.choice(firstWordList) + r.choice(secondWordList)
        while nickname in usedNames:
            nickname = r.choice(firstWordList) + r.choice(secondWordList)
        usedNames.append(nickname)
        return str(nickname)
    
    try:
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

        wait = WebDriverWait(driver, 5)

        driver.get(website)
        while not verifiedGameID:
        
            ID_SubmitButton = wait.until(EC.element_to_be_clickable((By.XPATH, gameIDSubmitXPATH)))
            ID_input_box = driver.find_element(By.XPATH, gameIDXPATH)
            ID_input_box.clear()
            for char in str(gameID):
                ID_input_box.send_keys(char)
                time.sleep(0.075 + (r.random() * 0.075))
            time.sleep(0.075)
            ID_SubmitButton.click()
            try:
                errorBar = wait.until(EC.presence_of_element_located((By.XPATH, errorXPATH)))
            except:
                errorBar = None
            if errorBar and errorBar.is_displayed():
                pg.alert(text="Invalid Game ID, please try again", title='Invalid Game ID', button='OK')
                gameID = getGameID()
            else:
                verifiedGameID = True
        
        nickname = generateNickname()
        
        Nickname_SubmitButton = wait.until(EC.element_to_be_clickable((By.XPATH, nicknameSubmitXPATH)))
        Nickname_input_box = driver.find_element(By.XPATH, nicknameXPATH)
        Nickname_input_box.clear()
        counter = 0
        for char in str(nickname):
            if counter < 15:
                Nickname_input_box.send_keys(char)
                time.sleep(0.075 + (r.random() * 0.075))
                counter += 1
        time.sleep(0.075)
        Nickname_SubmitButton.click()
        
        time.sleep(0.1)
        
        for i in range(numberBots):
            driver.switch_to.new_window('tab')
            driver.get(website)
            
            ID_SubmitButton = wait.until(EC.element_to_be_clickable((By.XPATH, gameIDSubmitXPATH)))
            ID_input_box = driver.find_element(By.XPATH, gameIDXPATH)
            ID_input_box.clear()
            for char in str(gameID):
                ID_input_box.send_keys(char)
                time.sleep(0.075 + (r.random() * 0.075))
            time.sleep(0.075)
            ID_SubmitButton.click()
            time.sleep(0.1)
            
            nickname = generateNickname()
            
            Nickname_SubmitButton = wait.until(EC.element_to_be_clickable((By.XPATH, nicknameSubmitXPATH)))
            Nickname_input_box = driver.find_element(By.XPATH, nicknameXPATH)
            Nickname_input_box.clear()
            counter = 0
            for char in str(nickname):
                if counter < 15:
                    Nickname_input_box.send_keys(char)
                    time.sleep(0.075 + (r.random() * 0.075))
                    counter += 1
            time.sleep(0.1)
            Nickname_SubmitButton.click()
            
            time.sleep(0.1)
        input("Input anything to quit the program and close the browser: ")
        driver.quit()
    except Exception as e:
        print(traceback.format_exc())
        driver.quit()
    finally:
        while driver:
            driver.quit()

