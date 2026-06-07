def winner(win_player, win_computer):
    if win_computer and win_player:
        print("What do we got here? It's a PUSH!!!")
    elif not win_computer and win_player:
        print("Congratulations, pal. You WIN!!!")
    else:
        print("Sorry, man. You LOSE")

