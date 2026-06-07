#DEBUGGING EXCERCISE
target = int(input())

for number in range(1, target+1):
    #The logical connector is "AND", not "OR"
    if number % 3 == 0 or number % 5 == 0:
        print("FizzBuzz")

    if number % 3 == 0: #This is an elif, not if
        print("Fizz")

    if number % 5 == 0: #This is an elif, not if
        print("Buzz")

    else:
        #There are additional bracket wrapping the variable
        print((number))
      
