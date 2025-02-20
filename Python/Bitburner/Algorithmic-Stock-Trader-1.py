'''
You are attempting to solve a Coding Contract. You have 5 tries remaining, after which the contract will self-destruct.


You are given the following array of stock prices (which are numbers) where the i-th element represents the stock price on day i:

181,190,13,73,47,46,109,62,65,68,186,179,101,25,199,173,76,20,32,93,117,123,121,73,176,99,38,102,60,30,56,174,101,145,34,189,54,73,51,180,189,38,79,96,180,186,48

Determine the maximum possible profit you can earn using at most one transaction (i.e. you can only buy and sell the stock once). If no profit can be made then the answer should be 0. Note that you have to buy the stock before you can sell it.


If your solution is an empty string, you must leave the text box empty. Do not use "", '', or ``.
'''
prices = [181,190,13,73,47,46,109,62,65,68,186,179,101,25,199,173,76,20,32,93,117,123,121,73,176,99,38,102,60,30,56,174,101,145,34,189,54,73,51,180,189,38,79,96,180,186,48]

def getDiffs():
    diffs = {}
    for k,i in enumerate(prices):
        diffs[k] = []
        for j in range(k,len(prices)):
            print(k,j)
            diffs[k].append([prices[j]-i,k,j])
        if diffs[k] == []:
            del diffs[k]
    return diffs

diffs = getDiffs()
diffList = []
for i in prices:
    for k,i in enumerate(prices):
        diffs[k] = []
        for j in range(k,len(prices)):
            print(k,j,prices[j]-i)
            diffList.append(prices[j]-i)
print(max(diffList))
input()

