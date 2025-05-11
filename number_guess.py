import random
# Juego de adivinar el numero que piensa la computadora.

max_number = input(
    "Type the max of the numbers that the machine will use for the guess game"
)

if max_number.isdigit():
    max_number = int(max_number)

    if max_number <= 0:
        print("Please digit a number higher than 0 next time: ")
        quit()
else:
    print("Please digit a number next time")
    quit()


random_number = random.randint(0, max_number)
guess_attempts = 0

while True:
    guess_attempts += 1
    user_input = input("Digit the number that the machine is thinking! ")

    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print("Please type a number, the last one you digit is not a number")
        continue

    if user_input == random_number:
        print("You have guessed the number")
        print(f"Took to you {guess_attempts} attempts to guess the number")
        break
    elif user_input < random_number:
        print("You are lower than the number")
    else:
        print("You are upper than the number")

print("The game have end!")
