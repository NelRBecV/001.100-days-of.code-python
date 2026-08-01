target = int(input())  # Enter a number between 0 and 1000
# Do not change the code below

# Write your code below this row
sum_even = 0
for even in range(0, target+1, 2):
    sum_even += even

print(f"{sum_even}")
