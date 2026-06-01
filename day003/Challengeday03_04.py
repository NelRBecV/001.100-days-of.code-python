print("Thank you fod choosing Python Pizza Delivers!")
size_pizza = input("What size of pizza do you want? S, M, L: ")
add_peperoni = input("Do you want peperoni in your pizza? Y, N: ")
extra_cheese = input("Do you want extra cheese in your pizza? Y, N: ")
#Don't change the code above

#Write your code below this line
if size_pizza == "S":
    price = 15
    if add_peperoni == "Y":
        price += 2
elif size_pizza == "M":
    price = 20
    if add_peperoni == "Y":
        price += 3
else:
    price = 25
    if add_peperoni == "Y":
        price += 3
if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: ${price}")