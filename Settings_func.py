import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

IMAGE = 'Images/space.jpg'
Flag = True
Flag1 = True
kolik = False
SOUND_MUSIC = True
SOUND_EFFECTS = True


class settings_Widget(QWidget):
    def __init__(self):
        global Flag
        super().__init__()
        # Загрузка qt файла
        uic.loadUi('Settings_qt.ui', self)

        # Создание картинок/иконок
        self.exit_bottom.setIcon(QIcon('Images/exit_icon.png'))
        self.setWindowIcon(QIcon('Images/settinds_icon.png'))

        # Установка картинок, работает звук или нет
        if Flag:
            self.sound_bottom.setIcon(QIcon('Images/sound_on.png'))
        else:
            self.sound_bottom.setIcon(QIcon('Images/sound_off.png'))

        if Flag1:
            self.pushButton_4.setIcon(QIcon('Images/sound_on.png'))
        else:
            self.pushButton_4.setIcon(QIcon('Images/sound_off.png'))

        # Реакция кнопок
        self.sound_bottom.clicked.connect(self.Change_icon_sound)
        self.exit_bottom.clicked.connect(self.exit_settings)
        self.pushButton.clicked.connect(self.kol_space)
        self.pushButton_2.clicked.connect(self.kol_mars)
        self.pushButton_3.clicked.connect(self.kol_desert)
        self.pushButton_4.clicked.connect(self.Change_icon_sound_effect)

    # Изменени картинок на кнопке музыки
    def Change_icon_sound(self):
        global Flag
        if Flag:
            self.sound_bottom.setIcon(QIcon('Images/sound_off.png'))
            Flag = False
            kolp()
        else:
            self.sound_bottom.setIcon(QIcon('Images/sound_on.png'))
            Flag = True
            kolp()

    # Изменени картинок на кнопке звуковых эффектов
    def Change_icon_sound_effect(self):
        global Flag1
        if Flag1:
            self.pushButton_4.setIcon(QIcon('Images/sound_off.png'))
            Flag1 = False
            kolp1()
        else:
            self.pushButton_4.setIcon(QIcon('Images/sound_on.png'))
            Flag1 = True
            kolp1()

    # Вспомогательные фунции для работы с задним фоном
    def kol_space(self):
        kol('space')

    def kol_mars(self):
        kol('mars')

    def kol_desert(self):
        kol('desert')

    def exit_settings(self):
        self.close()


# Куча вспомогательных функций
def kolp():
    global SOUND_MUSIC
    if SOUND_MUSIC:
        SOUND_MUSIC = False
    else:
        SOUND_MUSIC = True


def kolp1():
    global SOUND_EFFECTS
    if SOUND_EFFECTS:
        SOUND_EFFECTS = False
    else:
        SOUND_EFFECTS = True


def kol(lp):
    global IMAGE
    if lp == 'space':
        IMAGE = 'Images/space.jpg'
        return True
    if lp == 'mars':
        IMAGE = 'Images/mars.jpg'
        return True
    if lp == 'desert':
        IMAGE = 'Images/desert.jpg'
        return True


def get_background():
    return IMAGE


def get_sound_music():
    return SOUND_MUSIC


def get_sound_effects():
    return SOUND_EFFECTS
