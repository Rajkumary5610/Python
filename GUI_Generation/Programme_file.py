# How to Create the GUI, Label, Images, Layouts using python module PyQt5

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout,
                             QGridLayout, QPushButton)                              # Used to create window and application
from PyQt5.QtGui import QIcon, QFont, QPixmap                                       # Used to create Icon of the Window
from PyQt5.QtCore import Qt

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My cool first GUI')                                    # Naming the window
        self.setGeometry(600, 250, 400, 400)                                        # Adjusting the window axis and size
        self.setWindowIcon(QIcon('Profile_image.jpg'))                              # Setting window icon
        self.button = QPushButton('Click me', self)
        self.label = QLabel('Hello!', self)
        self.initUI()

        # Label setting
        # label = QLabel('Hello', self)
        # label.setFont(QFont("Time's now", 40))
        # label.setGeometry(0, 0, 400, 100)
        # label.setStyleSheet("color: #4334eb;"
        #                     "background-color: #eb3446;"
        #                    "font-weight: bold;"
        #                    "font-style: italic;"
        #                    "text-decoration: underline;")
        # label.setAlignment(Qt.AlignTop)                                             # Vertically Top
        # label.setAlignment(Qt.AlignBottom)                                          # Vertically Bottom
        # label.setAlignment(Qt.AlignVCenter)                                         # Vertically Center

        # label.setAlignment(Qt.AlignRight)                                           # Horizontally Right
        # label.setAlignment(Qt.AlignHCenter)                                         # Horizontally Center
        # abel.setAlignment(Qt.AlignLeft)                                             # Horizontally Left

        # label.setAlignment(Qt.AlignCenter)                                          # Center Horizontally and Vertically

        # label.setAlignment(Qt.AlignTop | Qt.AlignRight)                             # Top Right
        # label.setAlignment(Qt.AlignBottom | Qt.AlignRight)                          # Bottom Right
        # label.setAlignment(Qt.AlignTop | Qt.AlignLeft)                              # Top Left
        # label.setAlignment(Qt.AlignBottom | Qt.AlignLeft)                           # Bottom Left
        # label.setAlignment(Qt.AlignVCenter | Qt.AlignTop)                           # Vertically Center Top
        # label.setAlignment(Qt.AlignVCenter | Qt.AlignBottom)                        # Vertically Center Bottom
        # label.setAlignment(Qt.AlignVCenter | Qt.AlignRight)                         # Vertically Center Right
        # label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)                          # Vertically Center left
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)                           # Horizontally Center Top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)                        # Horizontally Center Bottom
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignRight)                         # Horizontally Center Right
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignLeft)                          # Horizontally Center left
        # label.setAlignment(Qt.AlignCenter)

        # Image setting
        # label = QLabel(self)
        # label.setGeometry(0, 0, 250, 250)

        # pixmap = QPixmap("Profile_image.jpg")
        # label.setPixmap(pixmap)

        # label.setScaledContents(True)
        # label.setGeometry((self.width() - label.width()) // 2,
        #                 (self.height() - label.height()) // 2,
        #                  label.width(),
        #                  label.height())

    # Layout setting
    #def initUI(self):
        # central_widget = QWidget()
        # self.setCentralWidget(central_widget)

        # label1 = QLabel("#1", self)
        # label2 = QLabel("#2", self)
        # label3 = QLabel("#3", self)
        # label4 = QLabel("#4", self)
        # label5 = QLabel("#5", self)

        # label1.setStyleSheet("background-color: red;")
        # label2.setStyleSheet("background-color: yellow;")
        # label3.setStyleSheet("background-color: green;")
        # label4.setStyleSheet("background-color: blue;")
        # label5.setStyleSheet("background-color: purple;")

        # vbox = QVBoxLayout()
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)
        # central_widget.setLayout(vbox)

        # hbox = QHBoxLayout()
        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        # hbox.addWidget(label5)
        # central_widget.setLayout(hbox)

        # grid = QGridLayout()
        # grid.addWidget(label1, 0, 0)
        # grid.addWidget(label2, 0, 1)
        # grid.addWidget(label3, 1, 0)
        # grid.addWidget(label4, 1, 1)
        # grid.addWidget(label5, 2, 3)
        # central_widget.setLayout(grid)

    # Pushing Button

    def initUI(self):
        self.button.setGeometry(100, 100, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(130, 200, 200, 100)
        self.label.setStyleSheet("font-size: 60px;")

    def on_click(self):
        self.lebel.setText("Goodbye ")
        print("Button Clicked")
        self.button.setText('Clicked')
        self.button.setDisabled(True)

class main():
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()