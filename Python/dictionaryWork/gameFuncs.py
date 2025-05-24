import random

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


def floatRand(lowBound,Highbound):
    return lowBound + (random.random() * (Highbound-lowBound))

def printChar(charDict : dict) -> None:
    #{'HEALTH': 36, 'STR': 34, 'INV': {'Bread': {'Quantity': 5}, 'Excalibur': {'Quantity': 1, 'UsedTimes': 0}, 'Potassium': {'Quantity': 6}}}
    '''
    Health: CurrHealth
    STR: CurrStr
         O
        /|\
        / \
    Weapon: WeapName Uses/Dur
    Consumables:
        Conume1 : Quant
    '''
    print(f"Health: {charDict['HEALTH']}")
    print(f"Strength: {charDict['STR']}")
    print("     OↃ")
    print("    /|\\\\")
    print("    / \\\\")
    
    charINV = charDict["INV"]
    
    charWeapon = ""
    for i in charINV.keys():
        if i in WeaponStats.keys():
            charWeapon = str(i)
            
    charConsume = []
    for i in charINV.keys():
        if i in ConsumeStats.keys():
            charConsume.append([str(i),charINV[i]["Quantity"]])
            
    print(f"Weapon: {charWeapon} | {WeaponStats[charWeapon]['DUR'] - charINV[charWeapon]['UsedTimes']} uses remain")
    
    print("Consumables: ")
    for i in charConsume:
        print(f"\t{i[0]} | {i[1]}")

def printDuel(charDict : dict, enemyDict:dict) -> None:
    #{'HEALTH': 36, 'STR': 34, 'INV': {'Bread': {'Quantity': 5}, 'Excalibur': {'Quantity': 1, 'UsedTimes': 0}, 'Potassium': {'Quantity': 6}}}
    '''
    Health: CurrHealth
    STR: CurrStr
         O
        /|\
        / \
    Weapon: WeapName Uses/Dur
    Consumables:
        Conume1 : Quant
    '''
    
    charINV = charDict["INV"]
    enemyINV = enemyDict["INV"]
    
    charWeapon = ""
    for i in charINV.keys():
        if i in WeaponStats.keys():
            charWeapon = str(i)
            
    charConsume = []
    for i in charINV.keys():
        if i in ConsumeStats.keys():
            charConsume.append([str(i),charINV[i]["Quantity"]])
    
    enemyWeapon = ""
    for i in enemyINV.keys():
        if i in WeaponStats.keys():
            enemyWeapon = str(i)
            
    enemyConsume = []
    for i in enemyINV.keys():
        if i in ConsumeStats.keys():
            enemyConsume.append([str(i),enemyINV[i]["Quantity"]])
    
    consume = []
    for i in charConsume:
        consume.append([i,0])
    for k,i in enumerate(enemyConsume):
        try:
            consume[k][1] = i
        except:
            consume.append([None,i])
    
    print(f"Health: {charDict['HEALTH']}                                       Health: {enemyDict['HEALTH']}")
    print(f"Strength: {charDict['STR']}                                     Strength: {enemyDict['STR']}")
    print(f"     OↃ                                              0Ↄ")
    print(f"    /|\\\\                                            /|\\\\")
    print(f"    / \\\\                                            / \\\\")
            
    print(f"Weapon: {charWeapon} | {WeaponStats[charWeapon]['DUR'] - charINV[charWeapon]['UsedTimes']} uses remain\t\tWeapon: {enemyWeapon} | {WeaponStats[enemyWeapon]['DUR'] - enemyINV[enemyWeapon]['UsedTimes']} uses remain")
    print("Consumables:                                    Consumables:")
    for i in consume:
        print(f"\t{i[0][0]} | {i[0][1]}                               \t{i[1][0]} | {i[1][1]}")

def actionSelect() -> int:
    print("Pick an option: ")
    print(" ⌜‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾⌝⌜‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾⌝")
    print(" |                     ||                      |")
    print(" |       Attack        ||       Consume        |")
    print(" |                     ||                      |")
    print(" ⌞_____________________⌟⌞_____________________⌟")
    correct = True
    while correct:
        userIn = input("type in number: ")
        try:
            userIn = int(userIn)
            if userIn == 1:
                correct = False
                return 1
            if userIn ==2:
                correct = False
                return 2
            else:
                correct = True
                print("enter 1 or 2")
        except:
            print("Enter 1 or 2")
    return userIn