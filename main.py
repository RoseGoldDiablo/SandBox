from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class Button(QPushButton):
    width = 75
    height = 35
    button = None

    def __init__(self, window, x, y, text):
        super().__init__()
        self.window = window
        self.x = x
        self.y = y
        self.text = text

    def makeButton(self):
        self.button = QPushButton(self.text, self.window)
        self.button.move(self.x, self.y)


class Label(QLabel):
    label = None

    def __init__(self, window, text, x, y):
        super().__init__()
        self.window = window
        self.text = text
        self.x = x
        self.y = y

    def makeLabel(self):
        self.label = QLabel(self.text, self.window)
        self.label.move(self.x, self.y)


class TextBox(QLineEdit):
    textbox = None

    def __init__(self, window, x, y, default):
        super().__init__()
        self.window = window
        self.x = x
        self.y = y
        self.default = default

    def makeTextBox(self):
        self.textbox = QLineEdit(self.default, self.window)
        self.textbox.move(self.x, self.y)




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
        softwareButton = Button(self, 200, 100, 'Software')
        softwareButton.makeButton()
        titleLabel = Label(self, 'Hello', 150, 75)
        titleLabel.makeLabel()
        testEdit = TextBox(self, 200, 300, 'Enter Here')
        testEdit.makeTextBox()
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    exe = ToolBox()
    sys.exit(app.exec_())
