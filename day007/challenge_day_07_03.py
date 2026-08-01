import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# For testing code purposes
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

# TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all
#  the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
endgame = False

while not endgame:
    guess = input("Guess a letter: ").lower()
    
    for position in range(word_length):        
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        endgame = True
        print("YOU GUESSED THE WORD")
