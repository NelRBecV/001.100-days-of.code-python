fruits = eval(input())
# Do not change the code above

#TODO: Catch the exception an make sure the code runs without crashing
#introduce 'apple', 'pear', 'orange' as input on console

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")

#Do not change the code below
make_pie(4)
