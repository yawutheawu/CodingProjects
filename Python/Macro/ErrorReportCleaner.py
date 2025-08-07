import pyperclip as clip
import datetime

rawError = clip.paste().strip()
print(rawError)
print("------------------------------------------------------------------------------------------------------------------------------------------------")
workingError = rawError.split("\n")
for k,_ in enumerate(workingError):
    if workingError[k] == "":
        del workingError[k]
for i,_ in enumerate(workingError):
    workingError[i] = workingError[i].split("  ")
for k,i in enumerate(workingError):
    while "" in workingError[k]:
        workingError[k].remove("")
for k,i in enumerate(workingError):
    for j,_ in enumerate(workingError[k]):
        workingError[k][j] = workingError[k][j].strip()
for k,i in enumerate(workingError):
    status = workingError[k][2]
    area = workingError[k][3]
    dept = workingError[k][4]

    workingError[k][1] = datetime.datetime.strptime(workingError[k][1],"%Y%m%d").date().strftime("%m/%d/%Y")
    workingError[k][2] = area
    workingError[k][3] = dept
    workingError[k][4] = status


copyText = ""
for i in workingError:
    for j in i:
        copyText += j + "\t"
    copyText += "\n"

clip.copy(copyText)
print(copyText)