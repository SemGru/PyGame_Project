from PyQt5 import uic
from Leader_board_func import leader_board_Widget
from Info_func import info_Widget
from Settings_func import settings_Widget
from End_game_func import end_game_Widget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyGame_next_vers import Game
from Settings_func import get_background
from Settings_func import get_sound_music
from Settings_func import get_sound_effects

Flag = True


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        # Загрузка qt файла
        uic.loadUi('PyGame_qt.ui', self)
        # Создание картинок/иконок
        self.back_color.setPixmap(QPixmap('Images/menu_game.png'))
        self.setWindowIcon(QIcon('Images/icon_game_2.png'))
        self.Settinds_bottom.setIcon(QIcon('Images/settinds_icon.png'))
        self.Leader_board_bottom.setIcon(QIcon('Images/crown_icon.png'))
        self.info_bottom.setIcon(QIcon('Images/info_icon.png'))
        self.Start_bottom.setIcon(QIcon('Images/ready_icon.png'))

        # Реакция кнопок
        self.Start_bottom.clicked.connect(self.Start)
        self.Leader_board_bottom.clicked.connect(self.Leader_board)
        self.info_bottom.clicked.connect(self.Info)
        self.Settinds_bottom.clicked.connect(self.Settings)

    def End_of_game(self):
        # Окно после окончания игры
        self.second = end_game_Widget()
        self.second.show()

    def Start(self):
        # Начало игры
        # Проверка на звук и уведомление об этом
        if get_sound_music() or get_sound_effects():
            self.dialog('Приготовься, игра сейчас начнётся!\n Советую сделать звук тише.')
        else:
            self.dialog('Приготовься, игра сейчас начнётся!')
        # Вызов функции из другого файла, с самой игрой
        Game(True, get_background(), get_sound_music(), get_sound_effects())
        self.End_of_game()

    def Leader_board(self):
        # Окно с доской лидеров
        self.second = leader_board_Widget()
        self.second.show()

    def Info(self):
        # Окно с информацией об игре
        self.second = info_Widget()
        self.second.show()

    def Settings(self):
        # Окно с настройками
        self.second = settings_Widget()
        self.second.show()

    def dialog(self, info):
        # Создание уведомлений
        dialog = QMessageBox()
        dialog.setText(info)
        dialog.setWindowTitle('Уведомление')
        dialog.setWindowIcon(QIcon('Images/icon_game_2.png'))
        dialog.setIcon(QMessageBox.Information)
        dialog.exec_()
