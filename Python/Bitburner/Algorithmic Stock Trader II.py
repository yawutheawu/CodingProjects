prices = [189,43,156,193,145,1,37,132,52,161,64,194,37,99,196,147,97,39,52,82,173,139,82,15,127,29,42]

startDay = 0
endDay = len(prices)-2

def getDiffs():
    diffs = {}
    for k,i in enumerate(prices):
        diffs[k] = []
        for c,j in enumerate(prices):
            if c > k and j-i > 0:
                diffs[k].append([j-i,k,c])
            else:
                pass
        if diffs[k] == []:
            del diffs[k]
    return diffs

diffs = getDiffs()
diffList = []
for i in diffs.keys():
    diffList.extend(diffs[i])

def getMaxReturn(listOfDiffs):
    maxReturn = 0
    maxVal = 0
    for k,i in enumerate(listOfDiffs):
        if i[0] > maxReturn:
            maxReturn = i[0]
            maxVal = k
    return listOfDiffs[maxVal]

def generateStarterCombos(diffs):
    comboGroups = []
    for i in diffs.keys():
        comboGroups.append([getMaxReturn(diffs[i])])
    return(comboGroups)
starter = generateStarterCombos(diffs)
perms = []
def generateNextPermutations(previous):
    endingDay = previous[2]
    potentialDiffs = [x for x in diffList if x[1] > endingDay]
    print(potentialDiffs)
for i in starter:
    pass