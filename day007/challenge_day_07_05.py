# Step 5
import random
from utilities.stages_logo import stages, logo
from utilities.list_words import list_words

# TODO-1: Update the word list to use the 'word_list' from hangman_words.py
#  Delete this line: word_list = ['ardvark', 'baboon', 'camel']

word_list = list_words()
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
hangman_stages = stages()
letters_entered = []
lives = 7

# TODO-3: Import the logo from hangman_art.py and print it at the start of the game
print(logo())

# For testing code purposes
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

endgame = False

while not endgame:
    print(" ".join(display))
    guess = input("Guess a letter: ").lower()
    guessed = False
    # TODO-4: If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in letters_entered:
        print(f'You have already said "{guess}" before.')
        continue
    letters_entered.append(guess)

    for position in range(word_length):

        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            guessed = True

    if not guessed:
        lives -= 1
        # TODO-5: If the letter id not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f'WRONG!!! The letter "{guess}" is not in the word. You got {lives} lives left')
        # TODO-2: Import the stages from hangman_art.py and make this error go away
        #  (The error that suppose to appear in here, it was solved in the previous challenge)
        print(hangman_stages[lives])

    if "_" not in display:
        endgame = True
        print("YOU GUESSED THE WORD")

    if lives == 0:
        endgame = True
        print("You Lose.")
