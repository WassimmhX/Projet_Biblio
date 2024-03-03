from exec import MainWindow
from PyQt5 import QtWidgets
import sys


class Main:
    def __init__(self):
        self.window = MainWindow()


app = QtWidgets.QApplication(sys.argv)
window = Main()
app.exec_()
