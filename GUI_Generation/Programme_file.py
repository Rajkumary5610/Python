# How to Create the GUI using python module PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow           #Used to create Window and Application
from PyQt5.QtGui import QIcon                                   #Used to create Icon of the Window

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My cool first GUI')                                    #Naming the window
        self.setGeometry(600, 250, 400, 400)                                        # Adjusting the window axis and size
        self.setWindowIcon(QIcon('Profile_image.jpg'))        # Setting window icon

class main():
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()