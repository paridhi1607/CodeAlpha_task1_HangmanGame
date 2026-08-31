import random
from words import WORDS


MAX_WRONG_GUESSES = 6


def display_word(word, guessed_letters):
    """Display guessed letters and hide the remaining letters."""
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    return display.strip()


def play_game():
    """Run one complete Hangman game."""

    word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0

    print("\n" + "=" * 40)
    print("        WELCOME TO HANGMAN")
    print("=" * 40)
    print(f"You have {MAX_WRONG_GUESSES} incorrect guesses.")
    print("Guess the word one letter at a time!\n")

    while wrong_guesses < MAX_WRONG_GUESSES:

        print("Word:", display_word(word, guessed_letters))
        print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}")

        # Check if the player has guessed the complete word
        if all(letter in guessed_letters for letter in word):
            print("\n Congratulations! You guessed the word!")
            print(f"The word was: {word}")
            return

        guess = input("\nEnter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print(" Please enter only one letter.")
            continue

        # Check repeated guess
        if guess in guessed_letters:
            print(" You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check whether the letter is in the word
        if guess in word:
            print(" Correct guess!")
        else:
            wrong_guesses += 1
            print(" Wrong guess!")

    print("\n GAME OVER!")
    print(f"The correct word was: {word}")


def main():
    """Start the game and allow the player to replay."""

    while True:
        play_game()

        again = input("\nDo you want to play again? (yes/no): ").lower().strip()

        if again not in ["yes", "y"]:
            print("\nThanks for playing Hangman! ")
            break


if __name__ == "__main__":
    main()