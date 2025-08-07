'''
Maykl Yakubovsky (MC Intern Summer of 2025)
Date Created: 06/27/2025
Last Edit: 07/29/2025
Title/Function: Script to setup an entry into the ScanClickLocations.json file for proper macro operation on different hosts

To-Do:


Complete:
[X] Add a mouse postion collector for the Chain Selection Action Entry for automatic select chain popup bypass
'''
#537574

import pyautogui as pg
import time
import json
import pyperclip as clip
import datetime
import copy
import socket
from pynput import mouse
import os

# Controls how long the delay between inputs for failsafe is (0.1 by default, 0.01 seems to just barely work if the mouse is moved quickly)
#0.01 is too fast for scan to work right
pg.PAUSE = 0.05

clicks = 0
lastClick = []

def on_click(x, y, button, pressed):
    global clicks
    global lastClick
    if pressed == True:
        lastClick = [(x, y)]
    else:
        lastClick.append((x,y))
    clicks += 1
    if clicks >= 2:
        listener.stop()


scriptRunner = str(socket.gethostname())
print(f"JSON setup function running on : {scriptRunner}")

pcClickLocs = {}
fileName = str(os.path.basename(__file__))
OverallFolder = str(__file__).replace(fileName,"")
os.chdir(OverallFolder)
os.chdir("Files")
with open("ScanClickLocations.json","r") as f:
    pcClickLocs = json.load(f)

run = True
scanWindowName= "Worcester - Micro Focus Rumba+ Desktop"

if scriptRunner in pcClickLocs.keys():
    selection = pg.confirm(text='This PC seems to have been setup previously, would you like to overwrite the existing setup?', title='Setup Completed', buttons=['Yes', 'No'])
    if selection == "No":
        run = False

