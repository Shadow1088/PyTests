import random
print(f"Lets play a game called Rock, paper, scissors")

p_choices = ["Rock","Paper","Scissors","R","P","S"]
pc_choices = ["Rock","Paper","Scissors"]



list1 = []

running = True

while running:

    player = None

    while player not in p_choices:
        player = input("Your choice?: ")

    computer = random.choice(pc_choices)
    if player:
        if player == "R":
            player == "Rock"
        elif player == "P":
            player == "Paper"
        elif player == "S":
            player == "Scissors"

    print (f"Player chose: {player}")
    print (f"Computer chose: {computer}")


    if computer == player:
        print("!! Its a tie! !!")

    elif computer == "Rock" and player == "Paper":
        print("!! You win! !!")

    elif computer == "Scissors" and player == "Rock":
        print("!! You win! !!")

    elif computer == "Paper" and player == "Scissors":
        print("!! You win! !!")

    else:
        print("!! You lose !!")
