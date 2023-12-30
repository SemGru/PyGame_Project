from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Dataset_base import save_plaer
# from PyGame import Global_score
# a = 0


class end_game_Widget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('end_1.0.ui', self)
        self.exit_bottom.setIcon(QIcon('Images/exit_icon.png'))
        self.setWindowIcon(QIcon('Images/Icon.png'))
        # self.score_view.setText(1)

        self.exit_bottom.clicked.connect(self.exit_settings)
        self.save_game_bottom.clicked.connect(self.save_game)

    def exit_settings(self):
        self.close()

    def save_game(self):
        # print(Global_score)
        save_plaer()
        self.close()
# def End_game_fc(Score):
#     second = End_game_Widget()
#     second.show()
