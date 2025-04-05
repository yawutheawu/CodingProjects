def askQuestion(prompt:str, question:str, choices:list) -> int:
    print(prompt)
    x = ""
    while not x in range(1,len(choices)+1):
        print("Do you take:")
        for Val,Key in enumerate(choices):
            print(f"\t{Val+1}. {Key}")
        x = input(question)
        try:
            x = int(x)
        except:
            print("Yorue so stupid type number")
            x = ''
    return x-1

question1Choices = ["Cheese","String","Dirt","Rock","Torch"]
output = askQuestion("You are in dark forest pick item: ", "Choose item number: ", question1Choices)
print(f"You picked {question1Choices[output]}")

question2Choices = ["More Cheese","Loam"]
output = askQuestion("You pick another item: ", "Choose item number: ", question2Choices)
print(f"You picked {question2Choices[output]}")