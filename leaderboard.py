
import sys

from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QGridLayout,QVBoxLayout, QLabel, QWidget, QMainWindow, QPushButton
from PySide6.QtCore import QSize, Qt


#this is the leaderboard itself
class MainWindow(QMainWindow):

    #on initialisation, just sets the title and size. the labels will be filled in by the update_gui function, which is called every time a player moves
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Draft Ordering")
        self.setFixedSize(QSize(1000, 800))

    #this fills in the labels
    def update_gui(self, player_list):
        #overall layout for the leaderboard
        leaderboard_layout = QVBoxLayout()

        #titles done like this so they can be styled differently to the player labels. colheader labels are assigned different styling
        titles_layout = QGridLayout()
        title_label1 =QLabel("Position")
        title_label1.setObjectName("colheader")
        title_label2 = QLabel("Player")
        title_label2.setObjectName("colheader")
        title_label3 = QLabel("Status")
        title_label3.setObjectName("colheader")
        title_label4 = QLabel("Distance to go")
        title_label4.setObjectName("colheader")
        titles_layout.addWidget(title_label1, 0, 0)
        titles_layout.addWidget(title_label2, 0, 1)
        titles_layout.addWidget(title_label3, 0, 2)
        titles_layout.addWidget(title_label4, 0, 3)       

        #goes through each row and assigns the relevant player to those labels and fills in
        player1_layout = QGridLayout()
        player1_layout.addWidget(QLabel("1. "), 0, 0)
        player1_layout.addWidget(QLabel(player_list[0].name), 0, 1)
        finished_label = QLabel("Finished" if player_list[0].finished == 1 else "")
        player1_layout.addWidget(finished_label, 0, 2)
        player1_layout.addWidget(QLabel(str(player_list[0].togo)), 0, 3)

        player2_layout = QGridLayout()
        player2_layout.addWidget(QLabel("2. "), 0, 0)
        player2_layout.addWidget(QLabel(player_list[1].name), 0, 1)
        finished_label = QLabel("Finished" if player_list[1].finished == 1 else "")
        player2_layout.addWidget(finished_label, 0, 2)
        player2_layout.addWidget(QLabel(str(player_list[1].togo)), 0, 3)

        player3_layout = QGridLayout()
        player3_layout.addWidget(QLabel("3. "), 0, 0)
        player3_layout.addWidget(QLabel(player_list[2].name), 0, 1)
        finished_label = QLabel("Finished" if player_list[2].finished == 1 else "")
        player3_layout.addWidget(finished_label, 0, 2)
        player3_layout.addWidget(QLabel(str(player_list[2].togo)), 0, 3)

        player4_layout = QGridLayout()
        player4_layout.addWidget(QLabel("4. "), 0, 0)
        player4_layout.addWidget(QLabel(player_list[3].name), 0, 1)
        finished_label = QLabel("Finished" if player_list[3].finished == 1 else "")
        player4_layout.addWidget(finished_label, 0, 2)
        player4_layout.addWidget(QLabel(str(player_list[3].togo)), 0, 3)

        player5_layout = QGridLayout()
        player5_layout.addWidget(QLabel("5. "), 0, 0)
        player5_layout.addWidget(QLabel(player_list[4].name), 0, 1)
        finished_label = QLabel("Finished" if player_list[4].finished == 1 else "")
        player5_layout.addWidget(finished_label, 0, 2)
        player5_layout.addWidget(QLabel(str(player_list[4].togo)), 0, 3)

        player6_layout = QGridLayout()
        player6_layout.addWidget(QLabel("6. "), 0, 0)
        player6_layout.addWidget(QLabel(player_list[5].name), 0, 1)
        finished_label = QLabel("Finished" if player_list[5].finished == 1 else "")
        player6_layout.addWidget(finished_label, 0, 2)
        player6_layout.addWidget(QLabel(str(player_list[5].togo)), 0, 3)

        player7_layout = QGridLayout()
        player7_layout.addWidget(QLabel("7. "), 0, 0)
        player7_layout.addWidget(QLabel(player_list[6].name), 0, 1)
        finished_label = QLabel("Finished" if player_list[6].finished == 1 else "")
        player7_layout.addWidget(finished_label, 0, 2)
        player7_layout.addWidget(QLabel(str(player_list[6].togo)), 0, 3)

        player8_layout = QGridLayout()
        player8_layout.addWidget(QLabel("8. "), 0, 0)
        player8_layout.addWidget(QLabel(player_list[7].name), 0, 1)
        finished_label = QLabel("Finished" if player_list[7].finished == 1 else "")
        player8_layout.addWidget(finished_label, 0, 2)
        player8_layout.addWidget(QLabel(str(player_list[7].togo)), 0, 3)

        player9_layout = QGridLayout()
        player9_layout.addWidget(QLabel("9. "), 0, 0)
        player9_layout.addWidget(QLabel(player_list[8].name), 0, 1)
        finished_label = QLabel("Finished" if player_list[8].finished == 1 else "")
        player9_layout.addWidget(finished_label, 0, 2)
        player9_layout.addWidget(QLabel(str(player_list[8].togo)), 0, 3)

        player10_layout = QGridLayout()
        player10_layout.addWidget(QLabel("10. "), 0, 0)
        player10_layout.addWidget(QLabel(player_list[9].name), 0, 1)
        finished_label = QLabel("Finished" if player_list[9].finished == 1 else "")
        player10_layout.addWidget(finished_label, 0, 2)
        player10_layout.addWidget(QLabel(str(player_list[9].togo)), 0, 3)

        #adds each row of labels above to the overall leaderboard layout, which is then set as the central widget of the window
        leaderboard_layout.addLayout(titles_layout)
        leaderboard_layout.addLayout(player1_layout)
        leaderboard_layout.addLayout(player2_layout)
        leaderboard_layout.addLayout(player3_layout)
        leaderboard_layout.addLayout(player4_layout)
        leaderboard_layout.addLayout(player5_layout)
        leaderboard_layout.addLayout(player6_layout)
        leaderboard_layout.addLayout(player7_layout)
        leaderboard_layout.addLayout(player8_layout)
        leaderboard_layout.addLayout(player9_layout)
        leaderboard_layout.addLayout(player10_layout)

        #leaderboard layout then set to be central widget of the window, so it is displayed on the screen
        central_widget = QWidget(self)
        central_widget.setObjectName("centralWidget")
        central_widget.setLayout(leaderboard_layout)
        self.setCentralWidget(central_widget)





