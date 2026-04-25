import requests as r
import os
from bs4 import BeautifulSoup

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
response = r.get(website, headers=None)

html = response.content
#print(html)
soup = BeautifulSoup(html, features="html.parser")
baseSite = ""
websiteParts = website.split("/")
for i in range(len(websiteParts)-1):
    baseSite += websiteParts[i] + "/"
imageSite = soup.find_all("a")[1]['href']
imageName = soup.select("body > center:nth-child(2) > b:nth-child(1)")[0].text.strip()
image = r.get(baseSite + imageSite,allow_redirects=True)
with open(f"images/{imageName}.png","wb") as f:
     f.write(image.content)
print("Got Image of Day!")