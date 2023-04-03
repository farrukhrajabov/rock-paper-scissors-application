import random

# Create options
while True:
    options = ["rock", "paper", "scissors"]
    
    # Players
    computer = random.choice(options)
    player = None

    while player not in options:
        player = input("Rock, paper or scissors?) \n ").lower()

    if player == computer:
        print(f"Computer: {computer} ") 
        print(f"Player: {player} ")
        print("\nYou have tied!")

    elif player == "rock":
        if computer == "paper":
            print(f"\nComputer: {computer} ") 
            print(f"Player: {player} ")
            print("\nYou lose!")
        if computer == "scissors":
            print(f"Computer: {computer} ") 
            print(f"Player: {player} ")
            print("\nYou win!") 

    elif player == "paper":
        if computer == "rock":
            print(f"\nComputer: {computer} ") 
            print(f"Player: {player} ")
            print("\nYou win!") 
        if  computer == "scissors":
            print(f"\nComputer: {computer} ") 
            print(f"Player: {player} ")  
            print("\nYou lose!")

    elif player == "scissors":
        if computer == "rock":
            print(f"\nComputer: {computer} ") 
            print(f"Player: {player} ")
            print("\nYou lose!")
        if computer == "paper":
            print(f"\nComputer: {computer} ") 
            print(f"Player: {player} ") 
            print("\nYou won!")

   

    game_restart = input("\nDo you want to play again? yes/no\n ").lower()
    if game_restart != "yes":
        break
    else:
        print(game_restart)

print("\nThanks for playing!")

        




                                 

