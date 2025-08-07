'''
Maykl Yakubovsky (MC Intern Summer of 2025)
Date Created: 07/22/2025
Last Edit: 08/04/2025
Title/Function: Fetches Units per P-List header for a given P-List date

To-Do:

Complete:

'''

#Steps:
# 3. Bulk, 1. P-List by Date, go to correct date, on each keytrol pass a 5, and then a 3 into the same keytrol in the list, then copy units

#Grab Keytrol, status, plts, units, desc, dept

import pyautogui as pg
import openpyxl as xsl
import time
import winsound
import json
import traceback
import re
import itertools
import pyperclip as clip
import datetime
import socket
import os
import pandas as pd

StartTime = time.time()

# Controls how long the delay between inputs for failsafe is (0.1 by default, 0.01 seems to just barely work if the mouse is moved quickly)
#0.01 is too fast for scan to work right
pg.PAUSE = 0.03

scriptRunner = str(socket.gethostname())
print(f"Running on PC: {scriptRunner}")

pcClickLocs = {}

def resetDir():
    fileName = str(os.path.basename(__file__))
    OverallFolder = str(__file__).replace(fileName,"")
    os.chdir(OverallFolder)
resetDir()
os.chdir("Additonal")
os.chdir("Files")
with open("ScanClickLocations.json","r") as f:
    pcClickLocs = json.load(f)

if not scriptRunner in pcClickLocs.keys():
    pg.alert(text = "This PC does not have scan positions set up, and will use default values. This can lead to errors that may not be caught by the script. In case of these errors, quickly move the mouse to any corner of the screen to trigger the failsafe and force end the script.",title='Warning', button='OK')

#Globals
scanWindowName= "Worcester - Micro Focus Rumba+ Desktop"
errorMessage = """---------------------------
Input Error
---------------------------
Roll up or down past the first or last record in file.
---------------------------
OK
---------------------------"""

#Cell Styles:
cellFont = xsl.styles.Font(name='Calibri',
                size=14,
                bold=False,
                italic=False,
                vertAlign=None,
                underline='none',
                strike=False,
                color='FF000000')
CellAlign = xsl.styles.Alignment(horizontal="center", vertical="bottom")

try:
    scanTitlePos = pcClickLocs[scriptRunner]["scanTitlePos"]
except:
    scanTitlePos = pcClickLocs["Default"]["scanTitlePos"]
try:
    mainScreenOptions = pcClickLocs[scriptRunner]["mainScreenOptions"]
except:
    mainScreenOptions = pcClickLocs["Default"]["mainScreenOptions"]
try:
    headerInputPos = pcClickLocs[scriptRunner]["headerInputPos"]
except:
    headerInputPos = pcClickLocs["Default"]["headerInputPos"]
try:
    HeaderStatus = pcClickLocs[scriptRunner]["HeaderStatus"]
except:
    HeaderStatus = pcClickLocs["Default"]["HeaderStatus"]
try:
    ASNStatus = pcClickLocs[scriptRunner]["ASNStatus"]
except:
    ASNStatus = pcClickLocs["Default"]["ASNStatus"]
try:
    NumHeadersCreated = pcClickLocs[scriptRunner]["NumHeadersCreated"]
except:
    NumHeadersCreated = pcClickLocs["Default"]["NumHeadersCreated"]
try:
    ProcArea = pcClickLocs[scriptRunner]["ProcArea"]
except:
    ProcArea = pcClickLocs["Default"]["ProcArea"]
try:
    DeptNum = pcClickLocs[scriptRunner]["DeptNum"]
except:
    DeptNum = pcClickLocs["Default"]["DeptNum"]
try:
    PLdate = pcClickLocs[scriptRunner]["PLdate"]
except:
    PLdate = pcClickLocs["Default"]["PLdate"]
try:
    PLdateListStart = pcClickLocs[scriptRunner]["PLdateListStart"]
except:
    PLdateListStart = pcClickLocs["Default"]["PLdateListStart"]
