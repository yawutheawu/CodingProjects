import smtplib as s
import imaplib as i
import time
import email
from email.header import decode_header
from email.message import EmailMessage


import os
from dotenv import load_dotenv

waitTime = 10



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


runFlag = True
while runFlag:
    time.sleep(1)
    inbox.select('inbox')
    status, messages = inbox.search(None, 'UNSEEN')
    message_ids = messages[0].split()
    if len(message_ids) > 0:
        for mail in message_ids:
            email_status, msg_data = inbox.fetch(mail, "(RFC822)")
            msg = email.message_from_bytes(msg_data[0][1])
            commander = msg["From"]
            subject = decode_header(msg["Subject"])[0][0]
            if subject.lower().strip() == "command":
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True)
                        messageText = body.decode()
                        break
                actualText = []
                for line in messageText.split("\n"):
                    appendText = line.replace(">","").strip()
                    if appendText != "":    
                        actualText.append(appendText)
                for i in actualText:
                    command = i.lower().strip()
                    print(f"Attempting to run command: {command} from {commander}")
                    try:
                        if command == "exit":
                            runFlag = False
                            print("Exiting program as per command.")
                            break
                        elif command.startswith("echo"):
                            echoMessage = command.replace("echo","",1).strip()
                            responseMsg = EmailMessage()
                            responseMsg["Subject"] = "RE:" + subject
                            responseMsg["From"] = f"TCS Coder Bot"
                            responseMsg["To"] = commander
                            responseMsg.set_content(echoMessage)
                            smtpObj.send_message(responseMsg)
                            print(echoMessage)
                        elif command.startswith("say"):
                            sayMessage = command.replace("say","",1).strip()
                            print(sayMessage)
                        elif command.startswith("sendmail"):
                            mailToSend = command.replace("sendmail","",1).strip()
                            recepient, message = mailToSend.split(",",1)
                            responseMsg = EmailMessage()
                            responseMsg["Subject"] = "Remote Message"
                            responseMsg["From"] = f"TCS Coder Bot"
                            responseMsg["To"] = recepient.strip()
                            responseMsg.set_content(message.strip())
                            smtpObj.send_message(responseMsg)
                            print("Sent automated email")
                        elif command.startswith("setwait"):
                            waitTime = command.replace("setwait","",1).strip()
                            try:
                                waitTime = float(waitTime)
                                print(f"Setting wait time to {waitTime} seconds")
                            except:
                                print("Invalid wait time specified.")
                        else:
                            print("Unknown command:", command)
                    except Exception as e:
                        print(f"Error executing command '{command}': {e}")
    else:
        time.sleep(waitTime)

del mail
os.environ.pop("mail")
os.environ.pop("passkey")
smtpObj.close()
inbox.logout()