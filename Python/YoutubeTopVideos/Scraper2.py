from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

opts = FirefoxOptions()
#opts.add_argument("--headless")
driver = webdriver.Firefox(options=opts)
driver.get("https://www.youtube.com/")

Content = driver.find_elements(By.ID, "contents")
for i in Content:
    print(i)

driver.close()
