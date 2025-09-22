import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word() -> str:
    """
    Return a random secret word from the built-in list.

    Selects one entry from ``WORDS`` uniformly at random.

    Returns:
        str: The chosen secret word (lowercase).
    """
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(
    mistakes: int,
    secret_word: str,
    guessed_letters: list[str]
) -> None:
    """
    Render the current game state.

    Prints the ASCII-art snowman stage for the given number of ``mistakes``
    and displays the masked secret word where unguessed letters are shown
    as underscores.

    Args:
        mistakes (int): Number of incorrect guesses (0–3).
        secret_word (str): The word to guess.
        guessed_letters (list[str]): Letters the player has already guessed.

    Returns:
        None
    """
    print(STAGES[mistakes])

    if mistakes < 3:
        masked_word = ""
        for letter in secret_word:
            masked_word += letter if letter in guessed_letters else "_"

        print(f"Word: {" ".join(masked_word)}\n")


def get_player_guess() -> str:
    """
    Prompt the player for a single letter and validate it.

    Reads input from ``stdin`` and ensures exactly one alphabetical character
    was entered. Raises ``ValueError`` if the input is empty, contains more
    than one character, or includes non-alphabetic symbols.

    Returns:
        str: The raw character the user entered.

    Raises:
        ValueError: If the input is invalid.
    """
    player_guess = input("Guess a letter: ")
    if len(player_guess) > 1:
        raise ValueError(
            "Invalid input: Only single alphabetical "
            "characters are allowed!"
        )
    elif player_guess == "":
        raise ValueError(
            "Invalid input: Guessing without characters is not allowed!"
        )
    elif not player_guess.isalpha():
        raise ValueError(
            "Invalid input: Guess should not contain any digits!"
        )


    return player_guess


def play_game():
    """
    Run the Snowman Meltdown game loop.

    Initializes game state, repeatedly displays the current state, and
    processes player guesses until the player either guesses all letters
    or reaches the maximum number of mistakes (3). Prints a win or loss
    message at the end.

    Returns:
        None
    """
    mistakes = 0
    guessed_letters = []
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        if mistakes == 3:
            print(f"Game Over! The word was {secret_word}")
            break
        elif len(set(guessed_letters)) == len(set(secret_word)):
            print(f"Congratulations, you saved the snowman!")
            break
        else:
            try:
                player_guess = get_player_guess()
            except ValueError as exc:
                print(exc)
            else:
                if player_guess in secret_word.lower():
                    guessed_letters.append(player_guess)
                else:
                    mistakes += 1

                print("You guessed:", player_guess)
