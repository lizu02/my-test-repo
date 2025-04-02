import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        

    




      
        




    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("GUI Programmierung")
        ### LAYOUT WÄHLEN:
        layout = QGridLayout()                


        button1 = QPushButton("Save")

        nameLabel1 = QLabel("Vorname:")
        nameLine1 = QLineEdit()
        nameLabel2 = QLabel("Nachname:")
        nameLine2 = QLineEdit()
        geburtsdatumLabel = QLabel("Geburtsdatum:")
        geburtsdatumLine = QLineEdit()
        adressLabel = QLabel("Adresse:")
        adressText = QTextEdit() 
        postleitzahlLabel = QLabel("Postleitzahl:")
        postleitzahlLine = QLineEdit()
        ortLabel = QLabel("Ort:")
        ortLine = QLineEdit()
        landLabel = QLabel("Land:")
        landLine = QLineEdit()




       

     
        layout.addWidget(nameLabel1, 0, 0)   
        layout.addWidget(nameLine1, 0, 1)     
        layout.addWidget(nameLabel2, 1, 0)
        layout.addWidget(nameLine2, 1, 1)
        layout.addWidget(geburtsdatumLabel, 2, 0)
        layout.addWidget(geburtsdatumLine, 2, 1)
        layout.addWidget(adressLabel, 3, 0)
        layout.addWidget(adressText, 3, 1)
        layout.addWidget(postleitzahlLabel, 4, 0)
        layout.addWidget(postleitzahlLine, 4, 1)
        layout.addWidget(ortLabel, 5, 0)
        layout.addWidget(ortLine, 5, 1)
        layout.addWidget(landLabel, 6, 0)
        layout.addWidget(landLine, 6, 1)
        layout.addWidget(button1, 7, 1)
             

       
        

        


        


        self.setMinimumSize(1200,400)
        

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







    def button1Clicked(self):  # Funktion die aufgerufen wird, wenn Button 1 geklickt wird
        print("Button 1 wurde geklickt")  # Ausgabe in der Konsole

 

   




def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()