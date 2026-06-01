#Write your code below this line
#Hint: Don't forget make the call to the module random
import random

coin_toss = random.randint(0,1)

if coin_toss == 0:
    print("Tails")
else:
    print("Head")