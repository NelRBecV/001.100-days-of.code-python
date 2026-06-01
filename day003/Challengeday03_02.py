#Enter your height in meters e.g., 1.55
height = float(input())
#Enter your weight in kilograms e,g,. 72
weight = int(input())
#Don't change the code above

#Write your code below this line
bmi = weight / height ** 2

if bmi <= 18.5:
    print(f"Your BMI is {round(bmi,1)}, you are underweight")
elif bmi <= 25:
    print(f"Your BMI is {round(bmi,1)}, You are normal")
elif bmi <= 30:
    print(f"Your BMI is {round(bmi,1)}, you are slightly overweight")
else:
    print(f"You BMI is {round(bmi,1)}. you are clinically obese")
