
from players import Player, reorder_players
import random


player1 = Player("Felix")
player2 = Player("Jason")
player3 = Player("Mary")
player4 = Player("OJ")
player5 = Player("Will")
player6 = Player("Pete")
player7 = Player("Sam")
player8 = Player("Conor")
player9 = Player("Mad Dog")
player10 = Player("Pearsy")

player_list = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10]
player_list = reorder_players(player_list)
for player in player_list:
    player.currentpos = player_list.index(player) + 1

show_period = 100
num_repeats = 0

ordering_finished = False
while not ordering_finished:

    number_finished =0
    for player in player_list:
        if player.finished == 1:
            number_finished += 1
    if number_finished == len(player_list):
        ordering_finished = True

    num = random.randint(1, 10)

    if player1.finished ==0 and num == 1:
        player1.togo -= 1
        if player1.togo == 0:
            player1.finished = 1
            player1.finishpos = number_finished + 1
    if player2.finished ==0 and num == 2:
        player2.togo -= 1
        if player2.togo == 0:
            player2.finished = 1
            player2.finishpos = number_finished + 1
    if player3.finished ==0 and num == 3:
        player3.togo -= 1
        if player3.togo == 0:
            player3.finished = 1
            player3.finishpos = number_finished + 1
    if player4.finished ==0 and num == 4:
        player4.togo -= 1
        if player4.togo == 0:
            player4.finished = 1
            player4.finishpos = number_finished + 1
    if player5.finished ==0 and num == 5:
        player5.togo -= 1
        if player5.togo == 0:
            player5.finished = 1
            player5.finishpos = number_finished + 1
    if player6.finished ==0 and num == 6:
        player6.togo -= 1
        if player6.togo == 0:
            player6.finished = 1
            player6.finishpos = number_finished + 1
    if player7.finished ==0 and num == 7:
        player7.togo -= 1
        if player7.togo == 0:
            player7.finished = 1
            player7.finishpos = number_finished + 1
    if player8.finished ==0 and num == 8:
        player8.togo -= 1
        if player8.togo == 0:
            player8.finished = 1
            player8.finishpos = number_finished + 1
    if player9.finished ==0 and num == 9:
        player9.togo -= 1
        if player9.togo == 0:
            player9.finished = 1
            player9.finishpos = number_finished + 1
    if player10.finished ==0 and num == 10:
        player10.togo -= 1
        if player10.togo == 0:
            player10.finished = 1
            player10.finishpos = number_finished + 1

    player_list = reorder_players(player_list)
    for player in player_list:
        player.currentpos = player_list.index(player) + 1

    num_repeats += 1

    if num_repeats % show_period == 0:
        for player in player_list:
            print(f"{player.name}: {player.currentpos}")

