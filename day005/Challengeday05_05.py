import random
av_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
              'A','B','C','D','E','F','G','H','I','J','K','L','M',"N","O","P","Q",'R',"S","T",'U',"V","W","X","Y","Z"]
av_numbers = ['0','1','2','3','4','5','6','7','8','9']
av_symbols = ['!','#','$','&','(',')','*','+']

print("Welcome to PyPassword Generator!")
letters = int(input("How many letters do you like in your password?\n"))
symbols = int(input("How many symbols?\n"))
numbers = int(input("How many numbers?\n"))
password = ""
count_letters = 0; count_symbols = 0; count_numbers = 0
total_characters = letters + symbols + numbers
for  i in range(0, total_characters):
    random_type = random.randint(1,3)
    random_letter = random.randint(0, 51)
    random_symbol = random.randint(0,7)
    random_number = random.randint(0,9)
    if random_type == 1:
        if count_symbols < symbols:
            password += str(av_symbols[random_symbol])
            count_symbols +=1
        elif count_numbers < numbers:
            password += str(av_numbers[random_number])
            count_numbers += 1
        else:
            password += av_letters[random_letter]
            count_letters += 1
    elif random_type==2:
        if count_numbers < numbers:
            password += str(av_numbers[random_number])
            count_numbers += 1
        elif count_symbols < symbols:
            password += str(av_numbers[random_symbol])
            count_symbols += 1
        else:
            password += av_letters[random_letter]
            count_letters += 1
    if random_type == 3:
        if count_letters < letters:
            password += av_letters[random_letter]
            count_letters += 1
        elif count_numbers < numbers:
            password += str(av_numbers[random_number])
            count_numbers += 1
        elif count_symbols < symbols:
            password += av_symbols[random_symbol]
            count_symbols += 1

print(f"Here is your password: {password}")