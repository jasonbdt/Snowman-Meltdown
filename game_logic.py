import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(
    mistakes: int,
    secret_word: str,
    guessed_letters: list[str]
) -> None:
    print(STAGES[mistakes])

    if mistakes < 3:
        masked_word = ""
        for letter in secret_word:
            masked_word += letter if letter in guessed_letters else "_"

        print(f"Word: {" ".join(masked_word)}\n")


def play_game():
    mistakes = 0
    guessed_letters = []
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # TODO: Build your game loop here.
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        if mistakes == 3:
            print(f"Game Over! The word was {secret_word}")
            break
        elif len(set(guessed_letters)) == len(set(secret_word)):
            print(f"Congratulations, you saved the snowman!")
            break
        else:
            guess = input("Guess a letter: ").lower()

            if guess in secret_word.lower():
                guessed_letters.append(guess)
            else:
                mistakes += 1

        print("You guessed:", guess)