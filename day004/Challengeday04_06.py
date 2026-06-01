import random
#it's assumed the user inputs an integer number, otherwise the program will raise an error
print("What do you choose? Type '0' for Rock, '1' Paper and '2' for Scissors")
human_choice = int(input())
computer_choice = random.randint(0, 2)
print(str(human_choice))
print(str(computer_choice))
if human_choice == 0 and computer_choice == 2:
    print('''
    _______                  _______
---'   ____)            ____(____   '---
      (_____)          (______
      (_____)         (__________
      (____)               (____)
---.__(___)                (___)__.---
You picked ROCK      Computer picked SCISSORS
              
               YOU WON!!!
''')
elif human_choice == 1 and computer_choice == 2:
    print('''
     _______                      _______
---'    ____)____             ___(____   '---
           ______)           (________
          _______)          (__________
         _______)                (____)
---.__________)                    (___)__.---
                
 You Picked PAPER            Computer picked SCISSORS                
        
                Computer WON!!!
    ''')
elif human_choice == 2 and computer_choice == 2:
    print('''
    _______                      _______
---'   ____)____            ____(____   '---
          ______)          (______
       __________)        (__________
      (____)                    (____)
---.__(___)                      (___)__.---
    
You picked Scissor      Computer picked Scissor

                It's a DRAW!!!
    ''')
elif human_choice == 0 and computer_choice == 1:
    print('''
    _______                 _______
---'   ____)           ____(____   '----
      (_____)         (______
      (_____)         (_______
      (____)          (_______
---.__(___)                (_________.---

   You Picked ROCK        Computer picked PAPER
   
                Computer WON!!!
    ''')
elif human_choice == 0 and computer_choice == 0:
    print('''
    _______           _______
---'   ____)         (____   '---
      (_____)       (_____)
      (_____)       (_____)
      (____)         (____)
---.__(___)           (___)__.---

You picked ROCK    Computer picked ROCK

            It's a DRAW
    ''')
elif human_choice == 2 and  computer_choice ==1:
    print('''
   _______                        _______
---'  ____)_____             ____(____   '----
          _______)          (______
       __________)         (_______
       (____)               (_______
---.__(___)                  (_________.---
                Paper VS Paper
 You Picked SCISSORS            Computer picked PAPER                
        
                    You WON!!!
    ''')
elif human_choice == 1 and computer_choice == 1:
    print('''
    
     _______                     _______
---'    ____)____           ____(____   '----
           ______)         (______
          _______)         (_______
         _______)           (_______
---.__________)                (_________.---

   You Picked PAPER        Computer picked PAPER
   
                It's a DRAW

    ''')
elif human_choice == 1 and computer_choice == 0:
    print('''
         _______                 _______
---'    ________)               (____)   '---
           ______)             (_____)
          _______)             (______)
         _______)               (_____)
---.__________)                  (_____.---

   You Picked PAPER          Computer picked ROCK
   
                    You WON!!!
    ''')
elif human_choice == 2 and computer_choice == 0:
    print('''
   _______                      _______
---'  ____)____                (______   '---
          ______)            (________
         _______)           (_________
       (____)                (_________
---.__(___)                   (___________.---

  You Picked SCISSORS          Computer picked ROCK

                    Compuer WON!!!
    ''')
else:
    print("You should pick up an option among '0', '1' and 2")
