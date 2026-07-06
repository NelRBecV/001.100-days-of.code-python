import pandas


nato_res = pandas.read_csv("nato_alphabet.csv")
#nato_alphabet = {row.letter: row.code for (index, row) in nato_res.iterrows()}
#iterrows, as its name says, iterate over DataFrame rows as (index, Series) pairs.

nato_alphabet = {nato_res["Letter"][letter]:nato_res["Word"][letter] for letter in range(len(nato_res["Letter"]))}
# nato_letter = nato_alphabet.keys()
# nato_word = nato_alphabet.values()
# nato_a = pandas.DataFrame({"Letter": nato_letter, "Word": nato_word})
# nato_a.to_csv("nato_alphabet.csv", index=False)
#index=False prevents pandas from adding the goddamn "Zero" column

nato: list = []
print("Python's Nato Alphabeth Conversor")

# my method
while True:
    try:
        word = list(input("Enter a word: ").upper())
        nato = [nato_alphabet[letter] for letter in word]
        if len(nato) == 0:
            raise KeyError
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        print(f"Your NATO word is: {nato}")
        break

#Angela's Method
# def generate_phonetics():
#     word = list(input("Enter a word: ").upper())
#     try:
#         nato = [nato_alphabet[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please")
#         generate_phonetics()
#     else:
#         print(f"Your NATO word is: {nato}")

# generate_phonetics()