try:
    PLselector = pcClickLocs[scriptRunner]["PLselector"]
except:
    PLselector = pcClickLocs["Default"]["PLselector"]
try:
    selectDesiredChain = pcClickLocs[scriptRunner]["selectDesiredChain"]
except:
    selectDesiredChain = pcClickLocs["Default"]["selectDesiredChain"]
try:
    EnterKeytrolTitle = pcClickLocs[scriptRunner]["EnterKeytrolTitle"]
except:
    EnterKeytrolTitle = pcClickLocs["Default"]["EnterKeytrolTitle"]
try:
    pListAddClick = pcClickLocs[scriptRunner]["pListAddClick"]
except:
    pListAddClick = pcClickLocs["Default"]["pListAddClick"]
try:
    pageTitle = pcClickLocs[scriptRunner]["pageTitle"]
except:
    pageTitle = pcClickLocs["Default"]["pageTitle"]
try:
    pListPosInput = pcClickLocs[scriptRunner]["PLISTPosTo"]
except:
    pListPosInput = pcClickLocs["Default"]["PLISTPosTo"]
try:
    keytrolPosInput = pcClickLocs[scriptRunner]["PLISTKeytrolPosTo"]
except:
    keytrolPosInput = pcClickLocs["Default"]["PLISTKeytrolPosTo"]
try:
    FullPLScreen = pcClickLocs[scriptRunner]["FullPLScreen"]
except:
    FullPLScreen = pcClickLocs["Default"]["FullPLScreen"]
try:
    PLFirstRowKeytrol = pcClickLocs[scriptRunner]["PListFirstRowKeytrol"]
except:
    PLFirstRowKeytrol = pcClickLocs["Default"]["PListFirstRowKeytrol"]
try:
    PLSecondRowKeytrol = pcClickLocs[scriptRunner]["PListSecondRowKeytrol"]
except:
    PLSecondRowKeytrol = pcClickLocs["Default"]["PListSecondRowKeytrol"]
try:
    PLArea = pcClickLocs[scriptRunner]["PListArea"]
except:
    PLArea = pcClickLocs["Default"]["PListArea"]
try:
    PLDept = pcClickLocs[scriptRunner]["PListDept"]
except:
    PLDept = pcClickLocs["Default"]["PListDept"]
try:
    PLPlts = pcClickLocs[scriptRunner]["PListPlts"]
except:
    PLPlts = pcClickLocs["Default"]["PListPlts"]
try:
    PLStatus = pcClickLocs[scriptRunner]["PListStatus"]
except:
    PLStatus = pcClickLocs["Default"]["PListStatus"]
try:
    PLBank = pcClickLocs[scriptRunner]["PListLURHdr"]
except:
    PLBank = pcClickLocs["Default"]["PListLURHdr"]
try:
    PLpo = pcClickLocs[scriptRunner]["PLPo"]
except:
    PLpo = pcClickLocs["Default"]["PLPo"]
try:
    PLAction = pcClickLocs[scriptRunner]["PListActionInput"]
except:
    PLAction = pcClickLocs["Default"]["PListActionInput"]
try:
    POInqKeytrolPos = pcClickLocs[scriptRunner]["POInqKeytrol"]
except:
    POInqKeytrolPos = pcClickLocs["Default"]["POInqKeytrol"]
try:
    POInqKeytrolAction = pcClickLocs[scriptRunner]["POActionInput"]
except:
    POInqKeytrolAction = pcClickLocs["Default"]["POActionInput"]
try:
    POKeytrolMessageBox = pcClickLocs[scriptRunner]["KeytrolByPOError"]
except:
    POKeytrolMessageBox = pcClickLocs["Default"]["KeytrolByPOError"]
try:
    hdrUnits = pcClickLocs[scriptRunner]["HeaderUnits"]
except:
    hdrUnits = pcClickLocs["Default"]["HeaderUnits"]
try:
    BottomText = pcClickLocs[scriptRunner]["BottomText"]
