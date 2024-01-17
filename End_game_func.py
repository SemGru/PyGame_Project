from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Dataset_base import save_plaer
from PyGame_next_vers import get_score
from PyQt5.QtCore import QRect


class end_game_Widget(QWidget):
    def __init__(self):
        super().__init__()
        # Загрузка qt файла
        uic.loadUi('end_game_1.0.ui', self)
        # Создание картинок/иконок
        self.exit_bottom.setIcon(QIcon('Images/exit_icon.png'))
        self.setWindowIcon(QIcon('Images/icon_game_2.png'))
        # Создание надписи вручную
        score_label = QLabel(self)
        score_label.setGeometry(190, 110, 100, 50)
        font = QFont()
        font.setPointSize(14)
        score_label.setFont(font)
        score_label.setText(f"{get_score()}")

        self.line_Edit = QLineEdit(self)
        self.line_Edit.setGeometry((QRect(50, 230, 100, 30)))
        # Реакция кнопок
        self.exit_bottom.clicked.connect(self.exit_settings)
        self.save_game_bottom.clicked.connect(self.save_game)

    def get_scored(self):
        pass

    def exit_settings(self):
        self.close()

    def save_game(self):
        # Сохранение игры через абзу данных
        save_plaer(self.line_Edit.text(), get_score())
        self.close()
