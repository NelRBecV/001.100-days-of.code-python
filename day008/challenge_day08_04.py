# Write your code below this line
def prime_checker(number):
    prime=0
    for i in range(2,number+1):
        if  number % i == 0:
            prime += 1

    if prime == 1 and number != 1:
        print(f"The number {number} is a prime number")
    elif prime > 1:
        print(f"The number {number} is not a prime number")
    else:
        print("The number 1 is neither of both ")
      
# Write your code above this line
# Define the function prime_checker() so the code below work
# Don't change the code above

n = int(input())
prime_checker(number=n)
