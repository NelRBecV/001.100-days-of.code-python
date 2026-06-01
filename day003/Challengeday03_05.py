print("The Love Calcualtor is calculatin your score...")
name1=input()#"What is your name?"
name2=input()#"What's her name?"
#Don't change the code above
#Write your code below this line
counting_T=0
counting_R=0
counting_U=0
counting_E=0
counting_L=0
counting_O=0
counting_V=0
counting_e=0
i=0

total_char_name = len(name1) + len(name2)
both_names = name1 + name2
for i in range(total_char_name):
    if both_names[i] == "T" or both_names[i] =="t":
        counting_T += 1
        i+= 1
    elif both_names[i] == "R" or both_names[i] == "r":
        counting_R += 1
        i += 1
    elif both_names[i] == "U" or both_names[i] == "u":
        counting_U += 1
        i += 1
    elif both_names[i] == "E" or both_names[i] == "e":
        counting_E += 1
        i += 1

print(f"T occurs {counting_T} times.\n")
print(f"R occurs {counting_R} times.\n")
print(f"U occurs {counting_U} times.\n")
print(f"E occurs {counting_E} times.\n")
total_true= counting_T + counting_R + counting_U + counting_E
print("Total: " + str(total_true))
i=0
for i in range(total_char_name):
    if both_names[i] == "L" or both_names[i] == "l":
        counting_L += 1
        i += 1
    elif both_names[i] == "O" or both_names[i] == "o":
        counting_O += 1
        i += 1
    elif both_names[i] == "V" or both_names[i] == "v":
        counting_V += 1
        i += 1
    elif both_names[i] == "E" or both_names[i] == "e":
        counting_e += 1
        i+= 1

print(f"L occurs {counting_L} times.\n")
print(f"O occurs {counting_O} times.\n")
print(f"V occurs {counting_V} times.\n")
print(f"E occurs {counting_e} times.\n")
total_love = counting_L + counting_O + counting_V + counting_e
print("Total: " + str(total_love))
total = int(str(total_true) + str(total_love))
if total <= 10 or total >=90:
    print(f"Yor score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")