except:
    BottomText = pcClickLocs["Default"]["BottomText"]
try:
    VendName = pcClickLocs[scriptRunner]["POVendor"]
except:
    VendName = pcClickLocs["Default"]["POVendor"]

disallowedProcAreas = ['ADWFT', 'ADWNC', 'ADWPT', 'LURAD', 'JWS1', 'JWS2', 'LUDSJ', 'LUDSW', 'LURSJ', 'LURSW', 'EVJCO', 'EVJWL', 'LUDEW', 'LUREW', 'TJU', 'EVMAR', 'EVMCO', 'LUDEM', 'LUREM', 'MCU']
mouseInterval = (PLSecondRowKeytrol[0][1] - PLFirstRowKeytrol[0][1])/2
secondPosInt = mouseInterval/1.3

procRows = 0

folderPath =r"Y:\AC_MC\MC Admin\PRIORITY LIST & ERROR REPORT UPDATE 2024\FY26 Outstanding Priority Keytrols\Macro"
os.chdir(folderPath)
noConfirm = True
while noConfirm:
    date = pg.prompt(text='Input the P-List date (In the format MM/DD/YYYY)', title='P-List date' , default=f"{datetime.date.today().strftime('%m/%d/%Y')}")
    try:
        date = datetime.datetime.strptime(str(date).strip(),"%m/%d/%Y")
        confirm = pg.confirm(text=f"You have inputted {datetime.datetime.strftime(date,"%m/%d/%Y")}, is this correct?", title = "Confirm",  buttons=['Yes', 'No'])
        if confirm == "Yes":
            noConfirm = False
        else:
            noConfirm = True
    except:
        pg.alert(text = "Please enter a dates in the format MM/DD/YYYY",title='Warning', button='OK')

keytrolToUnits = pd.DataFrame({"Keytrol":[],"Area":[] , "Dept" : [],"P.O. #" : [], "Vendor Name" : [], "Plts" : [], "Status" : [],"Units":[]})
pg.getWindowsWithTitle(scanWindowName)[0].activate()
pg.getWindowsWithTitle(scanWindowName)[0].maximize()
pg.moveTo(pageTitle[0][0],pageTitle[0][1])
pg.dragTo(pageTitle[1][0],pageTitle[1][1], duration=0.25)
pg.hotkey("ctrl","c")
while clip.paste().strip() != "Manager":
    pg.alert(text='Please Sign Into Scan! (and go to home screen)', title='User Logon Error', button='OK')
    time.sleep(10)
    pg.moveTo(pageTitle[0][0],pageTitle[0][1])
    pg.dragTo(pageTitle[1][0],pageTitle[1][1], duration=0.25)
    pg.hotkey("ctrl","c")
pg.click(button="left",x=mainScreenOptions[0],y=mainScreenOptions[1],clicks=1)
pg.typewrite(["3",'enter'])
pg.moveTo(pageTitle[0][0],pageTitle[0][1])
pg.dragTo(pageTitle[1][0],pageTitle[1][1], duration=0.25, button='left')
pg.hotkey('ctrl', 'c')
while clip.paste().strip() != "Bulk Supervisor":
    pg.click(button="left",x=mainScreenOptions[0],y=mainScreenOptions[1],clicks=1)
    pg.typewrite(['enter'])
    time.sleep(0.25)
    pg.moveTo(pageTitle[0][0],pageTitle[0][1])
    pg.dragTo(pageTitle[1][0],pageTitle[1][1], duration=0.25, button='left')
    pg.hotkey('ctrl', 'c')
pg.click(button="left",x=mainScreenOptions[0],y=mainScreenOptions[1],clicks=1)
pg.typewrite(["1",'enter'])
pg.moveTo(pageTitle[0][0],pageTitle[0][1])
pg.dragTo(pageTitle[1][0],pageTitle[1][1], duration=0.25)
pg.hotkey('ctrl', 'c')
while clip.paste().strip() != "Priority List Status Summary - 	T.J. Maxx":
    pg.click(button="left",x=mainScreenOptions[0],y=mainScreenOptions[1],clicks=1)
    pg.typewrite(["1",'enter'])
    pg.moveTo(pageTitle[0][0],pageTitle[0][1])
    pg.dragTo(pageTitle[1][0],pageTitle[1][1], duration=0.25, button='left')
    pg.hotkey('ctrl', 'c')
