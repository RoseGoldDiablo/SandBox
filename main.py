from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


# Function for deleting all items in  layout
def clearLayout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget() is not None:
            child.widget().deleteLater()
        elif child.layout() is not None:
            clearLayout(child.layout())


# ----------------------------------------------------------------------------------------------------------------------


# Class: UI (user interface)
# Description: Used to house the basics for setting up User Interface
class UI(QWidget):
    vlayout = None
    hlayout = None
    def __init__(self):
        super().__init__()
        self.title = 'ToolBox'
        self.left = 200
        self.top = 100
        self.width = 650
        self.height = 500
        self.Welcome()

    # Function for creating the Welcome window. Sets the window size, location on the screen, title for the window
    # and all the buttons and labels on the window

    def Welcome(self):
        # Function for closing the Welcome window
        def NextWindow():
            clearLayout(hlayout)
            clearLayout(vlayout)
            # Calls the next menu
            self.MainMenu()

        # --------------------------------------------------------------------------------------------------------------

        # Defining the layout
        global vlayout
        global hlayout
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        self.setLayout(vlayout)
        # --------------------------------------------------------------------------------------------------------------
        # Widgets
        WelcomeTitle = QLabel('Welcome')
        ContinueButton = QPushButton('Continue')
        # --------------------------------------------------------------------------------------------------------------
        # Setting the Layout (Vertical)
        vlayout.addStretch()
        vlayout.addWidget(WelcomeTitle)
        vlayout.addStretch()
        # --------------------------------------------------------------------------------------------------------------
        # Setting the Layout (Horizontal)
        hlayout.addStretch()
        hlayout.addWidget(ContinueButton)
        hlayout.addStretch()
        vlayout.addLayout(hlayout)
        vlayout.addStretch()
        # --------------------------------------------------------------------------------------------------------------
        # Aligns the text in label to the center
        WelcomeTitle.setAlignment(Qt.AlignHCenter)
        # --------------------------------------------------------------------------------------------------------------
        ContinueButton.clicked.connect(NextWindow)
        # Sets and shows the window
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
        # --------------------------------------------------------------------------------------------------------------

    # Function for creating the Main Menu window.
    def MainMenu(self):
        global vlayout
        global hlayout
        self.title = 'Main Menu'
        MainMenuTitle = QLabel('Main Menu')
        vlayout.addStretch()
        vlayout.addWidget(MainMenuTitle)
        vlayout.addStretch()
        MainMenuTitle.setAlignment(Qt.AlignCenter)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)


# Function that starts the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    exe = UI()
    sys.exit(app.exec_())
