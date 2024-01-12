from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3


# DB = sqlite3.connect('server_for_game.db')
# SQL = DB.cursor()
# al = SQL.execute("SELECT * FROM users ORDER BY score DESC").fetchall()
# num_1 = al[0]
# num_2 = al[1]
# num_3 = al[2]


class leader_board_Widget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('leader_board_qt.ui', self)
        self.exit_bottom.setIcon(QIcon('Images/exit_icon.png'))
        self.setWindowIcon(QIcon('Images/pedestal_1.png'))
        self.label.setPixmap(QPixmap('Images/first_place_64.png'))
        self.label_2.setPixmap(QPixmap('Images/second_place_64.png'))
        self.label_3.setPixmap(QPixmap('Images/third_place_64.png'))

        self.exit_bottom.clicked.connect(self.exit_settings)

        DB = sqlite3.connect('server_for_game.db')
        SQL = DB.cursor()
        al = SQL.execute("SELECT * FROM users ORDER BY score DESC").fetchall()
        num_1 = al[0]
        num_2 = al[1]
        num_3 = al[2]

        score_label_1 = QLabel(self)
        score_label_1.setGeometry(120, 30, 200, 50)
        font = QFont()
        font.setPointSize(14)
        score_label_1.setFont(font)
        score_label_1.setText(f"{num_1[0]} - {num_1[1]}")

        score_label_2 = QLabel(self)
        score_label_2.setGeometry(120, 100, 200, 50)
        font = QFont()
        font.setPointSize(14)
        score_label_2.setFont(font)
        score_label_2.setText(f"{num_2[0]} - {num_2[1]}")

        score_label_3 = QLabel(self)
        score_label_3.setGeometry(120, 170, 200, 50)
        font = QFont()
        font.setPointSize(14)
        score_label_3.setFont(font)
        score_label_3.setText(f"{num_3[0]} - {num_3[1]}")

    def exit_settings(self):
        self.close()
