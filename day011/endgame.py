def endgame(sum_player,sum_computer):
    win_player=False
    win_computer = False
    if sum_player == sum_computer:
        win_computer = True
        win_player = True
    elif sum_player > 21:
        win_computer = True
        win_player = False
    elif sum_computer > 21:
        win_computer = True
        win_player = False
    elif sum_player > sum_computer:
        win_computer = False
        win_player = True
    elif sum_player < sum_computer and sum_computer < 21:
        win_computer = True
        win_player = False
    elif sum_computer == 21:
        win_computer = True
        win_player = False
    else:
        win_player = True
        win_computer = False

    return win_player, win_computer
