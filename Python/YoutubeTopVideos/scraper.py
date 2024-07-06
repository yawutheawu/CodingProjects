from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By

opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(options=opts)
driver.get("https://www.youtube.com/")

print("getting links")

Content = driver.find_elements(By.ID, "video-title-link")
for i in Content:
    print(str(i.get_attribute("href")))
    
driver.close()
