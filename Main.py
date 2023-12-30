import sys
from PyQt5.QtWidgets import QApplication
from PyQt import Main

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    try:
        sys.exit(app.exec())
    except KeyboardInterrupt:
        pass


