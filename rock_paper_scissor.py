import random
from typing import Dict, List

# --------------------------------
# Game Variants Configuration
# --------------------------------
# Dictionary storing all game variants with their specific rules and choices.
# Each variant contains:
# - name: Display name of the variant
# - choices: List of valid moves
# - rules: Dictionary defining which moves beat other moves
GAME_VARIANTS = {
    "1": {
        "name": "Classic Game",
        "choices": ["rock", "paper", "scissors"],
        "rules": {"rock": ["scissors"], "paper": ["rock"], "scissors": ["paper"]},
    },
    "2": {
        "name": "Big Bang Theory",
        "choices": ["rock", "paper", "scissors", "lizard", "spock"],
        "rules": {
            "rock": ["scissors", "lizard"],
            "paper": ["rock", "spock"],
            "scissors": ["paper", "lizard"],
            "lizard": ["paper", "spock"],
            "spock": ["rock", "scissors"],
        },
    },
    "3": {
        "name": "European",
        "choices": ["rock", "paper", "scissors", "well"],
        "rules": {
            "rock": ["scissors"],
            "paper": ["rock", "well"],
            "scissors": ["paper"],
            "well": ["rock", "scissors"],
        },
    },
    "4": {
        "name": "Shield Hero",
        "choices": ["rock", "paper", "scissors", "dynamite", "shield"],
        "rules": {
            "rock": ["scissors", "dynamite"],
            "paper": ["rock", "shield"],
            "scissors": ["paper", "shield"],
            "dynamite": ["rock", "scissors"],
            "shield": ["dynamite", "rock"],
        },
    },
    "5": {
        "name": "Lightning",
        "choices": ["rock", "paper", "scissors", "tree", "lightning"],
        "rules": {
            "rock": ["scissors", "lightning"],
            "paper": ["rock", "tree"],
            "scissors": ["paper", "tree"],
            "tree": ["lightning", "rock"],
            "lightning": ["paper", "tree"],
        },
    },
}


# --------------------------------
# Game Functions
# --------------------------------

def print_tutorial(variant: Dict) -> None:
    """Print the tutorial for a specific game variant."""
    print(f"\nTutorial for {variant['name']}:")
    print(f"Available choices: {', '.join(variant['choices'])}")
    print("\nRules:")
    for choice, beats in variant["rules"].items():
        for beaten in beats:
            print(f"-> {choice} beats {beaten}")


def get_user_choice(choices: List[str]) -> str:
    """
    Gets and validates the user's move choice.
    
    Args:
        choices (List[str]): List of valid moves the user can choose from
        
    Returns:
        str: The user's validated choice from the available moves
        
    Note:
        - Displays numbered options for user selection
        - Validates input is a valid number within range
        - Keeps asking until valid input is received
    """
    while True:
        print("\nChoose your move:")
        for i, choice in enumerate(choices, 1):
            print(f"{i}: {choice}")

        user_input = input("\nEnter your choice (number): ")
        if user_input.isdigit() and 1 <= int(user_input) <= len(choices):
            return choices[int(user_input) - 1]
        print("Invalid choice! Please enter a valid number.")


def determine_winner(player_choice: str, computer_choice: str, rules: Dict) -> str:
    """
    Determines the winner of the game based on the choices and game rules.
    
    Args:
        player_choice (str): The move chosen by the player
        computer_choice (str): The move chosen by the computer
        rules (Dict): Dictionary containing the game rules defining which moves beat others
        
    Returns:
        str: A message indicating the result (win/lose/tie) in both Spanish and English
        
    Logic:
        - If both choices are the same -> Tie
        - If computer's choice is in the list of moves that player's choice beats -> Player wins
        - Otherwise -> Computer wins
    """
    if player_choice == computer_choice:
        return "¡Empate! / It's a tie!"
    elif computer_choice in rules[player_choice]:
        return "¡Ganaste! / You won! 🎉"
    else:
        return "¡Perdiste! / You lost! 😢"


def main():
    """
    Main game function that controls the game flow.
    
    Flow:
        1. Displays welcome message in Spanish and English
        2. Shows available game variants
        3. Gets user's choice of game variant
        4. Offers optional tutorial
        5. Starts main game loop:
           - Gets player's move
           - Generates computer's move
           - Determines winner
           - Asks to play again
        6. Shows goodbye message when player finishes
        
    Note:
        - The game is bilingual (Spanish/English)
        - Each variant has its own set of rules and moves
        - The computer's choice is randomly selected
    """
    print(
        "¡Bienvenido al juego de Piedra, Papel o Tijera! / Welcome to Rock, Paper, Scissors Game!"
    )
    print("\nAvailable versions:")
    for key, variant in GAME_VARIANTS.items():
        print(f"{key}: {variant['name']}")

    # Get game version
    while True:
        game_version = input("\nChoose a version (1-5): ")
        if game_version in GAME_VARIANTS:
            break
        print("Invalid version! Please choose a number between 1 and 5.")

    variant = GAME_VARIANTS[game_version]

    # Show tutorial if requested
    tutorial = input("\nDo you want to see the tutorial? (yes/no): ").lower()
    if tutorial.startswith("y"):
        print_tutorial(variant)

    # Main game loop
    while True:
        # Get choices
        player_choice = get_user_choice(variant["choices"])
        computer_choice = random.choice(variant["choices"])

        # Show choices
        print(f"\nYour choice: {player_choice}")
        print(f"Computer's choice: {computer_choice}")

        # Determine and show winner
        result = determine_winner(player_choice, computer_choice, variant["rules"])
        print(f"\n{result}")

        # Play again?
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if not play_again.startswith("y"):
            break

    print("\n¡Gracias por jugar! / Thanks for playing!")


if __name__ == "__main__":
    main()
