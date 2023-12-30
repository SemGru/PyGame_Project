import sys
from PyQt5 import uic

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

Flag = True


class Main_set(QWidget):
    def __init__(self):
        global Flag
        super().__init__()
        uic.loadUi('test_1.ui', self)
        self.sound_bottom.setIcon(QIcon('Images/sound_on.png'))

        self.sound_bottom.clicked.connect(self.Change_icon)

    def Change_icon(self):
        global Flag
        if Flag:
            self.sound_bottom.setIcon(QIcon('Images/sound_off.png'))
            Flag = False
        else:
            self.sound_bottom.setIcon(QIcon('Images/sound_on.png'))
            Flag = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_set()
    ex.show()
    try:
        sys.exit(app.exec())
    except KeyboardInterrupt:
        pass


def stru():
    app = QApplication(sys.argv)
    ex = Main_set()
    ex.show()
    try:
        sys.exit(app.exec())
    except KeyboardInterrupt:
        pass
