import smtplib as s
import imaplib as i
import email
from email.header import decode_header
from email.message import EmailMessage


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
#smtpObj.debuglevel = 1

smtpObj.ehlo()
smtpObj.login(mail, password)
inbox.login(mail, password)
del password

msg = EmailMessage()
msg["Subject"] = "You have mail"
msg["From"] = mail
msg["To"] = "mayklprime@gmail.com"
msg.set_content("hello I have sent the mail")

#smtpObj.send_message(msg)
del mail

inbox.select('inbox')
status, messages = inbox.search(None, 'ALL')
message_ids = messages[0].split()

for i in message_ids:
    email_status, msg_data = inbox.fetch(i, "(RFC822)")
    msg = email.message_from_bytes(msg_data[0][1])
    print("From:", msg["From"])
    print("Subject:", decode_header(msg["Subject"])[0][0])
    print("Date:", msg["Date"])
    print("")
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            print(body.decode())
            break
    print("="*50)

os.environ.pop("mail")
os.environ.pop("passkey")
smtpObj.close()
inbox.logout()
print("Sent Mail")