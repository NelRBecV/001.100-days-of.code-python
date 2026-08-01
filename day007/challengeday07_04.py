# Step 4
import random
from utilities import stages_logo


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
hangman_stages = stages_logo.stages()

# TODO-1: Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 7

# For testing code purposes
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

endgame = False

while not endgame:
    guess = input("Guess a letter: ").lower()
    guessed = False
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
            guessed = True

    print(" ".join(display))

    # TODO-2: If guess is not a letter in the chosen_word, then reduce 'lives' by 1.
    if not guessed:
        lives -= 1
        # TODO-3: print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has
        #  remaining.
        print(hangman_stages[lives])

    if "_" not in display:
        endgame = True
        print("YOU GUESSED THE WORD")

    # If 'lives' goes down to 0 then the game should stop, and it should print  "You Lose."
    if lives == 0:
        endgame = True
        print("You Lose.")