pg.click(pListPosInput[0],pListPosInput[1])
pg.press('del', presses=6)
PLISTdate=datetime.datetime.strftime(date,"%m/%d/%Y")
foundPList = False
counter = 0
lookForPdate = str(PLISTdate)
lookForPdate = datetime.datetime.strptime(lookForPdate,"%m/%d/%Y").date()
newDate = datetime.datetime.strptime("01/01/1825","%m/%d/%Y").date()
while not foundPList:
    pg.moveTo(PLdateListStart[0][0],PLdateListStart[0][1] + (mouseInterval*counter))
    pg.dragTo(PLdateListStart[1][0],PLdateListStart[1][1] + (mouseInterval*counter) + secondPosInt)
    pg.hotkey("ctrl","c")
    if str(clip.paste()).strip() == "":
        newDate = datetime.datetime.strptime("01/01/1825","%m/%d/%Y").date()
    elif "\n" in str(clip.paste()).strip():
        pass
    else:
        copiedDate = str(clip.paste()).strip()
        newDate = datetime.datetime.strptime(copiedDate,"%m/%d/%y").date()
    if newDate == lookForPdate:
        foundPList = True
    elif str(clip.paste()).strip() == "":
        pg.hotkey("pgdn")
        counter = 0
    else:
        counter += 1
pg.click(x=PLselector[0],y=PLdateListStart[0][1] + (mouseInterval*counter),button="left")
pg.typewrite(["5"])
pg.press(["enter"])
pg.moveTo(pageTitle[0][0],pageTitle[0][1])
pg.dragTo(pageTitle[1][0],pageTitle[1][1], duration=0.25, button='left')
pg.hotkey('ctrl', 'c')
while clip.paste().strip() != "Priority List Detail - 	T.J. Maxx":
    pg.click(button="left",x=mainScreenOptions[0],y=mainScreenOptions[1],clicks=1)
    pg.typewrite(["3",'enter'])
    pg.moveTo(pageTitle[0][0],pageTitle[0][1])
    pg.dragTo(pageTitle[1][0],pageTitle[1][1], duration=0.25, button='left')
    pg.hotkey('ctrl', 'c')
