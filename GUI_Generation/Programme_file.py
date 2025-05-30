# How to Create the GUI, Label, Images, Layouts using python module PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel           #Used to create Window and Application
from PyQt5.QtGui import QIcon, QFont, QPixmap                                #Used to create Icon of the Window
from PyQt5.QtCore import Qt

class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My cool first GUI')                                    #Naming the window
        self.setGeometry(600, 250, 400, 400)                                        # Adjusting the window axis and size
        self.setWindowIcon(QIcon('Profile_image.jpg'))                              # Setting window icon

        # Label setting
        #label = QLabel('Hello', self)
        #label.setFont(QFont("Time's now", 40))
        #label.setGeometry(0, 0, 400, 100)
        #label.setStyleSheet("color: #4334eb;"
         #                   "background-color: #eb3446;"
          #                  "font-weight: bold;"
           #                 "font-style: italic;"
            #                "text-decoration: underline;")
        #label.setAlignment(Qt.AlignCenter)

        # Image setting
        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap("Profile_image.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)
        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height() - label.height()) // 2,
                          label.width(),
                          label.height())


class main():
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()