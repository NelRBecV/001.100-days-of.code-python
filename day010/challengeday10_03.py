from clear import clear
def logo():
    logo=['''Again, here goes the logo, 
        but, I don't have internet right now''']

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

opertations={'+': add,
             '-': subtract,
             '*': multiply,
             '/': divide}
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    done_again ="y"
  
    while done_again == "y":
        for op in opertations:
            print(op)
          
        math_op = input("Which math opretation do yo want to do?:\n")
        num2 = float(input(("What's the next number?: ")))
        calculation_function = opertations[math_op]
        resul= calculation_function(num1,num2)      
        print(f"{num1} {math_op} {num2} = {resul}")
        done_again=input(f"Type 'y' if you'd like to calculate with {resul}, or type 'n' if you want to calculate another number\n").lower()
      
        if done_again=="y":
            clear()
            num1=resul
        else:
            clear()
            calculator()

calculator()
