import matplotlib.pyplot as plt
import json
import os

def AttemptInput(files):
    print("Which File would you like to graph?: ")
    n = 0
    for i,k in enumerate(files):
        if n < 5:
            print(str(i+1) + ". " + str(k), end = "   ")
            n+=1
        else:
            n = 0
            print("\n" + str(i+1) + ". " + str(k), end = "   ")
    selection = 0
    failed = True
    while failed:
        try:
            selection = int(input("\nType in the number before the filename: ")) - 1
            failed = False
        except:
            print("Please Input a number!")
    return selection

def retrVals(fileName):
    results = {}
    with open(fileName,"r") as f:
        results = json.load(f)
    return results

fileName = __file__
if type(fileName.split("\\")) == list:
    fileName = fileName.split("\\")[-1]
    filePath = __file__.replace(fileName,"")
else:
    fileName = fileName.split("/")[-1]
    filePath = __file__.replace(fileName,"")
os.chdir(filePath)
os.chdir("Results")
filesToTest = os.listdir()
files = []
for i in filesToTest:
    if os.path.isfile(i):
        files.append(i)
fileSelection = files[-1]
failed = True
while failed:
    try:
        fileSelection = files[AttemptInput(files)]
        failed = False
    except:
        print("Please enter the number of an existing file!")
encodedFile = retrVals(fileSelection)
dynamicNS = encodedFile["memoNS"]
dynamicSec = encodedFile["memoFloat"]
regNS = encodedFile["regNS"]
regSec = encodedFile["regFloat"]
#Nanosecond graph
plt.plot([x for x in range(len(dynamicNS))], dynamicNS, label ='Dynamic',color="blue")
plt.plot([x for x in range(len(dynamicNS))], regNS, '-.', label ='Regular ',color="red")
plt.xlabel("Value Inputed")
plt.ylabel("Nanoseconds")
plt.legend()
plt.title('Nanosecond Timer of Dynamic vs Recursive Fibonacci function')
os.chdir("..")
os.chdir("Graphs")
plt.savefig(str(fileSelection) + "_graphNS"+'.png',bbox_inches='tight')
plt.show()
#SecondsGraph
#Nanosecond graph
plt.plot([x for x in range(len(dynamicSec))], dynamicSec, label ='Dynamic',color="blue")
plt.plot([x for x in range(len(dynamicSec))], regSec, '-.', label ='Regular ',color="red")
plt.xlabel("Value Inputed")
plt.ylabel("Seconds")
plt.legend()
plt.title('Seconds (Float) Timer of Dynamic vs Recursive Fibonacci function')
os.chdir("..")
os.chdir("Graphs")
plt.savefig(str(fileSelection) + "_graphSeconds"+'.png',bbox_inches='tight')
plt.show()