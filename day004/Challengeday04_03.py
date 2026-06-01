names_string= input()

names= names_string.split(", ")#Transform a chain of Strings into a list taking in count the separator between brackets
#The code above converts the input into an array separating
#each name in the input by a comma and space.

#Don't change the code above
import random
people= len(names)-1

ramdon_people = random.randint(0, people)

print(f"{names[ramdon_people]} is going to buy the meal today!")