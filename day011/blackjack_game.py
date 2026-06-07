from winner import winner
from draw import draw
from endgame import endgame
from clear import clear
from blackjack_logo import logo

def play_new_game(start_game):
    logo()
    print("Welcome to the PyCharm Casino")
    print("where all your dreams come true")
    print("Tonight's game is a big night blackjack")
    player_hand = draw(2)
    computer_hand = draw(2)
    sum_computer = sum(computer_hand)
    sum_player = sum(player_hand)
    cards = 2
    print("All right, here is your hand")
    print(player_hand)
    print("Here is mine")
    print(f"[{computer_hand[0]}]")
    win_computer = False
    win_player = False

  while start_game[0] == "y":
        if sum_player != 21 and sum_computer != 21:
            while sum_player < 21 and input("Do you want another card?: ").lower() == "y":
                clear()
                if cards < 6:
                    cards += 1
                    card = draw(1)
                    player_hand.append(card[0])
                    sum_player = sum(player_hand)
                    if 11 in player_hand and sum(player_hand) > 21:
                        player_hand[player_hand.index(11)] = 1
                        sum_player -= 10
                    print(player_hand)

            while not sum_computer > 17 and not sum_player > 21:
                card = draw(1)
                computer_hand.append(card[0])
                sum_computer = sum(computer_hand)
                if 11 in player_hand and sum(player_hand) > 21:
                    player_hand[player_hand.index(11)] = 1
                    sum_player -= 10
                print(computer_hand)

            print(f"Your hand: {player_hand}")
            print(f"Dealer hand: {computer_hand}")

        win = endgame(sum_player, sum_computer)
        if win[0] == True or win[1] == True:
            winner(win[0], win[1])
            start_game = "n"


start_game = input("Do you wanna play Blackjack?: Y/N ").lower()
play_new_game(start_game[0])
new_game = input("Do you wanna play again?: Y/N ").lower()

if new_game=="y":
    clear()
    play_new_game(new_game[0])
else:
    clear()
    print("Goodbye!!!")
