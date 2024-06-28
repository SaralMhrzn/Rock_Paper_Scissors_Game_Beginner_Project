import random

game = ['rock', "paper", "scissors"]
while True:
    player1= input(f'Player_1 chose any from this {game}: ').lower()
    if player1 not in game:
        print(f"Invalid input. Please enter {game}")
        continue #Goes back to while loop if condition meets
    player2 = random.choice(game)
    print(f"player2 chose: {player2}")

    if (player1 == "rock") and (player2 == "paper") or \
       (player1 == "paper" and player2 == "scissors") or \
        (player1 == "scissor" and player2 == "rock"):
        print("player2 won the game")
    elif player1 == player2:
        print("It's a draw! Play next match")
    else:
        print("player1 won the game")

    while True:
        next_match = input("Do you want to play next game?(Yes/No): ").strip().lower()
        if next_match== "yes":
            print("playing next match")
            break
        elif next_match == "no": 
            break  #Exit the inner loop and tala baki vayeko code ma janxa
        else:
            print("Please, enter valid answer")
    if next_match == "no":
        break
print("Thanks for playing game!")