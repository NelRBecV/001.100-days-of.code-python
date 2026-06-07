#DEBUGGING EXCERCISE
#Which year do you want to check?

year = input()
#Problem detectec: Non valid data input type. An integer data is required for processing data
#                  but the variable value gotten from it was string

year = int(input()) #Casting input to integer solves the type incompatibility problem

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leap year")
        else:
            print("This is not a leap year")
    else:
        print("This is a leap year")
else:
    print("This is aa leap year")
