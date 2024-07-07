# Hangman
import random
import time
wordbank = (
    'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino factory protein bench squat salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra Ability Backing Cabinet Absence Balance Calibre Academy Banking Calling Account Barrier Capable Accused Battery Capital Achieve Bearing Captain Acquire Beating Caption Address Because Capture Advance Bedroom Careful Adverse Believe Carrier Advised Beneath Caution Adviser Benefit Ceiling Against Besides Central Airline Between Centric Airport Billion Century Alcohol Binding Certain Alleged Brother Chamber Already Brought Channel Analyst Burning Chapter Ancient Dealing Charity Another Decided Charlie Anxiety Decline Charter Anxious Default Checked Anybody Defence Chicken Applied Deficit Chronic Arrange Deliver Circuit Arrival Density Classes Article Deposit Classic Assault Desktop Climate Assumed Despite Closing Assured Destroy Closure Attempt Develop Clothes Attract Devoted Collect Auction Diamond College Average Digital Combine Eastern Discuss Comfort Economy Disease Command Edition Display Comment Elderly Dispute Compact Element Distant Company Engaged Diverse Compare Enhance Divided Compete Essence Drawing Complex Evening Driving Concept Evident Dynamic Concern Exactly Factory Concert Examine Faculty Conduct Example Failing Confirm Excited Failure Connect Exclude Fashion Consent Exhibit Feature Consist Expense Federal Contact Explain Feeling Contain Explore Fiction Content Express Fifteen Contest Extreme Filling Context Gallery Finance Control Gateway Finding Convert General Fishing Correct Genetic Fitness Council Genuine Foreign Counsel Gigabit Forever Counter Greater Formula Country Hanging Fortune Crucial Heading Forward Crystal Healthy Founder Culture Hearing Freedom Current Heavily Further Cutting Helpful Illegal Jointly Helping Illness Journal Herself Imagine Journey Highway Imaging Justice Himself Improve Justify History Include Keeping Holding Initial Killing Holiday Inquiry Kingdom Housing Insight Kitchen However Install Knowing Hundred Instant Machine Husband Instead Manager Landing Intense Married Largely Interim Massive Lasting Involve Maximum Leading Natural Meaning Learned Neither Measure Leisure Nervous Medical Liberal Network Meeting Liberty Neutral Mention Library Notable Message License Nothing Million Limited Nowhere Mineral Listing Nuclear Minimal Logical Nursing Minimum Loyalty Pacific Missing Obvious Package Mission Offence Painted Mistake Officer Parking Mixture Ongoing Partial Monitor Opening Partner Monthly Operate Passage Morning Opinion Passing Musical Optical Passion Mystery Organic Passive Portion Outcome Patient Poverty Outdoor Pattern Precise Outlook Payable Predict Outside Payment Premier Overall Penalty Premium Proudly Pending Prepare Project Pension Present Promise Pealing Prevent Promote Perfect Primary Protect Perform Printer Protein Perhaps Privacy Protest Phoenix Private Provide Picking Problem Publish Picture Proceed Purpose Pioneer Process Pushing Plastic Produce Qualify Pointed Product Quality Popular Profile Quarter Section Success Radical Segment Suggest Railway Serious Summary Readily Service Support Reading Serving Suppose Reality Session Supreme Realise Setting Surface Receipt Seventh Surgery Receive Several Surplus Recover Shortly Survive Reflect Showing Suspect Regular Silence Sustain Related Silicon Teacher Release Similar Telecom Remains Sitting Telling Removal Sixteen Tension Removed Skilled Theatre Replace Smoking Therapy Request Society Thereby Require Somehow Thought Reserve Someone Through Resolve Speaker Tonight Respect Special Totally Respond Species Touched Restore Sponsor Towards Retired Station Traffic Revenue Storage Trouble Reverse Strange Turning Rollout Stretch Typical Routine Student Uniform Running Studied Unknown Satisfy Subject Unusual Science Succeed Upgrade Walking Whether Upscale Wanting Willing Utility Warning Winning Variety Warrant Without Various Wearing Witness Vehicle Weather Working Venture Webcast Writing Version Website Written Veteran Wedding Western Victory Weekend Whereas Viewing Welcome Whereby Village Welfare Virtual Violent Visible Waiting Sigma'
).lower().split(" ")

HANGMANPICS = [
    '''
  +---+
  |   |
	  |
	  |
	  |
	  |
=========''', '''
  +---+
  |   |
  O   |
	  |
	  |
	  |
=========''', '''
  +---+
  |   |
  O   |
  |   |
	  |
	  |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
	  |
	  |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
	  |
	  |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
	  |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
	  |
========='''
]
hiddenWord = random.choice(wordbank)
guess = 0
correctGuesses = []
incorrectGuesses = []
Win = False
while (len(incorrectGuesses) < 7 and not Win):
    print(HANGMANPICS[len(incorrectGuesses)])
    for i in range(0, len(hiddenWord)):
        if hiddenWord[i] in correctGuesses:
            print(hiddenWord[i], end=' ')
        else:
            print('_', end=' ')
    print("\n")
    print("Letters guessed: " + str(incorrectGuesses))
    print(str(correctGuesses))
    #print(hiddenWord)
    userInput = input("Guess a letter or the word: ").lower()
    if (len(userInput) == 1):
        if userInput in hiddenWord:
            if userInput in correctGuesses:
                print("You already guessed this letter.")
            else:
                correctGuesses.append(userInput)
        else:
            if userInput in incorrectGuesses:
                print("You already guessed this letter.")
            else:
                incorrectGuesses.append(userInput)
        guess += 1
    else:
        pass
        if userInput == hiddenWord:
            Win = True
        else:
            guess += 1
            print("Thats not the right word!")
    tempHide = hiddenWord
    tempCorrect = [x for x in correctGuesses]
    for i in range(0, len(tempCorrect)):
        tempHide = tempHide.replace(tempCorrect[0], "")
        tempCorrect.pop(0)
    if tempHide == "":
        Win = True

# game over
if len(incorrectGuesses) >= 7:
    print(HANGMANPICS[6])
    print("You lost! The word was: " + hiddenWord)
    time.sleep(3)
if Win:
    print("You Won!")
    time.sleep(3)
