import random

random_pc_choice = random.randint(1, 3)

print("Welcome to Rock, Paper, Scissor Game!")

print(
    "Which version or variant you want to play: \n1: Classic Game.\n2: Big Bang Theory."
    "\n3: European.\n4: Shield Hero.\n5: Lightning."
)

game_version = input("Choose one of the numbers: ")

print("Do you want to see how to play the game version? ")
tutorial_version = input("Yes or No: ").lower()

if game_version == "1" and tutorial_version == "yes":
    print("You have choose: Classic Game")
    print(
        "The Tutorial of this games is:\n There are only 3 elements:\n- Rock, Scissor and Paper\nBasic rules:\n-> Rock breaks Scissors.\n-> Scissors cut Paper\n-> Paper covers Rock"
    )
