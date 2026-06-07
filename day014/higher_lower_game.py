#              Higher or lower Project
from hl_logo import main_logo
from clear import clear
from hl_data import data_choices
from hl_classical import play_classical_mode

high_score = 0

main_logo()

print("Do You wanna prove yourself testing your knowledge about the world of celebrities?")
print("If your answer is 'YES', then let's give a try to the most famous game ever")

while input("Do you want to start a new game?: ").lower()[0] == "y":
    end_game = False
    clear()
    print("The rules are simple. You must guess who has more fans between two celebrities")
    print("Pick 'h' (high) to point out if someone has more fans than another")
    print("or pick 'l' (low) to point out who has less")
    print("The game will continue till you choose a wrong answer")
    
    option1 = data_choices()    
    winning_points = 0    
    option2 = data_choices()
        
    while not end_game:        
        clear()        
        right_answer = play_classical_mode(option1, option2)
        
        if right_answer:
            option1 = option2
            winning_points += 1
            option2 = data_choices()
            print(option2)
        else:
            end_game = True    

    print(f"Your score is {winning_points}\n")
    
    if winning_points > high_score:
        high_score = winning_points
        
    print(f"Maximum score so far is {high_score}")
