from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class info_Widget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('info_qt.ui', self)
        self.exit_bottom.setIcon(QIcon('Images/exit_icon.png'))
        self.setWindowIcon(QIcon('Images/info_icon.png'))

        self.exit_bottom.clicked.connect(self.exit_settings)

    def exit_settings(self):
        self.close()
