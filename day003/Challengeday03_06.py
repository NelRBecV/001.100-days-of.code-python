print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to the Treasure Island")
print("Your mission is to find a hidden treasure somewhere in this island")

first_choice= input("There's a crossroad ahead from you. What path do you take? Left or Right\n")
if first_choice.lower() == "right":
    print("You've found a Cannibal village and then they eat you. Game over")
elif first_choice.lower() == "left":
    print("You walk through the dense jungle until dicovering a overflowed river in fron of you.")
    second_choice= input("What do you wanna do? Wait or Swing\n")
    if second_choice.lower() == "swing":
        print("You drag downriver while trying to swing and finally drowed down. Game over")
    elif second_choice.lower() == "wait":
        print("the torrent of water starts slowing down afer several minutes")
        print("You reached a place where there are three wooden doors. A yellow one, Blue one and Red one")
        third_choice = input("Which one do you wanna open?\n")
        if third_choice.lower() == "yellow":
            print("Congratulations!!! You found the trasure")
        elif third_choice.lower() == "Blue":
            print("You fell into a well and die. Game over")
        elif third_choice.lower() == "Red":
            print("A Rain of arrows are thown over your head. Game over")
        else:
            print("So, you think you're very funny, Uhh. Take this... A celestial blast felt down instantanly killing you")
            print("GAME OVER. PRICK!!!")
    else:
        print("So, you think you're very funny, Uhh. Take this... A celestial blast felt down instantanly killing you")
        print("GAME OVER. PRICK!!!")
else:
    print("So, you think you're very funny, Uhh. Take this... A celestial blast felt down instantanly killing you")
    print("GAME OVER. PRICK!!!")