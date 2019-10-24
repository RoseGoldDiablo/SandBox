from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class Button(QPushButton):
    def __init__(self, window, x, y):
        super().__init__()



class ToolBox(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'ToolBox'
        self.left = 10
        self.top = 10
        self.width = 650
        self.height = 500
        self.mainMenu()

    def mainMenu(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
        softwareButton.show()

    def makeButton(self):
        self.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    exe = ToolBox()
    sys.exit(app.exec_())
