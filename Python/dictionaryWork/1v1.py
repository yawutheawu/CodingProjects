import random
import gameFuncs as g

'''
Weapons:
    Fists
        DMG: 1
        DUR: 99999999999999999999999999999999999999999999999999999999999999999999999999999
    Rusty Sword
        DMG: 5
        DUR: 3
        
    Gold Sword
        DMG: 10
        DUR: 5
    
    Excalibur
        DMG: 100
        DUR: 1
    
    Mace
        DMG: 7
        DUR: 7
    
    Crossbow
        DMG: 8
        DUR: 5
        
Consumables
    Health Potion
        HEAL: 5
        STR: 0
    
    Bread
        HEAL: 2
        STR: 0
        
    Potassium
        HEAL: 0
        STR: 2
'''
WeaponStats = {
    "Fists" : {
        "DMG" : 1,
        "DUR" : 999999999999999999999999999999999999999999999999999999999999999999
    },
    "Rusty Sword" : {
        "DMG" : 5,
        "DUR" : 3
    },
    "Gold Sword" : {
        "DMG" : 10,
        "DUR" : 5
    },
    "Excalibur" : {
        "DMG" : 100,
        "DUR" : 1
    },
    "Mace" : {
        "DMG" : 7,
        "DUR" : 7
    },
    "Crossbow" : {
        "DMG" : 8,
        "DUR" : 5
    }
}

ConsumeStats = {
    "Health Potion" : {
        "HEAL" : 5,
        "STR" : 0
    },
    "Bread" : {
        "HEAL" : 2,
        "STR" : 0
    },
    "Potassium" : {
        "HEAL" : 0,
        "STR" : 2
    }
}

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
            for i in Player["INV"].keys():
                if i in ConsumeStats.keys():
                    charConsume.append(str(i))
g.printDuel(Player,Enemy)