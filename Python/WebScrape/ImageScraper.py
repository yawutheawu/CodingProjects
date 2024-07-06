import requests as re
from bs4 import BeautifulSoup

RSS = re.get("https://apod.nasa.gov/apod/astropix.html", headers=None)
Parsed = BeautifulSoup(RSS.content, features="html.parser")
allImage = Parsed.findAll("a")
Name = str(Parsed.findAll("center")[1].find("b")).replace("<b>", '').replace(
    "</b>", '')
image = re.get("https://apod.nasa.gov/apod/" + allImage[1]['href'],
               allow_redirects=True)
with open(f"images/{Name}.jpg", 'wb') as f:
    f.write(image.content)
print("Got Image of Day!")
