from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Dataset_base import save_plaer
from PyGame_next_vers import get_score
from PyQt5.QtCore import QRect


# from PyGame import Global_score
# SCORE = 0


class end_game_Widget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('end_game_1.0.ui', self)
        self.exit_bottom.setIcon(QIcon('Images/exit_icon.png'))
        self.setWindowIcon(QIcon('Images/icon_game_2.png'))
        # self.score_view.setText(1)
        # self.label.setText(1)
        score_label = QLabel(self)
        score_label.setGeometry(190, 110, 100, 50)
        font = QFont()
        font.setPointSize(14)
        score_label.setFont(font)
        score_label.setText(f"{get_score()}")
        self.exit_bottom.clicked.connect(self.exit_settings)
        self.save_game_bottom.clicked.connect(self.save_game)

        self.line_Edit = QLineEdit(self)
        self.line_Edit.setGeometry((QRect(50, 230, 100, 30)))
        # self.line_Edit.setFont(font_12)
        # self.line_Edit.setFocusPolicy(QtCore.Qt.ClickFocus)
        #         # self.line_Edit.setClearButtonEnabled(True)

    def get_scored(self):
        pass

    def exit_settings(self):
        self.close()

    def save_game(self):
        save_plaer(self.line_Edit.text(), get_score())
        self.close()
# def End_game_fc(Score):
#     second = End_game_Widget()
#     second.show()