# In P-List for Date
pg.click(keytrolPosInput[0],keytrolPosInput[1])
pg.press('del', presses=6)
oldScreen = ""
pg.moveTo(FullPLScreen[0][0],FullPLScreen[0][1])
pg.dragTo(FullPLScreen[1][0],FullPLScreen[1][1])
pg.hotkey("ctrl","c")
newScreen = clip.paste()
pagesScanned = 0
while newScreen != oldScreen:
    oldScreen = newScreen
    counter = 0
    pg.moveTo(PLFirstRowKeytrol[0][0],PLFirstRowKeytrol[0][1] + (mouseInterval * counter))
    pg.dragTo(PLFirstRowKeytrol[1][0],PLFirstRowKeytrol[1][1] + (mouseInterval * counter) + secondPosInt)
    pg.hotkey("ctrl","c")
    while clip.paste().strip() != "":
        pg.moveTo(PLFirstRowKeytrol[0][0],PLFirstRowKeytrol[0][1] + (mouseInterval * counter))
        pg.dragTo(PLFirstRowKeytrol[1][0],PLFirstRowKeytrol[1][1] + (mouseInterval * counter) + secondPosInt)
        pg.hotkey("ctrl","c")
        if clip.paste().strip() in keytrolToUnits["Keytrol"].apply(str).to_list():
                pass
        else:
            pg.moveTo(PLFirstRowKeytrol[0][0],PLFirstRowKeytrol[0][1] + (mouseInterval * counter))
            pg.dragTo(PLFirstRowKeytrol[1][0],PLFirstRowKeytrol[1][1] + (mouseInterval * counter) + secondPosInt)
            pg.hotkey("ctrl","c")
            if "\n" in clip.paste().strip():
                pass
            elif clip.paste().strip() == "":
                pass
            else:
                keytrol = clip.paste().replace("\n","").strip()
                units = 0
                pg.moveTo(PLArea[0][0],PLFirstRowKeytrol[0][1] + (mouseInterval * counter))
                pg.dragTo(PLArea[1][0],PLFirstRowKeytrol[1][1] + (mouseInterval * counter) + secondPosInt)
                pg.hotkey("ctrl","c")
                Area = clip.paste().strip()
                pg.moveTo(PLpo[0][0],PLFirstRowKeytrol[0][1] + (mouseInterval * counter))
                pg.dragTo(PLpo[1][0],PLFirstRowKeytrol[1][1] + (mouseInterval * counter) + secondPosInt)
                pg.hotkey("ctrl","c")
                PurchaseOrder = clip.paste().strip()
                if Area in disallowedProcAreas or PurchaseOrder[:2] != "60":
                    pass
                else:
                    try:
                        PurchaseOrder = int(PurchaseOrder)
                    except:
                        PurchaseOrder = str(PurchaseOrder)
                    pg.moveTo(PLDept[0][0],PLFirstRowKeytrol[0][1] + (mouseInterval * counter))
                    pg.dragTo(PLDept[1][0],PLFirstRowKeytrol[1][1] + (mouseInterval * counter) + secondPosInt)
                    pg.hotkey("ctrl","c")
                    dept = clip.paste().strip()
                    pg.moveTo(PLPlts[0][0],PLFirstRowKeytrol[0][1] + (mouseInterval * counter))
                    pg.dragTo(PLPlts[1][0],PLFirstRowKeytrol[1][1] + (mouseInterval * counter) + secondPosInt)
                    pg.hotkey("ctrl","c")
                    Plts = clip.paste().strip()
                    pg.moveTo(PLStatus[0][0],PLFirstRowKeytrol[0][1] + (mouseInterval * counter))
                    pg.dragTo(PLStatus[1][0],PLFirstRowKeytrol[1][1] + (mouseInterval * counter) + secondPosInt)
                    pg.hotkey("ctrl","c")
                    Status = clip.paste().strip()
                    pg.moveTo(VendName[0][0],PLFirstRowKeytrol[0][1] + (mouseInterval * counter))
                    pg.dragTo(VendName[1][0],PLFirstRowKeytrol[1][1] + (mouseInterval * counter) + secondPosInt)
                    pg.hotkey("ctrl","c")
                    VendorName = clip.paste().strip()
                    pg.click(PLAction[0],PLFirstRowKeytrol[0][1] + (mouseInterval * counter))
                    pg.typewrite(["3"])
                    pg.press(["enter"])
                    pg.moveTo(pageTitle[0][0],pageTitle[0][1])
                    pg.dragTo(pageTitle[1][0],pageTitle[1][1], duration=0.25, button='left')
                    pg.hotkey('ctrl', 'c')
                    while clip.paste().strip() != "Keytrol Inquiry By PO":
                        time.sleep(0.25)
                        pg.moveTo(pageTitle[0][0],pageTitle[0][1])
                        pg.dragTo(pageTitle[1][0],pageTitle[1][1], duration=0.25, button='left')
                        pg.hotkey('ctrl', 'c')
                    pg.press(["esc"])
                    pg.moveTo(POInqKeytrolPos[0][0],POInqKeytrolPos[0][1])
                    pg.dragTo(POInqKeytrolPos[1][0],POInqKeytrolPos[1][1])
                    pg.hotkey("ctrl","c")
                    newKey = clip.paste().strip()
                    poCount = 0
                    pg.press(["esc"])
                    pgDnCount = 0
                    recounts = 0
                    while newKey != keytrol:
                        if recounts > 10:
                            pass
                        else:
                            pg.press(["esc"])
                            pg.moveTo(POInqKeytrolPos[0][0],POInqKeytrolPos[0][1] + (mouseInterval * poCount))
                            pg.dragTo(POInqKeytrolPos[1][0],POInqKeytrolPos[1][1] + (mouseInterval * poCount) + secondPosInt)
                            pg.hotkey("ctrl","c")
                            pg.press(["esc"])
                            newKey = clip.paste().strip()
                            pg.press(["esc"])
                            pg.moveTo(BottomText[0][0],BottomText[0][1])
                            pg.dragTo(BottomText[1][0],BottomText[1][1])
                            pg.hotkey("ctrl","c")
                            pg.press(["esc"])
                            bottomStatus = clip.paste().strip().replace(" ","")
                            if newKey == "":
                                if bottomStatus == "Bottom":
                                    pg.press("pgup",presses=pgDnCount)
                                    poCount = 0
                                    recounts += 1
                                else:
                                    pg.hotkey("pgdn")
                                    pgDnCount += 1
                                    poCount = 0
                            elif newKey != keytrol:
                                poCount += 1
                    if recounts <= 10:
                        pg.click(POInqKeytrolAction[0],POInqKeytrolPos[0][1] + (mouseInterval * poCount))
                        pg.typewrite(["5"])
                        pg.press(["enter"])
                        time.sleep(0.25)
                        pg.moveTo(POKeytrolMessageBox[0][0],POKeytrolMessageBox[0][1])
                        pg.dragTo(POKeytrolMessageBox[1][0],POKeytrolMessageBox[1][1])
                        pg.hotkey("ctrl","c")
                        if clip.paste().strip().replace(".","") == "No records to display":
                            units = 0
                        else:
                            pg.moveTo(pageTitle[0][0],pageTitle[0][1])
                            pg.dragTo(pageTitle[1][0],pageTitle[1][1], duration=0.25, button='left')
                            pg.hotkey('ctrl', 'c')
                            while clip.paste().strip() != "Header Inquiry":
                                pg.click(button="left",x=mainScreenOptions[0],y=mainScreenOptions[1],clicks=1)
                                pg.click(POInqKeytrolAction[0],POInqKeytrolPos[1][1] + (mouseInterval * poCount))
                                pg.typewrite(["5"])
                                pg.press(["enter"])
                                pg.press(["esc"])
                                pg.moveTo(pageTitle[0][0],pageTitle[0][1])
                                pg.dragTo(pageTitle[1][0],pageTitle[1][1], duration=0.25, button='left')
                                pg.hotkey('ctrl', 'c')
                            pg.press(["esc"])
                            pg.moveTo(POKeytrolMessageBox[0][0],POKeytrolMessageBox[0][1])
                            pg.dragTo(POKeytrolMessageBox[1][0],POKeytrolMessageBox[1][1])
                            pg.hotkey("ctrl","c")
                            pg.press(["esc"])
                            if clip.paste().strip() != "":
                                units = 0
                            else:
                                pageEnd = ""
                                while pageEnd != "Bottom":
                                    pg.press(["esc"])
                                    pg.moveTo(hdrUnits[0][0],hdrUnits[0][1])
                                    pg.dragTo(hdrUnits[1][0],BottomText[0][1])
                                    pg.hotkey("ctrl","c")
                                    pg.press(["esc"])
                                    headers = clip.paste().strip().replace(" ","")
                                    headers = headers.split("\n")
                                    try:
                                        headers = [int(i) for i in headers]
                                        units += sum(headers)
                                    except:
                                        units += 0
                                    pg.moveTo(BottomText[0][0],BottomText[0][1])
                                    pg.dragTo(BottomText[1][0],BottomText[1][1])
                                    pg.hotkey("ctrl","c")
                                    pageEnd = clip.paste().replace("\n","").strip()
                                    if pageEnd != "Bottom":
                                        if pageEnd == "":
                                            pageEnd = "Bottom"
                                        else:
                                            pg.hotkey("pgdn")
                    else:
                        units = 0
                    keytrol = keytrol.replace("\n","")
                    Status = Status.replace("\n","")
                    try:
                        units = int(units)
                    except:
                        units = str(units)
                    try:
                        Plts = int(Plts)
                    except:
                        Plts = str(Plts)
                    try:
                        dept = int(dept)
                    except:
                        dept = str(dept)
                    try:
                        keytrol = int(keytrol)
                    except:
                        keytrol = str(keytrol)
                    try:
                        #pd.DataFrame({"Keytrol":[], "Dept" : [],"P.O. #" : [], "Vendor Name" : [], "Plts" : [], "Status" : [],"Units":[]})
                        keytrolToUnits.loc[len(keytrolToUnits)] = {"Keytrol":keytrol, "Area":Area ,"Dept" : dept, "P.O. #" : PurchaseOrder, "Vendor Name" : VendorName, "Plts" : Plts, "Status" : Status,"Units":units}
                        print(f"{keytrol} information fetched")
                        procRows += 1
                    except:
                        #pd.DataFrame({"Keytrol":[], "Dept" : [],"P.O. #" : [], "Vendor Name" : [], "Plts" : [], "Status" : [],"Units":[]})
                        keytrolToUnits = pd.DataFrame({"Keytrol":[keytrol], "Area":[Area] ,"Dept" : [dept], "P.O. #" : [PurchaseOrder], "Vendor Name" : [VendorName], "Plts" : [Plts], "Status" : [Status],"Units":[units]})
                        print(f"{keytrol} information fetched")
                        procRows += 1
                    units = 0
                    #Get Back to P-List
                    pg.moveTo(pageTitle[0][0],pageTitle[0][1])
                    pg.dragTo(pageTitle[1][0],pageTitle[1][1], duration=0.25, button='left')
                    pg.hotkey('ctrl', 'c')
                    while clip.paste().strip() != "Priority List Detail - 	T.J. Maxx":
                        if clip.paste().strip().replace(" ","").replace("\n","").replace("\t","") == "":
                            time.sleep(1)
                        elif clip.paste().strip() == "Priority List Status Summary - 	T.J. Maxx":
                            PLISTdate=datetime.datetime.strftime(date,"%m/%d/%Y")
                            foundPList = False
                            counter = 0
                            lookForPdate = str(PLISTdate)
                            lookForPdate = datetime.datetime.strptime(lookForPdate,"%m/%d/%Y").date()
                            while not foundPList:
                                pg.moveTo(PLdateListStart[0][0],PLdateListStart[0][1] + (mouseInterval*counter))
                                pg.dragTo(PLdateListStart[1][0],PLdateListStart[1][1] + (mouseInterval*counter) + secondPosInt)
                                pg.hotkey("ctrl","c")
                                if str(clip.paste()).strip() == "":
                                    newDate = datetime.datetime.strptime("01/01/1825","%m/%d/%Y").date()
                                elif "\n" in str(clip.paste()).strip():
                                    pass
                                else:
                                    copiedDate = str(clip.paste()).strip()
                                    newDate = datetime.datetime.strptime(copiedDate,"%m/%d/%y").date()
                                if newDate == lookForPdate:
                                    foundPList = True
                                elif str(clip.paste()).strip() == "":
                                    pg.hotkey("pgdn")
                                    counter = 0
                                else:
                                    counter += 1
                            pg.click(x=PLselector[0],y=PLdateListStart[0][1] + (mouseInterval*counter),button="left")
                            pg.typewrite(["5"])
                            pg.press(["enter"])
                            pg.moveTo(pageTitle[0][0],pageTitle[0][1])
                            pg.dragTo(pageTitle[1][0],pageTitle[1][1], duration=0.25, button='left')
                            pg.hotkey('ctrl', 'c')
                            while clip.paste().strip() != "Priority List Detail - 	T.J. Maxx":
                                pg.click(button="left",x=mainScreenOptions[0],y=mainScreenOptions[1],clicks=1)
                                pg.typewrite(["3",'enter'])
                                pg.moveTo(pageTitle[0][0],pageTitle[0][1])
                                pg.dragTo(pageTitle[1][0],pageTitle[1][1], duration=0.25, button='left')
                                pg.hotkey('ctrl', 'c')
                            # In P-List for Date
                            pg.click(keytrolPosInput[0],keytrolPosInput[1])
                            pg.press('del', presses=6)
                            pg.typewrite([str(keytrol),"enter"])
                            counter = 0
                        else:
                            pg.hotkey("f12")
                            time.sleep(0.25)
                            pg.moveTo(pageTitle[0][0],pageTitle[0][1])
                            pg.dragTo(pageTitle[1][0],pageTitle[1][1], duration=0.25, button='left')
                            pg.hotkey('ctrl', 'c')
                        pg.moveTo(pageTitle[0][0],pageTitle[0][1])
                        pg.dragTo(pageTitle[1][0],pageTitle[1][1], duration=0.25, button='left')
                        pg.hotkey('ctrl', 'c')
                    pg.moveTo(PLFirstRowKeytrol[0][0],PLFirstRowKeytrol[0][1] + (mouseInterval * counter))
                    pg.dragTo(PLFirstRowKeytrol[1][0],PLFirstRowKeytrol[1][1] + (mouseInterval * counter) + secondPosInt)
                    pg.hotkey("ctrl","c")
        counter += 1
    pagesScanned += 1
    pg.hotkey("pgdn")
    pg.moveTo(FullPLScreen[0][0],FullPLScreen[0][1])
    pg.dragTo(FullPLScreen[1][0],FullPLScreen[1][1])
    pg.hotkey("ctrl","c")
    newScreen = clip.paste()
