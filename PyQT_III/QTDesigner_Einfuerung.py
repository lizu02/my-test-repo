
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("PyQT_III/QTDesigner_Einfuehrung.ui", self)

  
        self.show()




def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()