def add(*num):
    result = 0
    for n in num:
        result += n
    print(result)


add(15, 25, 80, 45, 30, 90)
numbers = input("Introduce a lot of numbers: ").split(" ")
alo_numbers = [int(q) for q in numbers]
add(*alo_numbers)
