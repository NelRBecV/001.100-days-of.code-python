#Step 1
import random
word_list = ["ardvark", "baboon", "camel"]

#TODO-1 Randomly choose a word from "word_list" and assign it
#        to a variable called chosen_word

# TODO-2 Ask the user to guess a letter and assing their variable called
#        guess. Make gues lowcase

# TODO-3 Check if the letter of the user guessed (guess) is one of the letters
#         of the chosen word.
life_left = 10
chosen_word = word_list[random.randint(0,2)] #random.choice(word_list)
chosen_word_letters = list(chosen_word)
word_guessed = 0
you_win=0
you_lost=0
while life_left > 0 or you_win != len(chosen_word):
    guess=input("Choose a letter:\n") #guess=input("Choose a letter:").lower()
    for i in range(0, len(chosen_word)):
        if guess == chosen_word_letters[i] :
            print("RIGHT!!")
            word_guessed +=1
            chosen_word_letters[i] = ""
        else:
            print("WRONG")
            life_left -=1

# if word_guessed == len(chosen_word):
#     print("That's the correct word.")
#     print("Congrats!! You WON!!!")
# else:
#     print("Sorry!!! The correct word was ")
#     print("No lifes left. Game Over")
#

