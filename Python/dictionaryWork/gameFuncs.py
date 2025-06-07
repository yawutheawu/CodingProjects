import random
import constants

WeaponStats = constants.WeaponStats

ConsumeStats = constants.ConsumeStats



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
    if len(charConsume) > len(enemyConsume):
        for i in charConsume:
            if i != None:
                consume.append([i,0])
        for k,i in enumerate(enemyConsume):
            try:
                consume[k][1] = i
            except:
                consume.append([None,i])
    else:
        for i in enemyConsume:
            if i != None:
                consume.append([["\t", ""],i])
        for k,i in enumerate(charConsume):
            try:
                consume[k][0] = i
            except:
                consume.append([i,None])
    
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