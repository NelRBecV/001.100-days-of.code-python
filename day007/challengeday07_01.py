# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]
# TODO-1: Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []


# For testing code purposes
print(f'Pssst, the solution is {chosen_word}.')


for _ in range(word_length):
    display.append("_")

# TODO-2: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# TODO-3: Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for position in range(word_length):
    letter = chosen_word[position]

    if letter == guess:
        print("YOU RIGHT!!!")
