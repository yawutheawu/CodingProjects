import re

mail = re.compile(r"([\w\d]*)@(.+?)\.(.+?)\b")
corpus = """john@yahoo.com
john@hotmail.com
herman@gmail.com
jerry@somePreteniousCompany.org
jerimiah@hotmail.com
hello my email is jerimiah@hotmail.com and my home email is 12johnnyBoy1312@gmail.com"""

emailMatches = mail.findall(corpus)

print(emailMatches)

stringEmails = []

for match in emailMatches:
    stringEmails.append(f"{match[0]}@{match[1]}.{match[2]}")
    
print(stringEmails)