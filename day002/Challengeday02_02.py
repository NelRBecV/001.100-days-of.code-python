# print(3 * 3 + 3 / 3 - 3)
#print(3 * 3 / 3 + 3 - 3) #Mi método
#print(3 * (3 + 3) / 3 - 3)#El método de ella

#1st input: enter the heights in meters e.g. 1.65
height = float(input())

#2nd input: enter the weight in kilograms e.g. 72
weight = int(input())
#Don't change the code above

#Write the code below this line
bmi = weight / (height**2)

print("Your Body Muscular Index is " + str(bmi))

