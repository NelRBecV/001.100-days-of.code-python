target = int(input())#Enter a number between 0 to 1000
#Do not change the code below
sum_even = 0
#Write your code below this row
for even in range(0, target+1, 2):
    sum_even += even

print(f"{sum_even}")