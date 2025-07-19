import requests as re
import os
from bs4 import BeautifulSoup

def resetDir():
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

RSS = re.get("https://apod.nasa.gov/apod/astropix.html", headers=None)
Parsed = BeautifulSoup(RSS.content, features="html.parser")
title = Parsed.findAll("center")[1].find("b").text.strip()
ImageLink = Parsed.findAll("a")[1]['href']
imageBytes = re.get(f"https://apod.nasa.gov/apod/{ImageLink}",allow_redirects=True)
disallowedChars = ["/", "<", ">", ":", "\\", "|", "?", "*", " ",";",".","'"]
for i in disallowedChars:
    title = title.replace(i,"")
with open("images/"+title+".jpg", 'wb') as f:
    f.write(imageBytes.content)
print(f"Downloaded {title}.jpg from https://apod.nasa.gov/apod/{ImageLink}")