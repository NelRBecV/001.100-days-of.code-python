from clear import clear
from blackjack_logo import logo
import random


def get_game_deck() -> list:
    cards_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards_numbers = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    cards_suits = ["DIAMONDS", "HEARTS", "CLUBS", "SPADES"]
    deck: list = []
    for suit in range(len(cards_suits)):
        for num in range(len(cards_values)):
            deck.append({"suit": suit, "symbol": cards_numbers[num], "value": cards_values[num]})
    random.shuffle(deck)

    return deck


def calculate_score(hand: list) -> int:
    hand_count: int = 0
    for card in hand:
        hand_count += card['value']
    if hand_count > 21:
        for card in hand:
            if card['symbol'] == "A":
                card['value'] = 1
                hand_count -= 10
    return hand_count


def draw_card(deck: list) -> dict:
    card = random.choice(deck)
    deck.remove(card)

    return card


def find_game_winner(player1: list, player2: list) -> int:
    p1_cards = calculate_score(player1)
    p2_cards = calculate_score(player2)

    if p1_cards > 21:
        return 2

    if p2_cards > 21:
        return 1

    if p1_cards == p2_cards:
        return 0
    if p1_cards > p2_cards or p1_cards == 21:
        return 1
    if p2_cards > p1_cards or p2_cards == 21:
        return 2
    return -1


def show_cards(hand: list) -> str:
    cards: list = []
    for card in hand:
        cards.append(str(card['value']))

    return " ".join(cards)


def play_game():
    deck: list = get_game_deck()
    player_hand: list = [draw_card(deck) for _ in range(2)]
    computer_hand: list = [draw_card(deck) for _ in range(2)]
    print(f"All right, here is your hand: {show_cards(player_hand)}, score: {calculate_score(player_hand)}")
    print(f"Here is my first card: {computer_hand[0]['value']}")

    end_round = False
    while not end_round:
        while calculate_score(player_hand) < 21:
            if input("Do you want another card?: ").lower() == "n":
                break
            player_hand.append(draw_card(deck))
            clear()
            print(show_cards(player_hand))

        while True:
            if calculate_score(player_hand) > 21 or calculate_score(computer_hand) >= calculate_score(player_hand):
                break
            computer_hand.append(draw_card(deck))

        end_round = True

    print(f"Your hand: {show_cards(player_hand)}, score: {calculate_score(player_hand)}")
    print(f"Dealer's hand: {show_cards(computer_hand)}, score: {calculate_score(computer_hand)}")
    print()
    winner = find_game_winner(player_hand,computer_hand)
    if winner != 0:
        player = "Dealer has"
        if winner == 1:
            player = "You have"

        print(f"{player} won this round.")
    else:
        print("There's no winner. It's a draw!")


if __name__ == "__main__":
    logo()
    print("Welcome to the PyCharm Casino")
    print("where all your dreams come true")
    print("Tonight's game is a big night blackjack")
    play: bool = True

    while play:
        clear()
        play_game()
        if input("Do you wanna play another round?: Y/N ").lower() == "n":
            play = False

    print("Goodbye!!!")
