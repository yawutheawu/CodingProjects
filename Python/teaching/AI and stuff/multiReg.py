import os
import pandas
from sklearn import linear_model

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

originalDF = pandas.read_csv(r"Data\\FinanceData\\Original_data.csv")
df = pandas.read_csv(r"Data\\FinanceData\\Finance_data.csv")

questions = originalDF.columns

del originalDF

print(df.head())

def genderToNum(x):
    if type(x) != str:
        if x==1:
            return "Female"
        else:
            return "Male"
    else:
        if x=="Female":
            return 1
        else:
            return 0

def YesNoToNum(x):
    if type(x) != str:
        if x==1:
            return "Yes"
        else:
            return "No"
    else:
        if x=="Yes":
            return 1
        else:
            return 0

def factorToNum(x):
    if type(x) != str:
        if x==1:
            return "Returns"
        elif x==2:
            return "Locking Period"
        elif x==3:
            return "Risk"
        else:
            return  None
    else:
        if x=="Returns":
            return 1
        elif x=="Locking Period":
            return 2
        elif x=="Risk":
            return 3
        else:
            return 0

def ObjectiveToNum(x):
    if type(x) != str:
        if x==1:
            return "Capital Appreciation"
        elif x==2:
            return "Income"
        elif x==3:
            return "Growth"
        else:
            return  None
    else:
        if x=="Capital Appreciation":
            return 1
        elif x=="Income":
            return 2
        elif x=="Growth":
            return 3
        else:
            return 0

def PurposeToNum(x):
    if type(x) != str:
        if x==1:
            return "Wealth Creation"
        elif x==2:
            return "Savings for Future"
        elif x==3:
            return "Returns"
        else:
            return  None
    else:
        if x=="Wealth Creation":
            return 1
        elif x=="Savings for Future":
            return 2
        elif x=="Returns":
            return 3
        else:
            return 0

def DurationToNum(x):
    if type(x) != str:
        if x==1:
            return "1-3 years"
        elif x==2:
            return "More than 5 years"
        elif x==3:
            return "3-5 years"
        elif x==4:
            return "Less than 1 year"
        else:
            return  None
    else:
        if x=="1-3 years":
            return 1
        elif x=="More than 5 years":
            return 2
        elif x=="3-5 years":
            return 3
        elif x=="Less than 1 year":
            return 4
        else:
            return 0

def InvMonitorToNum(x):
    if type(x) != str:
        if x==1:
            return "Monthly"
        elif x==2:
            return "Weekly"
        elif x==3:
            return "Daily"
        else:
            return  None
    else:
        if x=="Monthly":
            return 1
        elif x=="Weekly":
            return 2
        elif x=="Daily":
            return 3
        else:
            return 0

def ExpectToNum(x):
    if type(x) != str:
        if x==1:
            return "20%-30%"
        elif x==2:
            return "10%-20%"
        elif x==3:
            return "30%-40%"
        else:
            return  None
    else:
        if x=="20%-30%":
            return 1
        elif x=="10%-20%":
            return 2
        elif x=="30%-40%":
            return 3
        else:
            return 0

def AvenueToNum(x):
    if type(x) != str:
        if x==1:
            return "Mutual Fund"
        elif x==2:
            return "Equity"
        elif x==3:
            return "Fixed Deposits"
        elif x==4:
            return "Public Provident Fund"
        else:
            return  None
    else:
        if x=="Mutual Fund":
            return 1
        elif x=="Equity":
            return 2
        elif x=="Fixed Deposits":
            return 3
        elif x=="Public Provident Fund":
            return 4
        else:
            return 0

df["gender"] = df["gender"].apply(genderToNum)
df["Investment_Avenues"] = df["Investment_Avenues"].apply(YesNoToNum)
df.rename(columns={"Stock_Marktet":"Stock_Market"}, inplace=True)
df["Stock_Market"] = df["Stock_Market"].apply(YesNoToNum)
df["Factor"] = df["Factor"].apply(factorToNum)
df["Objective"] = df["Objective"].apply(ObjectiveToNum)
df["Purpose"] = df["Purpose"].apply(PurposeToNum)
df["Duration"] = df["Duration"].apply(DurationToNum)
df["Invest_Monitor"] = df["Invest_Monitor"].apply(InvMonitorToNum)
df["Expect"] = df["Expect"].apply(ExpectToNum)
df["Avenue"] = df["Avenue"].apply(AvenueToNum)
for i in df.columns:
    print(f"Column '{i}' unique values: {list(df[i].unique())}")
    
print(df.head())
# X = df[['Weight', 'Volume']]
# y = df['CO2']

# regr = linear_model.LinearRegression()
# regr.fit(X, y)

# """
# GENDER,AGE,Do you invest in Investment Avenues?,What do you think are the best options for investing your money? (Rank in order of preference) [Mutual Funds],What do you think are the best options for investing your money? (Rank in order of preference) [Equity Market],What do you think are the best options for investing your money? (Rank in order of preference) [Debentures],What do you think are the best options for investing your money? (Rank in order of preference) [Government Bonds],What do you think are the best options for investing your money? (Rank in order of preference) [Fixed Deposits],What do you think are the best options for investing your money? (Rank in order of preference) [Public Provident Fund],What do you think are the best options for investing your money? (Rank in order of preference) [Gold],Do you invest in Stock Market?,What are the factors considered by you while investing in any instrument?,What is your investment objective?,What is your purpose behind investment?,How long do you prefer to keep your money in any investment instrument?,How often do you monitor your investment?,How much return do you expect from any investment instrument?,Which investment avenue do you mostly invest in?,What are your savings objectives?,Reasons for investing in Equity Market,Reasons for investing in Mutual Funds,Reasons for investing in Government Bonds,Reasons for investing in Fixed Deposits ,Your sources of information for investments is 
# Female,34,Yes,1,2,5,3,7,6,4,Yes,Returns,Capital Appreciation,Wealth Creation,1-3 years,Monthly,20%-30%,Mutual Fund,Retirement Plan,Capital Appreciation,Better Returns,Safe Investment,Fixed Returns,Newspapers and Magazines
# """
# predictedCO2 = regr.predict([[2300, 1300]])

# print(predictedCO2)

#https://matplotlib.org/stable/plot_types/3D/surface3d_simple.html