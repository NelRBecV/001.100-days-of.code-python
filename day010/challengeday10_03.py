from clear import clear


def logo():
    app_logo = ["""
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

    """]


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {'+': add,
              '-': subtract,
              '*': multiply,
              '/': divide}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    done_again = "y"
  
    while done_again == "y":
        for op in operations:
            print(op)
          
        math_op = input("Which math operation do yo want to do?:\n")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[math_op]
        resul = calculation_function(num1, num2)
        print(f"{num1} {math_op} {num2} = {resul}")
        done_again = input(f"Type 'y' if you'd like to calculate with {resul}, or type 'n' if you want to calculate"
                           f" another number\n").lower()
      
        if done_again == "y":
            clear()
            num1 = resul
        else:
            clear()
            calculator()


calculator()
