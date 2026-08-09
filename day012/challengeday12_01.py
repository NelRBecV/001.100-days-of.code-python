# Introducing Local and Global Scopes and Namespaces

# Example of a global Scope
Money = 100  # This variable can be used all over the code


# Example of a local variable
def supplement():
    Money = 200


supplement()
print(f"money with extra payment {Money}")
# It prints the value of global money, not the supplement module


# Modifying a Global Variable
def feeding_tickets():
    global Money
    Money += (Money * 1) 
                       
# global keyword brings us values from inner scopes without returning anything, but it must be used carefully
# due to the high risk of getting bugs by changing the value of the variable itself


feeding_tickets()
print(Money)
