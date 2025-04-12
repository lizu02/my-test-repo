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
        layout = QGridLayout()                # QGridLayout() = Gitterlayout  QVBoxLayout() = vertikaler aufbau  QHBoxLayout() = horizontaler aufbau


        nameLabel = QLabel("Name:")
        nameLine = QLineEdit()
        adressLabel = QLabel("Adresse:")
        adressText = QTextEdit()              


        layout.addWidget(nameLabel, 0, 0)      # layout.addRow("Label:", Widget)  # Label und Widget in einer Zeile (an Position 0,0 positionieren)
        layout.addWidget(nameLine, 0, 1)       # layout.addRow("Label:", Widget)  # Label und Widget in einer Zeile (an Position 0,1 positionieren)
        layout.addWidget(adressLabel, 1, 0)    # layout.addRow("Label:", Widget)  # Label und Widget in einer Zeile (an Position 1,0 positionieren)
        layout.addWidget(adressText, 1, 1)     # layout.addRow("Label:", Widget)  # Label und Widget in einer Zeile (an Position 1,1 positionieren)

       
        

        


        


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