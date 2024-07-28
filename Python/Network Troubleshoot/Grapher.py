import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import json

pingDat = r"pingData.json"
failDat = r"FailureData.json"
AppIgnore = r"IgnoreList.json"

def load(file):
    with open(file, "r") as f:
        return json.load(f)
pingDict = load(pingDat)

def piGraph(data):
    labels = ["Success", "Failure"]
    Sizes = [0,0]
    for i in data.keys():
        if data[i]:
            Sizes[0] += 1
        else:
            Sizes[1] += 1
    
    fig, ax = plt.subplots()
    ax.pie(Sizes, labels=labels, autopct='%1.1f%%', colors=["green","red"])
    plt.show()

def ColorGraph(data,pingsToShow = 0):
    lineData = []
    timeData = []
    for k,i in enumerate(data.keys()):
        if data[i]:
            lineData.append(1)
        else:
            lineData.append(-1)
        timeData.append(k)
    if pingsToShow>0:
        lineData = lineData[-1*pingsToShow:]
        timeData = timeData[-1*pingsToShow:]
    lineData = np.array(lineData)
    timeData = np.array(timeData)
    fig, ax = plt.subplots()
    ax.plot(timeData, lineData, color='black')
    ax.axhline(0, color='black')
    ax.fill_between(timeData, 1, where=lineData > 0, facecolor='green', alpha=.5)
    ax.fill_between(timeData, -1, where=lineData < 0, facecolor='red', alpha=.5)
    plt.show()

def FailPie(FailFile, remover=True, sortTo = 0):
    data = load(FailFile)
    appData = {}
    for i in data.values():
        for j in i:
            if j in appData.keys():
                appData[j] +=1
            else:
                appData[j] =1
    ignoreList = load(AppIgnore)
    if remover:
        for i in ignoreList:
            try:
                del appData[i]
            except:
                print(f"{i} was not running, skipping")
    labels = list(appData.keys())
    Sizes = list(appData.values())
    if sortTo > 0 and sortTo < len(Sizes):
        NewSize = []
        NewLabel = []
        for k in range(0,sortTo):
            NewSize.append(max(Sizes))
            Sizes.remove(max(Sizes))
        for i in NewSize:
            for j in appData.keys():
                if appData[j] == i and j not in NewLabel:
                    NewLabel.append(j)
                    break
        Sizes = NewSize
        labels = NewLabel
    fig, ax = plt.subplots()
    ax.pie(Sizes, labels=labels, autopct='%1.1f%%')
    plt.show()

def ColorGraphLive(file, numToShow):
    #Ensure Pinger Is running (W.I.P.)
    lineData = []
    timeData = []
    data = load(file)
    for k,i in enumerate(data.keys()):
        if data[i]:
            lineData.append(1)
        else:
            lineData.append(-1)
        timeData.append(k)
    CutLine = []
    CutTime = []
    for i in range(len(lineData)-1,len(lineData)-numToShow-1,-1):
        CutLine.insert(0,lineData[i])
        CutTime.insert(0,i)
    lineData = np.array(CutLine)
    timeData = np.array(CutTime)
    def animate(i):
        lineData = []
        timeData = []
        data = load(file)
        for k,i in enumerate(data.keys()):
            if data[i]:
                lineData.append(1)
            else:
                lineData.append(-1)
            timeData.append(k)
        CutLine = []
        CutTime = []
        for i in range(len(lineData),len(lineData)-numToShow,-1):
            CutLine.insert(0,lineData[i])
            CutTime.insert(0,i)
        lineData = np.array(CutLine)
        timeData = np.array(CutTime)
    fig, ax = plt.subplots()
    ax.plot(timeData, lineData, color='black')
    ax.axhline(0, color='black')
    ax.fill_between(timeData, 1, where=lineData > 0, facecolor='green', alpha=.5)
    ax.fill_between(timeData, -1, where=lineData < 0, facecolor='red', alpha=.5)
    animated = animation.FuncAnimation(fig, animate, interval = 1000)
    plt.show()

#Ensure Pinger Is running (Not Working as of now)
#ColorGraphLive(pingDat,50)

#piGraph(pingDict)
y = 0
try:
    y = int(input("How Many Pings should be shown? "))
except Exception as e:
    print(f"Exception {e} as occured, defaulting to All pings")
ColorGraph(pingDict, y)
x = 15
try:
    x = int(input("How Many Programs should be shown? "))
except Exception as e:
    print(f"Exception {e} as occured, defaulting to 15 programs")
FailPie(failDat, sortTo=x)
