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
ImageLink = Parsed.findAll("a")[1]['href']
Name = str(Parsed.findAll("center")[1].find("b")).replace("<b>", '').replace(
    "</b>", '')
image = re.get("https://apod.nasa.gov/apod/" + ImageLink,
               allow_redirects=True)
Name = Name.replace("/","-")
Name = Name.replace("<"," ")
Name = Name.replace(">"," ")
Name = Name.replace(":",";")
Name = Name.replace("\\","_")
Name = Name.replace("|","_")
Name = Name.replace("?"," ")
Name = Name.replace("*"," ")
Name = Name.replace(" ","")
with open(f"images/{Name}.jpg", 'wb') as f:
    f.write(image.content)
print("Got Image of Day!")