keytrolToUnits.drop_duplicates(inplace=True,ignore_index=True)
pg.hotkey("f12")
pg.hotkey("f12")
pg.click(button="left",x=mainScreenOptions[0],y=mainScreenOptions[1],clicks=1)
pg.typewrite(["1",'enter'])
pg.moveTo(pageTitle[0][0],pageTitle[0][1])
pg.dragTo(pageTitle[1][0],pageTitle[1][1], duration=0.25)
pg.hotkey('ctrl', 'c')
while clip.paste().strip() != "Priority List Status Summary - 	T.J. Maxx":
    pg.click(button="left",x=mainScreenOptions[0],y=mainScreenOptions[1],clicks=1)
    pg.typewrite(["1",'enter'])
    pg.moveTo(pageTitle[0][0],pageTitle[0][1])
    pg.dragTo(pageTitle[1][0],pageTitle[1][1], duration=0.25, button='left')
    pg.hotkey('ctrl', 'c')
pg.click(pListPosInput[0],pListPosInput[1])
pg.press('del', presses=6)

while clip.paste().strip() != "Manager":
                pg.hotkey("f12")
                time.sleep(0.25)
                pg.moveTo(pageTitle[0][0],pageTitle[0][1])
                pg.dragTo(pageTitle[1][0],pageTitle[1][1], duration=0.25)
                pg.hotkey("ctrl","c")
                time.sleep(0.25)

os.chdir("P-List Units")
with open(f"{datetime.datetime.strftime(date,"%m-%d-%Y")} P-List units.xlsx","wb") as f:
    keytrolToUnits.to_excel(f,sheet_name=f"{datetime.datetime.strftime(date,"%m-%d-%Y")} P-List units",index=False,na_rep='NA', inf_rep='INFINITY')

totalTime = time.time() - StartTime

print(f"Total Rows Processed: {procRows}")
print(f"Total runtime was {round(totalTime,2)} seconds, or {round(totalTime/60,2)} minutes")
print(f"Average time per row: {round(totalTime,2)/procRows} seconds, {round(totalTime/60,2)/procRows} minutes")