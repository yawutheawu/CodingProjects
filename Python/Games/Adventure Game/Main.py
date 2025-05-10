def askQuestion(prompt:str, question:str, choices:list) -> int:
    x = ""
    while not x in range(1,len(choices)+1):
        print(prompt)
        for Key,Val in enumerate(choices):
            print(f"\t{Key+1}. {Val}")
        x = input(question)
        try:
            x = int(x)
        except:
            print("Yorue so stupid type number")
            x = ''
    return x-1

def victory():
    print("We are so back")
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
        prompt = "Will you eat a burger or drink apple juice?: "
        question = "Choose a number: "
        answerList = ["Eat a Burger", 
                    "Drink Apple Juice"
                    ]
        output = askQuestion(prompt, question, answerList)
        if output == 0:
            prompt = "What kind of burger do you desire?: "
            question = "Choose a number: "
            answerList = ["CheeseBurger",
                            "Double Whopper", 
                            "Whopper"
                            ]
            output = askQuestion(prompt, question, answerList)
            if output == 0:
                print("A golden ticket to willy wonka's factory gets stuck between your teeth")
                victory()
            elif output == 1:
                prompt = "What filling do you desire?: "
                question = "Choose a number: "
                answerList = ["Tuna",
                            "Metal Pipes"
                            ]
                output = askQuestion(prompt, question, answerList)
                if output == 0:
                    print("The big fish bouncer takes offense to your frankly awful taste in burgers")
                    loss()
                else:
                    print("The lead in the pipes gets to you")
                    loss() 
            else:
                prompt = "How much money do you wish to gamble for your whopper to win?: "
                question = "Choose a number: "
                answerList = ["all in",
                              "None",
                              "50%",
                              "60%",
                              "-30%"
                            ]
                output = askQuestion(prompt, question, answerList)
                if output == 0:
                    print("You win big")
                    victory()
                elif output == 1:
                    print("It was all a dream (You get nothing)")
                    loss()
                elif output == 2:
                    print("Your whopper disintegrates")
                    loss()
                elif output == 3:
                    print("Your whopper leaves you and bets his own money")
                    loss()
                else:
                    print("Your whopper can believe you have so little self-esteem and breaks up with you")
                    loss()
        else:
            print("A person asks if you are drinking beer")
            print("You decide to like and say yes")
            print('They try your "beer"')
            print("You die of humiliation")
            loss()
    elif output == 2:
        print("You bet on green until you have no green")
        loss()
    else:
        print("A big fish, presumably the bouncer, stops you violently")
        loss()
elif output == 1:
    prompt = "Filler"
    question = "Choose a number: "
    answerList = ["Option 1",
                  "Option 2"
                ]
    output = askQuestion(prompt, question, answerList)
    if output == 0:
        prompt = "Filler"
        question = "Choose a number: "
        answerList = ["Option 1",
                    "Option 2"
                    ]
        output = askQuestion(prompt, question, answerList)
        if output == 0:
            print("Death Message")
            loss()
        else:
            print("Win Message")
            victory()
    else:
        print("Death Message")
        loss()
elif output == 2:
    prompt = "Filler"
    question = "Choose a number: "
    answerList = ["Option 1",
                    "Option 2",
                    "option 3"
                    ]
    output = askQuestion(prompt, question, answerList)
    if output == 0:
        print("Death Message")
        loss()
    elif output == 1:
        prompt = "Filler"
        question = "Choose a number: "
        answerList = ["Option 1",
                        "Option 2"
                        ]
        output = askQuestion(prompt, question, answerList)
        if output == 0:
            print("Death Message")
            loss()
        else:
            print("Death Message")
            loss()
    else:
        prompt = "Filler"
        question = "Choose a number: "
        answerList = ["Option 1",
                        "Option 2"
                        ]
        output = askQuestion(prompt, question, answerList)
        if output == 1:
            print("win message")
            victory()
else:
    prompt = "Filler"
    question = "Choose a number: "
    answerList = ["Option 1",
                        "Option 2",
                        "Option 3"
                        ]
    output = askQuestion(prompt, question, answerList)
    if output == 0:
        prompt = "Filler"
        question = "Choose a number: "
        answerList = ["Option 1",
                            "Option 2",
                            "Option 3"
                            ]
        output = askQuestion(prompt, question, answerList)
        if output == 0:
            print("Loss message")
            loss()
        else:
            print("win message")
            victory()
    elif output == 1:
        prompt = "Filler"
        question = "Choose a number: "
        answerList = ["Option 1",
                            "Option 2",
                            "Option 3"
                            ]
        output = askQuestion(prompt, question, answerList)
        if output == 0:
            print("loss message")
            loss()
        elif output == 1:
            print("loss message")
            loss()
        else:
            print("Loss Message")
            loss()
    else:
        print("loss message")
        loss()