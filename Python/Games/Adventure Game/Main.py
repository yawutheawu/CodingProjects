def askQuestion(prompt:str, question:str, choices:list) -> int:
    x = ""
    while not x in range(1,len(choices)+1):
        print(prompt)
        for Val,Key in enumerate(choices):
            print(f"\t{Val+1}. {Key}")
        x = input(question)
        try:
            x = int(x)
        except:
            print("Yorue so stupid type number")
            x = ''
    return x-1

def victory():
    print("YOU WIN YIPPIIEEE")
    return 1

def loss():
    print("its over")
    return 0

prompt = "Pick a Card: "
question = "Choose a number: "
answerList = ["7 of Hearts", 
              "4 of Clubs", 
              "Ace of Spades",
              "King of Hearts"
              ]
output = askQuestion(prompt, question, answerList)

if output == 0:
    print("You picked the 7 of Hearts")
    print("Shadows figures force you to take a shot of a clear liquor")
    print("\tYour judgment is affected!")
    prompt = "Which Casino Attraction will you visit?: "
    question = "Choose a number: "
    answerList = ["Play Blackjack", 
                "Play a hand of Texas Poker", 
                "Bet on Roulette",
                "Try to leave the casino"
                ]
    output = askQuestion(prompt, question, answerList)
    if output == 0:
        print("You see Jack Black playing Black Jack and die from shock")
        loss()
    elif output == 1:
        print("People smile eerily at you")
        pass
    elif output == 2:
        print("You bet on green until you have no green")
        loss()
    else:
        print("A big fish, presumably the bouncer, stops you violently")
        loss()
elif output == 1:
    pass
elif output == 2:
    pass
else:
    pass