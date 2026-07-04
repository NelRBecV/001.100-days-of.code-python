nato_alphabet: dict = {"A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta",
                 "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel",
                 "I": "India", "J": "Juliett", "K": "Kilo", "L": "Lima",
                 "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa",
                 "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
                 "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "Xray",
                 "Y": "Yankiee", "Z": "Zulu"
                 }
nato: list = []

# Get word letters
word = list(input("Python's Nato Alphabeth Conversor\nEnter a word: ").upper()) #Method 1
# name.split() #Method 2

# Get NATO code from given letters
# for letter in name: #method 1
#     nato.append(nato_alphabet[letter.upper()])
nato: list = [nato_alphabet[letter] for letter in word if letter in nato_alphabet] #Method 2
print(nato)