if run:
    pcClickLocs[scriptRunner] = copy.deepcopy(pcClickLocs["Default"])
    '''
    ['scanTitlePos', 'mainScreenOptions', 'loginUserPos', 
    'headerInputPos', 'HeaderStatus', 'ASNStatus', 
    'NumHeadersCreated', 'ProcArea', 'DeptNum', 
    'PLdate', 'PLdateListStart', 'PLselector', 
    'selectDesiredChain', 'EnterKeytrolTitle', 'pListAddClick', 'pageTitle']
    '''
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please Sign Into Scan and go the the home screen, and once you press OK press the first and last character in "SCAN System Control and Automation Network"', title='Scan Title Position', button='OK')
        pg.getWindowsWithTitle(scanWindowName)[0].activate()
        pg.getWindowsWithTitle(scanWindowName)[0].maximize()
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['scanTitlePos'] = []
        pcClickLocs[scriptRunner]['scanTitlePos'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['scanTitlePos'])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['scanTitlePos'].append(lastClick[0])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['scanTitlePos'][0][0],pcClickLocs[scriptRunner]['scanTitlePos'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['scanTitlePos'][1][0],pcClickLocs[scriptRunner]['scanTitlePos'][1][1])
        selection = pg.confirm(text='Is the selected text correct?', title='Title Selection Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":
            goodFlag = True
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please Sign Into Scan and go the the home screen, and once you press OK click above the first underline in "Option: __"', title='Option input Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        
        pcClickLocs[scriptRunner]['mainScreenOptions'] = lastClick[0]
        pg.click(pcClickLocs[scriptRunner]['mainScreenOptions'][0],pcClickLocs[scriptRunner]['mainScreenOptions'][1])
        time.sleep(0.25)
        selection = pg.confirm(text='Is the cursor in the options input area?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":
            goodFlag = True
    pg.click(pcClickLocs[scriptRunner]['mainScreenOptions'][0],pcClickLocs[scriptRunner]['mainScreenOptions'][1])
    pg.typewrite(["2","enter"])
    pg.click(pcClickLocs[scriptRunner]['mainScreenOptions'][0],pcClickLocs[scriptRunner]['mainScreenOptions'][1])
    pg.typewrite(["6","enter"])
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please press "OK" then click the first space in the header input section in the inquiry screen', title='Header input Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        
        pcClickLocs[scriptRunner]['headerInputPos'] = lastClick[0]
        pg.click(pcClickLocs[scriptRunner]['headerInputPos'][0],pcClickLocs[scriptRunner]['headerInputPos'][1])
        time.sleep(0.25)
        selection = pg.confirm(text='Is the cursor in the header input area?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":
            goodFlag = True
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please press "OK" then click before and after "Enter Keytrol to Query/Edit" (You click on the space before "E" and the space after "t")', title='Title Selection Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['EnterKeytrolTitle'] = []
        pcClickLocs[scriptRunner]['EnterKeytrolTitle'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['EnterKeytrolTitle'])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['EnterKeytrolTitle'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['EnterKeytrolTitle'])
        pg.moveTo(pcClickLocs[scriptRunner]['EnterKeytrolTitle'][0][0],pcClickLocs[scriptRunner]['EnterKeytrolTitle'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['EnterKeytrolTitle'][1][0],pcClickLocs[scriptRunner]['EnterKeytrolTitle'][1][1])
        time.sleep(0.25)
        selection = pg.confirm(text='Is "Enter Keytrol to Query/Edit" highlighted completely?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":
            goodFlag = True
    selection = pg.confirm(text='If you have a keytrol # that will trigger the "Select Desired Chain" Screen, please enter it and press "Yes", otherwise press "No" and the default value will be used. This may cause errors when a header that generates this screen appears', title='Input Confirmation', buttons=['Yes', 'No'])
    if selection == "Yes":
         goodFlag = False
         while not goodFlag:
            pg.alert(text='Please press "OK" then click before and after "Select Desired Chain" (You click on the space before "S" and the space after "n")', title='Title Selection Position', button='OK')
            with mouse.Listener(on_click=on_click) as listener:
                listener.join()
            pcClickLocs[scriptRunner]['selectDesiredChain'] = []
            pcClickLocs[scriptRunner]['selectDesiredChain'].append(lastClick[0])
            print(pcClickLocs[scriptRunner]['selectDesiredChain'])
            time.sleep(0.25)
            with mouse.Listener(on_click=on_click) as listener:
                listener.join()
            pcClickLocs[scriptRunner]['selectDesiredChain'].append(lastClick[0])
            print(pcClickLocs[scriptRunner]['selectDesiredChain'])
            pg.moveTo(pcClickLocs[scriptRunner]['selectDesiredChain'][0][0],pcClickLocs[scriptRunner]['selectDesiredChain'][0][1])
            pg.dragTo(pcClickLocs[scriptRunner]['selectDesiredChain'][1][0],pcClickLocs[scriptRunner]['selectDesiredChain'][1][1])
            time.sleep(0.25)
            selection = pg.confirm(text='Is "Select Desired Chain" highlighted completely?', title='Input Confirmation', buttons=['Yes', 'No'])
            if selection == "Yes":
                goodFlag = True
            goodFlag = False
            while not goodFlag:
                pg.alert(text='Please press "OK" then click on the action input for the tjmaxx chain (the underscore)', title='Title Selection Position', button='OK')
                with mouse.Listener(on_click=on_click) as listener:
                    listener.join()
                pcClickLocs[scriptRunner]['selectDesiredAction'] = lastClick[0]
                print(pcClickLocs[scriptRunner]['selectDesiredAction'])
                time.sleep(0.25)
                print(pcClickLocs[scriptRunner]['selectDesiredAction'])
                pg.click(pcClickLocs[scriptRunner]['selectDesiredAction'][0],pcClickLocs[scriptRunner]['selectDesiredAction'][1])
                time.sleep(0.25)
                selection = pg.confirm(text='Is the chain input selected?', title='Input Confirmation', buttons=['Yes', 'No'])
                if selection == "Yes":
                    goodFlag = True
    else:
        pcClickLocs[scriptRunner]['selectDesiredAction'] = pcClickLocs["Default"]['selectDesiredAction']
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please enter a test keytrol and once "OK" is click the first and last whitespaces in the Header Status section', title='Option input Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['HeaderStatus'] = []
        pcClickLocs[scriptRunner]['HeaderStatus'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['HeaderStatus'])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['HeaderStatus'].append(lastClick[0])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['HeaderStatus'][0][0],pcClickLocs[scriptRunner]['HeaderStatus'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['HeaderStatus'][1][0],pcClickLocs[scriptRunner]['HeaderStatus'][1][1])
        time.sleep(0.25)
        selection = pg.confirm(text='Is the header status highlighted without any extra text?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please enter a test keytrol and once "OK" is pressed highlight the first and last whitespace in ASN Status', title='Option input Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['ASNStatus'] = []
        pcClickLocs[scriptRunner]['ASNStatus'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['ASNStatus'])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['ASNStatus'].append(lastClick[0])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['ASNStatus'][0][0],pcClickLocs[scriptRunner]['ASNStatus'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['ASNStatus'][1][0],pcClickLocs[scriptRunner]['ASNStatus'][1][1])
        time.sleep(0.25)
        selection = pg.confirm(text='Is the ASN status highlighted without any extra text?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please enter a test keytrol and once "OK" is pressed click the first and last whitespace for # Headers Created', title='Option input Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['NumHeadersCreated'] = []
        pcClickLocs[scriptRunner]['NumHeadersCreated'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['NumHeadersCreated'])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['NumHeadersCreated'].append(lastClick[0])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['NumHeadersCreated'][0][0],pcClickLocs[scriptRunner]['NumHeadersCreated'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['NumHeadersCreated'][1][0],pcClickLocs[scriptRunner]['NumHeadersCreated'][1][1])
        time.sleep(0.25)
        selection = pg.confirm(text='Is the # Headers Created highlighted without any extra text?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please enter a test keytrol and once "OK" is pressed click the first and last whitespace for Proc Area', title='Option input Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['ProcArea'] = []
        pcClickLocs[scriptRunner]['ProcArea'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['ProcArea'])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['ProcArea'].append(lastClick[0])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['ProcArea'][0][0],pcClickLocs[scriptRunner]['ProcArea'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['ProcArea'][1][0],pcClickLocs[scriptRunner]['ProcArea'][1][1])
        time.sleep(0.25)
        selection = pg.confirm(text='Is the Proc Area highlighted without any extra text?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please enter a test keytrol and once "OK" is pressed click the first and last whitespace for Dept.', title='Option input Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['DeptNum'] = []
        pcClickLocs[scriptRunner]['DeptNum'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['DeptNum'])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['DeptNum'].append(lastClick[0])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['DeptNum'][0][0],pcClickLocs[scriptRunner]['DeptNum'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['DeptNum'][1][0],pcClickLocs[scriptRunner]['DeptNum'][1][1])
        time.sleep(0.25)
        selection = pg.confirm(text='Is the Department Number highlighted without any extra text?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    pg.hotkey("f11")
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please enter a test keytrol and once "OK" is pressed click the first and last whitespace for P/L Date', title='Option input Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PLdate'] = []
        pcClickLocs[scriptRunner]['PLdate'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['PLdate'])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PLdate'].append(lastClick[0])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['PLdate'][0][0],pcClickLocs[scriptRunner]['PLdate'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['PLdate'][1][0],pcClickLocs[scriptRunner]['PLdate'][1][1])
        time.sleep(0.25)
        selection = pg.confirm(text='Is the P-List Date highlighted without any extra text?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    pg.hotkey("f12")
    time.sleep(0.25)
    pg.hotkey("f12")
    time.sleep(0.25)
    pg.hotkey("f12")
    time.sleep(0.25)
    pg.hotkey("f12")
    time.sleep(0.25)
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please click on the first and last whitespace for the page title (should be "Manager")', title='Page Title Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['pageTitle'] = []
        pcClickLocs[scriptRunner]['pageTitle'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['pageTitle'])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['pageTitle'].append(lastClick[0])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['pageTitle'][0][0],pcClickLocs[scriptRunner]["pageTitle"][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['pageTitle'][1][0],pcClickLocs[scriptRunner]["pageTitle"][1][1])
        time.sleep(0.25)
        selection = pg.confirm(text='Is page title highlighted with all whitespace surrounding it included (and no extra text)?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    pg.click(x=pcClickLocs[scriptRunner]["mainScreenOptions"][0],y=pcClickLocs[scriptRunner]["mainScreenOptions"][1],button="left")
    pg.typewrite(["3"])
    pg.press(["enter"])
    pg.moveTo(pcClickLocs[scriptRunner]['pageTitle'][0][0],pcClickLocs[scriptRunner]['pageTitle'][0][1])
    pg.dragTo(pcClickLocs[scriptRunner]['pageTitle'][1][0],pcClickLocs[scriptRunner]['pageTitle'][1][1])
    pg.hotkey("ctrl","c")
    while clip.paste().strip() != 'Bulk Supervisor':
        print("waiting on bulk screen")
        pg.click(x=pcClickLocs[scriptRunner]["mainScreenOptions"][0],y=pcClickLocs[scriptRunner]["mainScreenOptions"][1],button="left")
        pg.typewrite(["3"])
        pg.press(["enter"])
        time.sleep(0.1)
        pg.moveTo(pcClickLocs[scriptRunner]['pageTitle'][0][0],pcClickLocs[scriptRunner]['pageTitle'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['pageTitle'][1][0],pcClickLocs[scriptRunner]['pageTitle'][1][1])
        pg.hotkey("ctrl","c")
    pg.click(x=pcClickLocs[scriptRunner]["mainScreenOptions"][0],y=pcClickLocs[scriptRunner]["mainScreenOptions"][1],button="left")
    pg.typewrite(["1"])
    pg.press(["enter"])
    print('In P-List by Date')
    pg.moveTo(pcClickLocs[scriptRunner]['pageTitle'][0][0],pcClickLocs[scriptRunner]['pageTitle'][0][1])
    pg.dragTo(pcClickLocs[scriptRunner]['pageTitle'][1][0],pcClickLocs[scriptRunner]['pageTitle'][1][1])
    pg.hotkey("ctrl","c")
    while clip.paste().strip() != 'Priority List Status Summary - \tT.J. Maxx':
        print("waiting on p-list screen")
        pg.click(x=pcClickLocs[scriptRunner]["mainScreenOptions"][0],y=pcClickLocs[scriptRunner]["mainScreenOptions"][1],button="left")
        pg.typewrite(["1"])
        pg.press(["enter"])
        time.sleep(0.1)
        pg.moveTo(pcClickLocs[scriptRunner]['pageTitle'][0][0],pcClickLocs[scriptRunner]['pageTitle'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['pageTitle'][1][0],pcClickLocs[scriptRunner]['pageTitle'][1][1])
        pg.hotkey("ctrl","c")
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please select the First PlDate Row (should be "12/07/24") by clicking on the first and last characters (1 and 4 in example case, but should include whitespace if any exist)', title='P-List row Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PLdateListStart'] = []
        pcClickLocs[scriptRunner]['PLdateListStart'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['PLdateListStart'])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PLdateListStart'].append(lastClick[0])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['PLdateListStart'][0][0],pcClickLocs[scriptRunner]["PLdateListStart"][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['PLdateListStart'][1][0],pcClickLocs[scriptRunner]["PLdateListStart"][1][1])
        time.sleep(0.25)
        selection = pg.confirm(text='Is P-List highlighted with no whitespace surrounding it (and no extra text)?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please click on the first position for the "Position To" input', title='P-List position input', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PLISTPosTo'] = lastClick[0]
        pg.click(pcClickLocs[scriptRunner]['PLISTPosTo'][0],pcClickLocs[scriptRunner]['PLISTPosTo'][1])
        time.sleep(0.25)
        selection = pg.confirm(text='Is the Position input for the P-List selected?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    pg.click(pcClickLocs[scriptRunner]['PLISTPosTo'][0],pcClickLocs[scriptRunner]['PLISTPosTo'][1])
    pg.press('del', presses=6)
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please select the action input on the first p-list date (should be "12/07/24") without any whitespace', title='P-List row Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PLselector'] = lastClick[0]
        pg.click(pcClickLocs[scriptRunner]['PLselector'][0],pcClickLocs[scriptRunner]['PLselector'][1])
        time.sleep(0.25)
        selection = pg.confirm(text='Is the action section for the first P-List date selected?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    pg.click(pcClickLocs[scriptRunner]['PLselector'][0],pcClickLocs[scriptRunner]['PLselector'][1])
    pg.typewrite(["5"])
    pg.press(["enter"])
    pg.hotkey("f6")
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please click on the first position for the header input', title='P-List header input Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['pListAddClick'] = lastClick[0]
        pg.click(pcClickLocs[scriptRunner]['pListAddClick'][0],pcClickLocs[scriptRunner]['pListAddClick'][1])
        time.sleep(0.25)
        selection = pg.confirm(text='Is the Header input for the P-List selected?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    #"PLISTPosTo","FullPLScreen","PListFirstRowKeytrol","PListSecondRowKeytrol",
    pg.hotkey("f12")
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please click on the first position for "Position To Keytrol" input', title='P-List header input Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PLISTKeytrolPosTo'] = lastClick[0]
        pg.click(pcClickLocs[scriptRunner]['PLISTKeytrolPosTo'][0],pcClickLocs[scriptRunner]['PLISTKeytrolPosTo'][1])
        time.sleep(0.25)
        selection = pg.confirm(text='Is the Keytrol input selected?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please click on first and last char in the first row\'s keytrol', title='First Row Keytrol Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PListFirstRowKeytrol'] = []
        pcClickLocs[scriptRunner]['PListFirstRowKeytrol'].append(lastClick[0])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PListFirstRowKeytrol'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['PListFirstRowKeytrol'])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['PListFirstRowKeytrol'][0][0],pcClickLocs[scriptRunner]['PListFirstRowKeytrol'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['PListFirstRowKeytrol'][1][0],pcClickLocs[scriptRunner]['PListFirstRowKeytrol'][1][1])
        time.sleep(0.25)
        selection = pg.confirm(text='is the Keytrol selected?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please select first and last char in the Second row\'s keytrol', title='Second Row Keytrol Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PListSecondRowKeytrol'] = []
        pcClickLocs[scriptRunner]['PListSecondRowKeytrol'].append(lastClick[0])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PListSecondRowKeytrol'].append(lastClick[0])
        time.sleep(0.25)
        print(pcClickLocs[scriptRunner]['PListSecondRowKeytrol'])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['PListSecondRowKeytrol'][0][0],pcClickLocs[scriptRunner]['PListSecondRowKeytrol'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['PListSecondRowKeytrol'][1][0],pcClickLocs[scriptRunner]['PListSecondRowKeytrol'][1][1])
        time.sleep(0.25)
        selection = pg.confirm(text='is the second row Keytrol selected?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    #"PListArea","PListDept" ,
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please select first and last char in the first row\'s Area', title='Area Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PListArea'] = []
        pcClickLocs[scriptRunner]['PListArea'].append(lastClick[0])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PListArea'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['PListArea'])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['PListArea'][0][0],pcClickLocs[scriptRunner]['PListArea'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['PListArea'][1][0],pcClickLocs[scriptRunner]['PListArea'][1][1])
        time.sleep(0.25)
        selection = pg.confirm(text='is the area selected?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please select first and last char in the first row\'s Dept', title='Department Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PListDept'] = []
        pcClickLocs[scriptRunner]['PListDept'].append(lastClick[0])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PListDept'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['PListDept'])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['PListDept'][0][0],pcClickLocs[scriptRunner]['PListDept'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['PListDept'][1][0],pcClickLocs[scriptRunner]['PListDept'][1][1])
        time.sleep(0.25)
        selection = pg.confirm(text='is the Dept selected?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please select first and last char in the first row\'s PO', title='PO Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PLPo'] = []
        pcClickLocs[scriptRunner]['PLPo'].append(lastClick[0])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PLPo'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['PLPo'])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['PLPo'][0][0],pcClickLocs[scriptRunner]['PLPo'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['PLPo'][1][0],pcClickLocs[scriptRunner]['PLPo'][1][1])
        time.sleep(0.25)
        selection = pg.confirm(text='is the PO selected?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please select first and last char in the first row\'s Vendor Name', title='Vendor Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['POVendor'] = []
        pcClickLocs[scriptRunner]['POVendor'].append(lastClick[0])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['POVendor'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['POVendor'])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['POVendor'][0][0],pcClickLocs[scriptRunner]['POVendor'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['POVendor'][1][0],pcClickLocs[scriptRunner]['POVendor'][1][1])
        time.sleep(0.25)
        selection = pg.confirm(text='is the Vendor selected?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    #"PListPlts","PListStatus" ,"PListLURHdr"
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please select first and last char in the first row\'s # of Pallets', title='Pallets Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PListPlts'] = []
        pcClickLocs[scriptRunner]['PListPlts'].append(lastClick[0])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PListPlts'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['PListPlts'])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['PListPlts'][0][0],pcClickLocs[scriptRunner]['PListPlts'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['PListPlts'][1][0],pcClickLocs[scriptRunner]['PListPlts'][1][1])
        selection = pg.confirm(text='is the # Plts selected?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please click on first and last char in the first row\'s Status', title='Status Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PListStatus'] = []
        pcClickLocs[scriptRunner]['PListStatus'].append(lastClick[0])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PListStatus'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['PListStatus'])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['PListStatus'][0][0],pcClickLocs[scriptRunner]['PListStatus'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['PListStatus'][1][0],pcClickLocs[scriptRunner]['PListStatus'][1][1])
        selection = pg.confirm(text='is the Status selected?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please click on first and last char in the first row\'s LUR Hdr', title='LUR Hdr Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PListLURHdr'] = []
        pcClickLocs[scriptRunner]['PListLURHdr'].append(lastClick[0])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PListLURHdr'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['PListLURHdr'])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['PListLURHdr'][0][0],pcClickLocs[scriptRunner]['PListLURHdr'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['PListLURHdr'][1][0],pcClickLocs[scriptRunner]['PListLURHdr'][1][1])
        selection = pg.confirm(text='is the LUR Hdr selected?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please click on the action input on the first row keytrol', title='P-List action input', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['PListActionInput'] = lastClick[0]
        pg.click(pcClickLocs[scriptRunner]['PListActionInput'][0],pcClickLocs[scriptRunner]['PListActionInput'][1])
        time.sleep(0.25)
        selection = pg.confirm(text='Is the action input for the P-List selected?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    pg.click(pcClickLocs[scriptRunner]['PListActionInput'][0],pcClickLocs[scriptRunner]['PListActionInput'][1])
    pg.typewrite(["3"])
    pg.press(["enter"])
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please click on the first and last characters of the first keytrol in the Keytrol Inquiry by PO list', title='Keytrol by PO', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['POInqKeytrol'] = []
        pcClickLocs[scriptRunner]['POInqKeytrol'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['POInqKeytrol'])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['POInqKeytrol'].append(lastClick[0])
        time.sleep(0.25)
        selection = pg.confirm(text='Is the Keytrol Selected?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please click on the action input on the first row keytrol', title='PO keytrol action input', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['POActionInput'] = lastClick[0]
        pg.click(pcClickLocs[scriptRunner]['POActionInput'][0],pcClickLocs[scriptRunner]['POActionInput'][1])
        time.sleep(0.25)
        selection = pg.confirm(text='Is the action input for the PO Keytrol selected?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please click Below the n in "PO Inq" at the bottom of the screen, then the end of the line', title='PO keytrol action input', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['KeytrolByPOError'] = []
        pcClickLocs[scriptRunner]['KeytrolByPOError'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['KeytrolByPOError'])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['KeytrolByPOError'].append(lastClick[0])
        time.sleep(0.25)
        selection = pg.confirm(text='Is the space under "q" to the end of the line selected?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    pg.click(pcClickLocs[scriptRunner]['POActionInput'][0],pcClickLocs[scriptRunner]['POActionInput'][1])
    pg.typewrite(["5"])
    pg.press(["enter"])
    goodFlag = False
    while not goodFlag:
        pg.alert(text='After making sure that no error message appeared at the bottom of the screen, Please click on the first and last spaces for the Total Qty value for all headers on the first page', title='Units per header', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['HeaderUnits'] = []
        pcClickLocs[scriptRunner]['HeaderUnits'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['HeaderUnits'])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['HeaderUnits'].append(lastClick[0])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['HeaderUnits'][0][0],pcClickLocs[scriptRunner]['HeaderUnits'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['HeaderUnits'][1][0],pcClickLocs[scriptRunner]['HeaderUnits'][1][1])
        selection = pg.confirm(text='Is the header units selected?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    goodFlag = False
    while not goodFlag:
        pg.alert(text='After making sure that no error message appeared at the bottom of the screen, Please click on the first and last characters in "Bottom" (In the bottom right)', title='Units per header', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['BottomText'] = []
        pcClickLocs[scriptRunner]['BottomText'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['BottomText'])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['BottomText'].append(lastClick[0])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['BottomText'][0][0],pcClickLocs[scriptRunner]['BottomText'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['BottomText'][1][0],pcClickLocs[scriptRunner]['BottomText'][1][1])
        selection = pg.confirm(text='Is the text "Bottom" selected?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    pg.press("f12")
    pg.press("f12")
    goodFlag = False
    while not goodFlag:
        pg.alert(text='Please Click on the top left and bottom right corner of all the rows (from under the Action input to the last rows LUR Hdr)', title='Screen Position', button='OK')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['FullPLScreen'] = []
        pcClickLocs[scriptRunner]['FullPLScreen'].append(lastClick[0])
        print(pcClickLocs[scriptRunner]['FullPLScreen'])
        time.sleep(0.25)
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        pcClickLocs[scriptRunner]['FullPLScreen'].append(lastClick[0])
        time.sleep(0.25)
        pg.moveTo(pcClickLocs[scriptRunner]['FullPLScreen'][0][0],pcClickLocs[scriptRunner]['FullPLScreen'][0][1])
        pg.dragTo(pcClickLocs[scriptRunner]['FullPLScreen'][1][0],pcClickLocs[scriptRunner]['FullPLScreen'][1][1])
        selection = pg.confirm(text='Are all rows selected?', title='Input Confirmation', buttons=['Yes', 'No'])
        if selection == "Yes":  
            goodFlag = True
    pg.hotkey("f12")
    pg.hotkey("f12")
    pg.hotkey("f12")
    with open("ScanClickLocations.json","w") as f:
        json.dump(pcClickLocs,f)
else:
    print("Setup Cancelled")