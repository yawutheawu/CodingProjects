import pandas as pd
import matplotlib.pyplot as plt
import os

def resetDir():
    """ Sets current working directory to the folder containing the script
        (For Relative Pathing)
    """
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

def getExtremes(dfCol, colDif=1):
    """ Returns list of indices of local minima and maxima in dataframe df """
    indices = []
    for i in range(1,len(dfCol)-1):
        if (dfCol.iloc[i] > dfCol.iloc[i-colDif] and dfCol.iloc[i] > dfCol.iloc[i+colDif]) or (dfCol.iloc[i] < dfCol.iloc[i-colDif] and dfCol.iloc[i] < dfCol.iloc[i+colDif]):
            indices.append(i)
    return indices

x = pd.read_csv(r"SPY Historical Data 1YR.csv",header=0,index_col=0,parse_dates=True)
print(x.head())
markers_on = getExtremes(x["Close"])
plt.plot(x.index, x["Close"], '-gD', markevery=markers_on)
plt.show()