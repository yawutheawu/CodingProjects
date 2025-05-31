import random
import time
import constants
import gameFuncs as g

WeaponStats = constants.WeaponStats

ConsumeStats = constants.ConsumeStats

'''
Entity
    HEALTH
    STR
    INV = {}
'''

Player = {
    "HEALTH" : 15,
    "STR" : 5,
    "INV" : {
    }
}

intFlag = True
while intFlag:
    inputHealth = input("How many health points will your character have? ")
    try:
        inputHealth = int(inputHealth)
        if inputHealth < 1:
            inputHealth = 1
        intFlag = False
    except:
        print("Please enter whole numbers only")
Player["HEALTH"] = inputHealth

intFlag = True
while intFlag:
    inputSTR = input("How many strength points will your character have? ")
    try:
        inputSTR = int(inputSTR)
        if inputSTR < 1:
            inputSTR = 1
        intFlag = False
    except:
        print("Please enter whole numbers only")
Player["STR"] = inputSTR

intFlag = True
while intFlag:
    for i in range(len(WeaponStats.keys())):
        print(f"{i+1} : {list(WeaponStats.keys())[i]}")
    inputWeapon = input("Which weapon will your character have? ")
    try:
        inputWeapon = int(inputWeapon)
        if inputWeapon > 0 and inputWeapon <= len(WeaponStats.keys()):
            inputWeapon = inputWeapon-1
            intFlag = False
        else:
            raise Exception("Put in the Right Numba")
    except:
        print("Please enter whole numbers shown in the list above only")
Player["INV"][list(WeaponStats.keys())[inputWeapon]] = {"Quantity": 1, "UsedTimes":0}

intFlag = True
while intFlag:
    for i in range(len(ConsumeStats.keys())):
        print(f"{i+1} : {list(ConsumeStats.keys())[i]}")
    inputConsume = input("Which consumable will your character have? ")
    try:
        inputConsume = int(inputConsume)
        if inputConsume > 0 and inputConsume <= len(ConsumeStats.keys()):
            inputConsume -= 1
            intFlag = False
        else:
            raise Exception("Put in the Right Numba")
    except:
        print("Please enter whole numbers shown in the list above only")
Player["INV"][list(ConsumeStats.keys())[inputConsume]] = {"Quantity": max(round(random.gauss(5,3)),1)}

Enemy = {
    "HEALTH" : random.randrange(
        round(Player["HEALTH"]-(Player["HEALTH"]*0.5)),
        round(Player["HEALTH"]+(Player["HEALTH"]*0.3))
        ),
    "STR" : random.randrange(
        round(Player["STR"]-(Player["STR"]*0.5)),
        round(Player["STR"]+(Player["STR"]*0.3))
        ),
    "INV" : {
        random.choice(list(WeaponStats.keys())) : {"Quantity": 1, "UsedTimes":0},
        random.choice(list(ConsumeStats.keys())) : {"Quantity":max(round(random.gauss(5,3)),1)}
    }
}
while Player["HEALTH"] > 0 and Enemy["HEALTH"]>0:
    g.printDuel(Player,Enemy)
    turnUsed = False
    while not turnUsed:
        PlayerAction = g.actionSelect()
        if PlayerAction == 1:
            charWeapon = ""
            for i in Player["INV"].keys():
                if i in WeaponStats.keys():
                    charWeapon = str(i)
            if Player["INV"][charWeapon]["UsedTimes"] < WeaponStats[charWeapon]["DUR"]:
                Enemy["HEALTH"] -= WeaponStats[charWeapon]["DMG"] * Player["STR"]
                Player["INV"][charWeapon]["UsedTimes"] += 1
                if Player["INV"][charWeapon]["UsedTimes"] >= WeaponStats[charWeapon]["DUR"]:
                    del Player["INV"][charWeapon]
                    Player["INV"]["Fists"] = {"Quantity" : 1, "UsedTimes" : 0}
            turnUsed = True
        else:
            charConsume = []
            for i in Player["INV"].items():
                if i[0] in list(ConsumeStats.keys()):
                    charConsume.append(i)
            ConsumeInputFlag = True
            while ConsumeInputFlag:
                print("What would you like to consume?")
                for i in range(len(charConsume)):
                    print(f"{i+1}. {charConsume[i][0]} | Left: {charConsume[i][1]['Quantity']}")
                print(f"{len(charConsume)+1}. Return")
                selection = input("Pick a number from the list: ")
                try:
                    selection = int(selection)-1
                    if selection == len(charConsume):
                        print("Returning")
                        ConsumeInputFlag = False
                    elif selection >= 0 and selection <= len(charConsume):
                        itemSelection = charConsume[selection][0]
                        Player["INV"][itemSelection]["Quantity"] -= 1
                        Player["HEALTH"] += ConsumeStats[itemSelection]["HEAL"]
                        Player["STR"] += ConsumeStats[itemSelection]["STR"]
                        if Player["INV"][itemSelection]["Quantity"] <= 0:
                            del Player["INV"][itemSelection]
                        turnUsed = True
                        ConsumeInputFlag = False
                    else:
                        print("Bad Input")
                        ConsumeInputFlag = True
                except Exception as e:
                    print(e)
                    print("Try Again")
                    ConsumeInputFlag = True
    while turnUsed:
        print("Enemy Turn")
        time.sleep(1)
        turnUsed = False
        '''
        Agression Meter, chance of attack vs consumeables depending on consumables
            potentially based off of STR
        If low health, focus on healing
        if high health and not agressive, focus on using potassium
        avoid using healing items too early
        '''
g.printDuel(Player,Enemy)