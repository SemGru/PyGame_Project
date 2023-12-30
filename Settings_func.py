import sys
from PyQt5 import uic

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

Flag = True


class settings_Widget(QWidget):
    def __init__(self):
        global Flag
        super().__init__()
        uic.loadUi('Settings_qt.ui', self)
        self.sound_bottom.setIcon(QIcon('Images/sound_on.png'))
        self.exit_bottom.setIcon(QIcon('Images/exit_icon.png'))
        self.setWindowIcon(QIcon('Images/settinds_icon.png'))

        self.sound_bottom.clicked.connect(self.Change_icon_sound)
        self.exit_bottom.clicked.connect(self.exit_settings)

    def Change_icon_sound(self):
        global Flag
        if Flag:
            self.sound_bottom.setIcon(QIcon('Images/sound_off.png'))
            Flag = False
        else:
            self.sound_bottom.setIcon(QIcon('Images/sound_on.png'))
            Flag = True

    def exit_settings(self):
        self.close()
