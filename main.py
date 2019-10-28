from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class Button(QPushButton):
    button = None
    command = None
    
    def __init__(self, window, x, y, text):
        super().__init__()
        self.window = window
        self.x = x
        self.y = y
        self.text = text
    
    def makeButton(self):
        self.button = QPushButton(self.text, self.window)
        self.button.move(self.x, self.y)
    
    def onClick(self, command):
        self.button.clicked.connect(command)


class Label(QLabel):
    label = None
    font = 'Source Code Pro'
    fontSize = '20pt'
    
    def __init__(self, window, text, x, y):
        super().__init__()
        self.window = window
        self.text = text
        self.x = x
        self.y = y
    
    def makeLabel(self):
        self.label = QLabel(self.text, self.window)
        self.label.setStyleSheet("font: " + self.fontSize + " " + self.font)
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


class ui(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'ToolBox'
        self.left = 200
        self.top = 100
        self.width = 650
        self.height = 500
        self.Welcome()
    
    def Welcome(self):
        def close():
            ContinueButton.clear()
            titleLabel.clear()
            
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        ContinueButton = Button(self, 280, 380, 'Continue')
        ContinueButton.makeButton()
        ContinueButton.onClick(close)
        ContinueButton.onClick(self.MainMenu)
        titleLabel = Label(self, 'ToolBox', 270, 75)
        titleLabel.makeLabel()
        
        self.show()
    
    def MainMenu(self):
        self.title = 'Main Menu'
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    exe = ui()
    sys.exit(app.exec_())

