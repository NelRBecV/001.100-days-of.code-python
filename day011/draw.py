import random

def draw(card):
    cards_numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    player_hand=[]
    for i in range(card):
        player_hand.append(random.choice(cards_numbers))

    return player_handimport random

def draw(card):
    cards_numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    player_hand=[]
    for i in range(card):
        player_hand.append(random.choice(cards_numbers))

    return player_hand
