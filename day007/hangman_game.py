from random import choice

word_list = ["pipe", "flower", "glass", "clock", "doorbell", "watermelon", "painting", "cellphone"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


print("Welcome to the Hangman game")

picked_word = choice(word_list)
guessed_word = []
letters_given = []
lives = 7
for _ in range(len(picked_word)):
    guessed_word.append("_")

start_game = True

print(picked_word)

while start_game:
    print(" ".join(guessed_word))
    guess = input("Guess a letter: ").strip()

    if guess not in picked_word and guess not in letters_given:
        lives -= 1
        print(stages[lives])
        if lives >= 1:
            print(f"WRONG!!! Try again.\nLives left: {lives}\n\n")

    #We assume the user will input alphabetical characters only, so we don't check whether the character is a letter or not.
    if guess in letters_given:
        print(f"You already said the {guess} letter")
    else:
        letters_given.append(guess)

    for letter in range(len(picked_word)):
        if picked_word[letter] == guess:
            guessed_word[letter] = guess

    if "_" not in guessed_word or lives == 0:
        start_game = False

if lives > 0:
    print(" ".join(guessed_word))
    print("Congratulations!!! You did it")
else:
    print(f'You lose. The correct word was "{picked_word}"')
