import time
import json
import os

flag = True
while flag:
    whichOne = input("Dynamic or Regular? (D/R): ").lower()
    if whichOne == "d" or whichOne == "r":
        flag = False
    else:
        print("Choose")



def FibonacciMemo(n,memo={0:1,1:1}):
    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = FibonacciMemo(n-1,memo) + FibonacciMemo(n-2,memo)
        return memo[n]

def FibonacciRec(n):
    if n == 1 or n == 0 :
        return 1
    else:
        return FibonacciRec(n-1) + FibonacciRec(n-2)

def timeTakenRecorder(cases):
    if whichOne == "d":
        resultsDict = {"memoNS":[0 for x in range(0,cases+1)],"memoFloat":[0 for x in range(0,cases+1)]}
    else:
        resultsDict = {"regNS":[0 for x in range(0,cases+1)],"regFloat":[0 for x in range(0,cases+1)]}
    for i in range(0,cases+1):
        print("Testing value: " + str(i))
        if whichOne == "d":
            floatStart = time.process_time()
            nanoSecondStart = time.process_time_ns()
            FibonacciMemo(i)
            floatEnd = time.process_time()
            nanoSecondEnd = time.process_time_ns()
            resultsDict["memoFloat"][i] = floatEnd-floatStart
            resultsDict["memoNS"][i] = nanoSecondEnd-nanoSecondStart
        else:
            floatStart = time.process_time()
            nanoSecondStart = time.process_time_ns()
            FibonacciRec(i)
            floatEnd = time.process_time()
            nanoSecondEnd = time.process_time_ns()
            resultsDict["regFloat"][i] = floatEnd-floatStart
            resultsDict["regNS"][i] = nanoSecondEnd-nanoSecondStart
    return resultsDict

fileName = __file__
if type(fileName.split("\\")) == list:
    fileName = fileName.split("\\")[-1]
    filePath = __file__.replace(fileName,"")
else:
    fileName = fileName.split("/")[-1]
    filePath = __file__.replace(fileName,"")
os.chdir(filePath)
os.chdir("Results")
os.chdir("SingleRuns")

Tests = 10
failed = True
while failed:
    try:
        Tests = int(input("How many values to test?: "))
        failed = False
    except:
        print("Please Enter a number! ")

results = timeTakenRecorder(Tests)
if whichOne == "d":
    os.chdir("Dynamic")
    resultsFileBase = "DynamicRunResult_"
    fileNumba = 1
    filesInResultsDir = os.listdir()
    if len(filesInResultsDir)>0:
        fileNumba = int(filesInResultsDir[-1].replace(resultsFileBase,"").replace(".json",""))
        fileNumba = fileNumba + 1
    with open(resultsFileBase+str(fileNumba)+".json","w") as f:
        json.dump(results,f)
else:
    os.chdir("Regular")
    resultsFileBase = "RegularRunResult_"
    fileNumba = 1
    filesInResultsDir = os.listdir()
    if len(filesInResultsDir)>0:
        fileNumba = int(filesInResultsDir[-1].replace(resultsFileBase,"").replace(".json",""))
        fileNumba = fileNumba + 1
    with open(resultsFileBase+str(fileNumba)+".json","w") as f:
        json.dump(results,f)
