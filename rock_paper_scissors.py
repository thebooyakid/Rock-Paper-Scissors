import random

def rock_paper_scissors():
    wins = 0
    losses = 0
    choices = ['rock', 'paper', 'scissors']
    while True:
        player_choice = input("\nChoose one: 'rock' 'paper' 'scissors' or 'quit' to quit: ")
        if player_choice.lower() == "quit":
            if wins > losses:
                print(f"\nYou won {wins} times, and lost {losses} times. That's a winning record! ")
            elif losses > wins:
                print(f"\nYou won {wins} times, and lost {losses} times. Today's not your day. ")
            else:
                print(f"\nYou won {wins} times, and lost {losses} times. Not bad.")
            print("Later dude\n")
            return
        while player_choice.lower() not in choices:
            player_choice = input("Invalid choice, please choose again ")
            
        print(f"\nYou have chosen {player_choice}.")
        challenger_choice = random.choice(choices)
        print(f"Your opponent has chosen {challenger_choice}")
        if player_choice.lower() == challenger_choice:
            print("It's a tie")
        elif player_choice.lower() == 'rock':
            if challenger_choice == 'paper':
                print("You lose, kid.")
                losses += 1
            else:
                print("Winner Winner")
                wins += 1
        elif player_choice.lower() == 'paper':
            if challenger_choice == 'rock':
                print("Victory is yours")
                wins += 1
            else:
                print("You just got beat")
                losses +=1
        elif player_choice.lower() == 'scissors':  
            if challenger_choice == 'rock':
                print("I am sorry to inform you that you have lost, sir or madame")
                losses += 1
            else:
                print("This is a triumph for humanity")
                wins += 1

rock_paper_scissors()