import random

random_pc_choice = random.randint(1, 3)

print("Welcome to Rock, Paper, Scissor Game!")

print(
    "Which version or variant you want to play: \n1: Classic Game."
    "\n2: Big Bang Theory."
    "\n3: European.\n4: Shield Hero.\n5: Lightning."
)

game_version = input("Choose one of the numbers: ")

print("Do you want to see how to play the game version? ")
tutorial_version = input("Yes or No: ").lower()

while True:
    if game_version == "1" and tutorial_version == "yes":
        print("you have choose: classic game")
        print(
            "the tutorial of this games is:\n there are only 3 elements:"
            "\n- rock, scissor and paper\nbasic rules:\n-> rock breaks scissors."
            "\n-> scissors cut paper\n-> paper covers rock"
        )
    elif game_version == "2" and tutorial_version == "yes":
        print("you have choose: Big Bang Theory variant")
        print(
            "the tutorial of this games is:\nthere are 5 elements:"
            "\n- rock, scissor, paper, lizard and spock\nbasic rules:"
            "\n-> rock crushes scissors.\n-> scissors cuts paper."
            "\n-> paper covers rock.\n-> rock crushes lizard."
            "\n-> lizard poisons spock.\n-> spock smashes scissors.\n"
        )
    elif game_version == "3" and tutorial_version == "yes":
        print("you have choose: European variant")
        print(
            "the tutorial of this games is:\n there are 4 elements:"
            "\n- rock, scissor, paper and well\nbasic rules:"
            "\n-> rock breaks scissors.\n-> scissors cut paper"
            "\n-> paper covers rocks and well\n well drowns rocks and scissors"
        )
    elif game_version == "4" and tutorial_version == "yes":
        print("You have choose: ShieldHero version")
        print(
            "the tutorial for this game is:\nthere are 5 elements:"
            "\n- rock, scissor, paper, dynamite, shield.\nbasic rules:"
            "\n-> rock crushes scissors and block dynamite.\n-> scissors cuts paper and pierce shield."
            "\n-> paper covers rock and jams shield.\n-> dynamite blows up rock and scissors."
            "\n-> shield block dynamite and deflects rock."
        )
    elif game_version == "5" and tutorial_version == "yes":
        print("You have choose: Lightning version")
        print(
            "the tutorial for this game is:\nthere are 5 elements:"
            "\n- rock, scissor, paper, tree, lightning.\nbasic rules:"
            "\n-> rock crushes scissors and shelters lightning.\n-> scissors cuts paper and prune tree."
            "\n-> paper covers rock and documents tree.\n-> tree absorbs lightning and outgrows rock."
            "\n-> lightning burns paper and splits tree."
        )
