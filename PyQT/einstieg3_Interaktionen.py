import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        

    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("Mein erstes GUI")
        ### LAYOUT WÄHLEN:
        layout = QVBoxLayout()                


        button1 = QPushButton("Button 1")     # Buttons erstellen  -- was brauche ich: siehe link auf Moodle (doc.qt.io)
        button2 = QPushButton("Button 2")

        layout.addWidget(button1)      #Buttons dem Layout hinzufügen
        layout.addWidget(button2)       

       
        

        


        


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


        button1.clicked.connect(self.button1Clicked)  # Wenn Button 1 geklickt wird, dann wird die Funktion button1Clicked aufgerufen
        button2.clicked.connect(self.button2Clicked)  # Wenn Button 2 geklickt wird, dann wird die Funktion button2Clicked aufgerufen







    def button1Clicked(self):  # Funktion die aufgerufen wird, wenn Button 1 geklickt wird
        print("Button 1 wurde geklickt")  # Ausgabe in der Konsole

    def button2Clicked(self):  # Funktion die aufgerufen wird, wenn Button 2 geklickt wird
        print("Button 2 wurde geklickt")  # Ausgabe in der Konsole

   




def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()