import sys
from PyQt5 import uic
# from PyGame_next_vers import SCOREEE
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

IMAGE = 'Images/space.jpg'
# 1 4 7
Flag = True
Flag1 = True
kolik = False
SOUND_MUSIC = True
SOUND_EFFECTS = True


# def get_background():
#     if self.sound_bottom
#     return 1


class settings_Widget(QWidget):
    def __init__(self):
        global Flag
        super().__init__()
        uic.loadUi('Settings_qt.ui', self)
        if Flag:
            self.sound_bottom.setIcon(QIcon('Images/sound_on.png'))
        else:
            self.sound_bottom.setIcon(QIcon('Images/sound_off.png'))

        if Flag1:
            self.pushButton_4.setIcon(QIcon('Images/sound_on.png'))
        else:
            self.pushButton_4.setIcon(QIcon('Images/sound_off.png'))
        self.exit_bottom.setIcon(QIcon('Images/exit_icon.png'))
        self.setWindowIcon(QIcon('Images/settinds_icon.png'))

        self.sound_bottom.clicked.connect(self.Change_icon_sound)
        self.exit_bottom.clicked.connect(self.exit_settings)
        self.pushButton.clicked.connect(self.kol_space)
        self.pushButton_2.clicked.connect(self.kol_mars)
        self.pushButton_3.clicked.connect(self.kol_desert)
        self.pushButton_4.clicked.connect(self.Change_icon_sound_effect)

        # self.radioButton_space.clicked.connect(self.get_background('space'))
        # self.radioButton_desert.clicked.connect(self.get_background('desert'))
        # self.radioButton_mars.clicked.connect(self.get_background('mars'))
        # if self.comboBox_back.currentText() == 'Space':
        # elif self.comboBox_back.currentText() == 'Mars':
        #     IMAGE = '1.jpg'
        #     IMAGE = '4.jpg'
        # elif self.comboBox_back.currentText() == 'Desert':
        #     IMAGE = '7.jpg'

    # def change_bc_ground(self, img):
    #     # pass
    #     if img == 'space':
    #         kol('space')
    #     elif img == 'mars':
    #         kol('mars')
    #     elif img == 'desert':
    #         kol('desert')
    def kol_space(self):
        kol('space')

    def kol_mars(self):
        kol('mars')

    def kol_desert(self):
        kol('desert')

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

    def exit_settings(self):
        self.close()


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
