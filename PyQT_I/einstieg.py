import sys
from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createConnects()

    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("Mein erstes GUI")
        ### LAYOUT WÄHLEN:
        layout = QFormLayout()                # QVBoxLayout() = vertikaler aufbau  QHBoxLayout() = horizontaler aufbau


        nameLineEdit = QLineEdit()
        nameLindeEdit = QLineEdit()
        ageSpinBox = QSpinBox()

        layout.addRow("Name:", nameLineEdit)      # layout.addRow("Label:", Widget)  # Label und Widget in einer Zeile
        layout.addRow("Email:", nameLindeEdit)
        layout.addRow("Alter:", ageSpinBox)
        

        


        


        self.setMinimumSize(1200,400)
        # self.setMinimumHeight(400)    Minimale Höhe     
        # self.setMinimumWidth(1200)    minimale Breite

        ## Zentrierung der Widgets
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        
        ## Widgets erstellen
        # ...

        ## Layout füllen
        # ...

        ## Fenster anzeigen
        self.show()


    def createConnects(self):
        pass




def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()