
#imports for the random number work and the apps
import random
import sys

#imports for the GUI elements used here
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

#brings through my GUI (set out in leaderboard) and player objects (set out in players)
#reorder function also stored in players
from leaderboard import MainWindow
from players import Player, reorder_players

#define the app and set the style sheet to the one I created
app = QApplication(sys.argv)
app.setStyleSheet(open("style.qss").read())

#create instances of players and name them
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

#collate players into a list
player_list = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10]
for player in player_list:
    player.currentpos = player_list.index(player) + 1
#sets current pos in line with their position in the list (1-10), but no movement done yet

window = MainWindow()
window.show()
#sets out that the window is my mainWindow object, and shows it on the screen

#function to randomly move one player forwards
def one_number_step():
    num = random.randint(1, 10)

    if player1.finished == 0 and num == 1:
        player1.togo -= 1
        if player1.togo == 0:
            player1.finished = 1
            player1.finishpos = sum(1 for player in player_list if player.finished == 1)
    if player2.finished == 0 and num == 2:
        player2.togo -= 1
        if player2.togo == 0:
            player2.finished = 1
            player2.finishpos = sum(1 for player in player_list if player.finished == 1)
    if player3.finished == 0 and num == 3:
        player3.togo -= 1
        if player3.togo == 0:
            player3.finished = 1
            player3.finishpos = sum(1 for player in player_list if player.finished == 1)
    if player4.finished == 0 and num == 4:
        player4.togo -= 1
        if player4.togo == 0:
            player4.finished = 1
            player4.finishpos = sum(1 for player in player_list if player.finished == 1)
    if player5.finished == 0 and num == 5:
        player5.togo -= 1
        if player5.togo == 0:
            player5.finished = 1
            player5.finishpos = sum(1 for player in player_list if player.finished == 1)
    if player6.finished == 0 and num == 6:
        player6.togo -= 1
        if player6.togo == 0:
            player6.finished = 1
            player6.finishpos = sum(1 for player in player_list if player.finished == 1)
    if player7.finished == 0 and num == 7:
        player7.togo -= 1
        if player7.togo == 0:
            player7.finished = 1
            player7.finishpos = sum(1 for player in player_list if player.finished == 1)
    if player8.finished == 0 and num == 8:
        player8.togo -= 1
        if player8.togo == 0:
            player8.finished = 1
            player8.finishpos = sum(1 for player in player_list if player.finished == 1)
    if player9.finished == 0 and num == 9:
        player9.togo -= 1
        if player9.togo == 0:
            player9.finished = 1
            player9.finishpos = sum(1 for player in player_list if player.finished == 1)
    if player10.finished == 0 and num == 10:
        player10.togo -= 1
        if player10.togo == 0:
            player10.finished = 1
            player10.finishpos = sum(1 for player in player_list if player.finished == 1)

#defines my variable to halt the calcs
ordering_finished = False

#this does the heavy lifting. runs the random number, and reorders the players based on new positions 
def step_iteration():
    global ordering_finished

    one_number_step()
    player_list[:] = reorder_players(player_list)
    players_not_finished = 0
    for player in player_list:
        player.currentpos = player_list.index(player) + 1
        if player.finished == 0:
            players_not_finished += 1

    #runs the update GUI function to reassign the labels for new player positions
    window.update_gui(player_list)

    #if everyone completed, stops the timer and the loop
    if players_not_finished == 0:
        ordering_finished = True
        timer.stop()

#sets up a timer to run the step_iteration function every 30 milliseconds, and starts the app  
timer = QTimer()
timer.timeout.connect(step_iteration)
timer.start(30)
app.exec()



