import random as r
import time

exampleList = [i for i in range(1,1000000)]
r.shuffle(exampleList)

def mergeSort(listToSort):
    sortington = [[x] for x in listToSort]
    while type(sortington[0]) == list:
        for i in range(0,len(sortington)-1,2):
            mergaliciousList = []
            counter1 = 0
            counter2 = 0
            while counter1 < len(sortington[i]) or counter2 < len(sortington[i + 1]):
                if counter1 == len(sortington[i]):
                    mergaliciousList.append(sortington[i + 1][counter2])
                    counter2 +=  1
                elif counter2 == len(sortington[i+1]):
                    mergaliciousList.append(sortington[i][counter1])
                    counter1 +=  1
                elif sortington[i+1][counter2]  < sortington[i][counter1]:
                    mergaliciousList.append(sortington[i + 1][counter2])
                    counter2 +=  1
                else:
                    mergaliciousList.append(sortington[i][counter1])
                    counter1 +=  1
            sortington[i] = mergaliciousList
            sortington[i+1] = None
        sortington = [x for x in sortington if x != None]
        if len(sortington) == 1:
            sortington = sortington[0]
    return sortington

startMerge = time.time()
merged = mergeSort(exampleList)
endMerge = time.time()

startTrue = time.time()
trueSort  = sorted(exampleList)
endTrue = time.time()
print(merged)

print(f"Merge is accurate?: {merged == trueSort}")
print(f"Seconds to merge: {round(endMerge-startMerge,2)}")
print(f"Seconds to python  sort: {round(endTrue-startTrue,2)}")