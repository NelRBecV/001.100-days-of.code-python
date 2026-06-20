import time
from turtle import Screen
from player import Player
from level import Level

scenario = Screen()
scenario.setup(600, 600)
player = Player()
scenario.listen()
game_level = Level()
game_level.enemies()
scenario.onkey(player.move_player, 'w')

while True:
    if not player.is_crossed():
        game_level.move_enemies()
        game_over: bool = game_level.is_endgame(player)
        if game_over:
            player.set_player_health(False)
            break

        time.sleep(0.1)
        scenario.update()
    else:
        player.reset_player()

    if player.is_crossed():
        game_level.increment_scoreboard()

    game_level.scoreboard()

scenario.exitonclick()
