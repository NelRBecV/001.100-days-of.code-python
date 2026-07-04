def add(*num):
    result = 0
    for n in num:
        result += n
    print(result)


# num = input("Introduce a lot of numbers: ").split()
# alo_numbers = [int(q) for q in num]
# add(alo_numbers)
# result = [add(cipher) for cipher in alo_numbers]
# print(result)
add(15, 25, 80, 45, 30, 90)
