import random
from clear import clear


def logo():
    print('''
    _  _   _  _   _   _  ___   ___   ____     ____   _  _   ___    ___    ___    ___   _  _   ____  
    ) \/ ( ) () ( ) \_/ (\  _) ) __( /  _ \   ).-._( ) () ( ) __(  (  _(  (  _(  )_ _( ) \/ ( ).-._( 
    |  \ | | \/ | |  _  ||  (  | _)  )  ' /   |( ,-. | \/ | | _)   _) \   _) \   _| |_ |  \ | |( ,-. 
    )_()_( )____( )_( )_(/__o) )___( |_()_\   )_`__( )____( )___( )____) )____) )_____()_()_( )_`__( 
    ''')


def guessing_level(level):
    attempt_left = 5
    random_number = random.randint(1, 100)
    if level.lower() == "easy":
        attempt_left = 10

    return random_number, attempt_left


def finding_number(mistery_number):
    my_number = int(input("Make a guess: "))
    if mistery_number == my_number:
        print("Congratulations!!! You did it")
        return 1

    if mistery_number > my_number:
        print("Too low")
    else:
        print("Too high")
    return 0


clear()
logo()
print("Welcome to the Number Guessing Game!!!")
number_to_guess, lives_left = guessing_level(input("Choose a difficulty. Type 'easy' or 'hard': ").lower())
print("I'm thinking of a number between 1 and 100.")
while lives_left != 0:
    print(f"You have {lives_left} attempts to guess the number")
    result = finding_number(number_to_guess)
    if result == 0:
        lives_left -= 1
    else:
        break

    if lives_left == 0:
        print("No lives left. Game Over!!!")
