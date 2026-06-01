#Which tear do you want to check?
leap = int(input())
#Don't chang the code above

#Write your code below this line

if leap % 4 == 0:
    if leap % 100 == 0:
        if leap % 400 == 0:
            print(f"The year {leap} is a leap year")
        else:
            print(f"The year {leap} is not a leap year")
    else:
        print(f"The year {leap} is a leap year")
else:
    print(f"The year {leap} is not a leap year")