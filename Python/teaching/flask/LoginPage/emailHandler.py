import smtplib as s
import imaplib as i
import email
from email.header import decode_header
from email.message import EmailMessage
import random as r
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

mail =  os.getenv("mail")
password =  os.getenv("passkey")

smtpObj = s.SMTP_SSL('smtp.gmail.com', 465)
inbox = i.IMAP4_SSL("imap.gmail.com")
resetDir()

def sendPasswordResetEmail(to_email):
    reset_code = r.randint(100000, 999999)
    smtpObj.ehlo()
    smtpObj.login(mail, password)
    msg = EmailMessage()
    msg["Subject"] = "Password Reset Request"
    msg["From"] = mail
    msg["To"] = to_email
    msg.set_content("You have requested a password reset. Your reset code is: {}\nDo not share this code with anyone.".format(reset_code))
    smtpObj.send_message(msg)
    return reset_code