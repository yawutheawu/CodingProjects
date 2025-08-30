import smtplib
import os
from dotenv import load_dotenv

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
load_dotenv("secrets.env")

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)

smtpObj.ehlo()
smtpObj.login('tcstestbot@gmail.com', os.getenv("passkey"))

recep = "mayklprime@gmail.com"

subject = "Test Email from Python"
Text = "hello this is a test email from python"

msg = 'Subject: {}\n\n{}'.format(subject, Text)

smtpObj.sendmail(to_addrs=recep, from_addr='tcstestbot@gmail.com' ,  msg=msg)

smtpObj.close()