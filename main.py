# Import Statements
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


# ----------------------------------------------------------------------------------------------------------------------

# Function for deleting all items in a layout
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
    # Setting global layout variables
    Vertical = None
    Horizontal = None
    
    # Initialize
    def __init__(self):
        super().__init__()
        # Constructing Window title, size, and position
        self.title = 'ToolBox'
        self.left = 200
        self.top = 100
        self.width = 650
        self.height = 500
        self.Welcome()
        
        # --------------------------------------------------------------------------------------------------------------
    
    # Function for creating the Welcome window. Sets the window size, location on the screen, title for the window
    # and all the buttons and labels on the window
    def Welcome(self):
        # Function for authenticating the password and closing the Welcome window if the correct password was entered
        def NextWindow():
            if TEPassword.text() == 'Test':
                
                clearLayout(Horizontal)
                clearLayout(Vertical)
            
                # Calls the next menu
                self.MainMenu()
        
            else:
                TEPassword.setText('Wrong')
        # --------------------------------------------------------------------------------------------------------------
        
        # Defining the layout
        global Vertical
        global Horizontal
        Vertical = QVBoxLayout()
        Horizontal = QHBoxLayout()
        Horizontal2 = QHBoxLayout()
        self.setLayout(Vertical)
        # --------------------------------------------------------------------------------------------------------------
        # Widgets
        WelcomeTitle = QLabel('Welcome')
        ContinueButton = QPushButton('Continue')
        TEPassword = QLineEdit('Enter Password')
        # --------------------------------------------------------------------------------------------------------------
        # Setting the Layout (Vertical)
        Vertical.addStretch()
        Vertical.addWidget(WelcomeTitle)
        Vertical.addStretch()
        Horizontal.addStretch()
        Horizontal.addWidget(TEPassword)
        Horizontal.addStretch()
        Vertical.addLayout(Horizontal)
        
        # --------------------------------------------------------------------------------------------------------------
        # Setting the Layout (Horizontal)
        Horizontal2.addStretch()
        Horizontal2.addWidget(ContinueButton)
        Horizontal2.addStretch()
        Vertical.addLayout(Horizontal2)
        Vertical.addStretch()
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
        # Layout globals
        global Vertical
        global Horizontal
        global Grid
        super().__init__()
        # Constructing Window title, size, and position
        self.title = 'ToolBox'
        self.left = 200
        self.top = 100
        self.width = 650
        self.height = 500
        self.Welcome()

        # ----------------------------------------------------
        
        # Clears layouts and calls Software Loop-er menu
        def CleanUp():
            clearLayout(Vertical)
            clearLayout(Horizontal)
            clearLayout(Grid)
            
        def SLNext():
            CleanUp()
            self.SLMenu()
            
        def P12Next():
            CleanUp()
            self.P12Menu()
        
        # --------------------------------------------------------------------------------------------------------------
        # Sets some changes for the the menu like adding the buttons and changing the window title
        self.title = 'ToolBox'
        SoftwareLoopButton = QPushButton('Software Looper')
        DeleteP12 = QPushButton('P12 Removal')
        Option2 = QPushButton('Option2')
        Option3 = QPushButton('Option3')
        
        # --------------------------------------------------------------------------------------------------------------
        # Sets the layout for the window
        Grid = QGridLayout()
        Vertical.addStretch()
        Grid.addWidget(SoftwareLoopButton, 0, 0)
        Grid.addWidget(DeleteP12, 0, 1)
        Grid.addWidget(Option2, 1, 0)
        Grid.addWidget(Option3, 1, 1)
        Vertical.addLayout(Grid)
        Vertical.addStretch()
        SoftwareLoopButton.clicked.connect(SLNext)
        DeleteP12.clicked.connect(P12Next)
        # --------------------------------------------------------------------------------------------------------------
        
        # Setting the window
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        # --------------------------------------------------------------------------------------------------------------
    
    # Function for creating the software loop window
    def SLMenu(self):
        # Global layout variables
        global Vertical
        global Horizontal
        # Setting the title for the window
        self.title = 'Software Loop-er'
        self.setWindowTitle(self.title)
        # Defining the widgets
        TEComputerNames = QTextEdit()
        Software1 = QPushButton('Software 1')
        Software2 = QPushButton('Software 2')
        Software3 = QPushButton('Software 3')
        Software4 = QPushButton('Software 4')
        Software5 = QPushButton('Software 5')
        Software6 = QPushButton('Software 6')
        
        # Setting the layout
        Grid = QGridLayout()
        Horizontal.addWidget(TEComputerNames)
        Grid.addWidget(Software1, 0, 0)
        Grid.addWidget(Software2, 0, 1)
        Grid.addWidget(Software3, 0, 2)
        Grid.addWidget(Software4, 1, 0)
        Grid.addWidget(Software5, 1, 1)
        Grid.addWidget(Software6, 1, 2)
        Horizontal.addLayout(Grid)
        
        Vertical.addLayout(Horizontal)
        
    def P12Menu(self):
        global Vertical
        global Horizontal
        
    


# Function that starts the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    exe = UI()
    sys.exit(app.exec_())
