import random, os, time, sys
import pyttsx3

def computer():
    return (random.randint(1,1000000000))%3 + 1

def play(playerChoice):
    global playerScore, computerScore, totalPlays
    computerChoice = computer()
    engine.say(f"Opponet choosed {choice[computerChoice]}")
    if (playerChoice==1 and computerChoice==3) or (playerChoice==2 and computerChoice==1) or (playerChoice==3 and computerChoice==2):
        print("Win") 
        playerScore+=1
    elif playerChoice==computerChoice:
        print("Tie")
        playerScore+=1
        computerScore+=1
    else:
        print("Lost")
        computerScore+=1
    engine.runAndWait()
    totalPlays+=1
    return

engine = pyttsx3.init()
choice = {1: "rock",2: "paper",3: "scissors"}
playerScore = 0
computerScore = 0
totalPlays = 0

print("WelCome to Rock-Paper-Scissor Game")
name=input("Name: ")
playerChoice = 1
input("Enter 1/2/3 and press enter\nEnter 0 to end the game.\nDon't press 'Enter' without any values\nPress any key to continue...")

while(playerChoice):
    os.system("cls")
    playerChoice = input("1.Rock\n2.Paper\n3.Scissors\nEnter: ")
    print(len(playerChoice))
    if len(playerChoice) == 1 :
        try:
            playerChoice=int(playerChoice)
            if playerChoice not in [0,1,2,3]:
                raise ValueError
            if playerChoice==0:
                break
            play(playerChoice)
        except ValueError:
            print("Invalid Input ---> Enter [0, 1, 2, 3] only")
            time.sleep(1)


if playerScore > computerScore:
    print(f"You won the match by {playerScore - computerScore} points")
    engine.say(f"Hello {name}, you won the match by {playerScore - computerScore} points. In {totalPlays} rounds.")
elif playerScore > computerScore:
    print(f"You lost the match by {computerScore - playerScore} points")
    engine.say(f"Hello {name}, you lost the match by {computerScore - playerScore} points. In {totalPlays} rounds.")
else:
    print(f"Tie with score {computerScore}")
    engine.say(f"Hello {name}, it is a tie match with score {computerScore}. In {totalPlays} rounds.")

engine.say(f"Visit and Play again {name}")
engine.runAndWait()