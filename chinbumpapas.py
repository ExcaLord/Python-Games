import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input(
        "Please choose one: Paper, Rock, Scissor. or type Q to quit the game"
    ).lower()

    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissor"]:
        continue

    random_number = random.randint(0, 2)
    # rock = 0, paper = 1, scissor = 2.
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissor":
        print(f"You won! computer choose: {computer_pick}")
        user_wins += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print(f"You won! computer choose: {computer_pick}")
        user_wins += 1
        
    elif user_input == "scissor" and computer_pick == "paper":
        print(f"You won! computer choose: {computer_pick}")
        user_wins += 1
    else:
        print("You Lose!")
        computer_wins += 1
        
    if user_wins == 3:
        print("You ave won the match")
        print(f"Your wins = {user_wins}\n Computer wins = {computer_wins}")
        break
    else:
        print("You have lose the match")
        print(f"Computer wins = {computer_wins}\n Your wins = {user_wins}")

print("Good bye!")