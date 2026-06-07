#Step 2
import os
import random
import list_words
import stages_logo
print(stages_logo.logo())
word_list = list_words.list_words()
stages = stages_logo.stages()

#TODO-1 create an empty list called "display" For each
#       letter in "chosen_word", ass an "_" into "display"
#
#       So, if the chosen_word is "apple", display should be
#       # ['_','_','_','_','_'] representing each letter to guess
#TODO-2 Ask the user to guess a letter and assing their variable called
#
#
#
# TODO-3 Check if the letter of the user guessed (guess) is one of the letters
# #         of the chosen word.
chances = 7
chosen_word = word_list[random.randint(0,len(word_list))]#random.choice(word_list)
print(chosen_word)
display = []

for i in range(len(chosen_word)):
    display.append("_")



answer = 0
you_won=0
you_lost=0
while chances > 0 and you_won == 0:
    os.system('cls')#Clean the screen
    guess=input("Choose a letter:\n") #guess=input("Choose a letter:").lower()
    count_letter = 0; rep = 0
    for i in range(0, len(chosen_word)):
        if guess.lower() == chosen_word[i]:
            if  display[i] == chosen_word[i]:
                rep=1
            else:
                count_letter += 1
                display[i] = guess
                rep =0
    print(display)
    if count_letter > 0 and not rep:
        print("RIGHT!!!")
        answer +=count_letter
    elif count_letter == 0 and not  rep:
        print(f"WRONG! The letter {guess} is not in the word")
        chances -= 1
    else:
        print("You already said that letter")
    if answer == len(chosen_word):
        you_won = 1
        print("That's the correct word.")
        print("Congrats!! You WON!!!")
    elif chances == 0:
        you_lost = 1
        print(f"The correct word was {chosen_word.capitalize()}")
        print("Sorry, no lifes left. Game Over")
    if chances != 7:
        print(stages[chances])
