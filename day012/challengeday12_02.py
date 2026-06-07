import random
from clear import clear

def logo():
    print('''
            _  _   _  _   _   _  ___   ___   ____     ____   _  _   ___    ___    ___    ___   _  _   ____  
            ) \/ ( ) () ( ) \_/ (\  _) ) __( /  _ \   ).-._( ) () ( ) __(  (  _(  (  _(  )_ _( ) \/ ( ).-._( 
            |  \ | | \/ | |  _  ||  (  | _)  )  ' /   |( ,-. | \/ | | _)   _) \   _) \   _| |_ |  \ | |( ,-. 
            )_()_( )____( )_( )_(/__o) )___( |_()_\   )_`__( )____( )___( )____) )____) )_____()_()_( )_`__( 
    ''')

clear()
logo()

def guessing_level(level):
    random_number = random.randint(1, 100)
    if level[0] == "e":
        attempt_left = 10
    else:
        attempt_left = 5

    return random_number, attempt_left


def finding_number(mistery_number, attempt):
    my_number = int(input("Make a guess: "))
    win = 0
    if mistery_number == my_number:
        print("Congratulations!!! You did it")
        win = 1
    else:
        if mistery_number > my_number:
            print("Too low")
            attempt -= 1
        else:
            print("Too high")
            attempt -= 1
        if attempt > 0:
            print("Try again.")
            print(f"You have {attempt} lives remaining")

    return attempt, win


print("Welcome to the Number Guessing Game!!!")
print("I'm thinking of a number between 1 and 100.")
game_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
this_match = guessing_level(game_level)
number_to_guess = this_match[0]
guess_left = this_match[1]
print(f"You have {guess_left} attempts to guess the number")

while guess_left != 0:
        result = finding_number(number_to_guess, guess_left)
        guess_left = result[0]
        if guess_left == 0 and result[1] == 0:
            print("No lifes left. Game Over!!!")
        elif guess_left != 0 and result[1] != 0:
            guess_left = 0
