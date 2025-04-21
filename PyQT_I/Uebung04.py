import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()


    def createLayout(self):
        
        self.setWindowTitle("GUI Programmierung")      ## Fenstertitel / Layout
    
        layout = QGridLayout()                         ### LAYOUT WÄHLEN:


        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")            # Menüleiste (oben) erstellen
        
        speichern = QAction("save", self)             # Aktion "save" erstellen für das menu
        verlassen = QAction("Quit", self)             # Aktion "quit" erstellen für das menu

        speichern.triggered.connect(self.menu_save)   #wenn es 'getriggert' wird, also ausgelöst wird, dann wird die Funktion menu_save aufgerufen
        verlassen.triggered.connect(self.menu_quit)   #wenn es 'getriggert' wird, also ausgelöst wird, dann wird die Funktion menu_quit aufgerufen

        filemenu.addAction(speichern)                 # Aktion "speichern" dem Menü "File" hinzufügen
        filemenu.addAction(verlassen)                 # Aktion "verlassen" dem Menü "File" hinzufügen


        button1 = QPushButton("Save")           # knopf ganz unten erstellen

        # alle abfragemasken bzw. felder zum ausfüllen erstellen. jeweils immer ein Label(='Titel') und ein Eingabefeld
        self.nameLabel1 = QLabel("Vorname:")
        self.nameLine1 = QLineEdit()
        self.nameLabel2 = QLabel("Nachname:")
        self.nameLine2 = QLineEdit()
        self.geburtsdatumLabel = QLabel("Geburtsdatum:")
        self.geburtsdatumLine = QLineEdit()
        self.adressLabel = QLabel("Adresse:")
        self.adressLine = QLineEdit() 
        self.postleitzahlLabel = QLabel("Postleitzahl:")
        self.postleitzahlLine = QLineEdit()
        self.ortLabel = QLabel("Ort:")
        self.ortLine = QLineEdit()
        self.landlabel = QLabel("Land:")
        self.landlabel2 = QComboBox()
        self.landlabel2.addItems(["Schweiz", "Deutschland", "Österreich"])    

        # Positionierung der einzelnen Widgets im Gesamtlayout
        layout.addWidget(self.nameLabel1, 0, 0)   
        layout.addWidget(self.nameLine1, 0, 1)     
        layout.addWidget(self.nameLabel2, 1, 0)
        layout.addWidget(self.nameLine2, 1, 1)
        layout.addWidget(self.geburtsdatumLabel, 2, 0)
        layout.addWidget(self.geburtsdatumLine, 2, 1)
        layout.addWidget(self.adressLabel, 3, 0)
        layout.addWidget(self.adressLine, 3, 1)
        layout.addWidget(self.postleitzahlLabel, 4, 0)
        layout.addWidget(self.postleitzahlLine, 4, 1)
        layout.addWidget(self.ortLabel, 5, 0)
        layout.addWidget(self.ortLine, 5, 1)
        layout.addWidget(self.landlabel, 6, 0)
        layout.addWidget(self.landlabel2, 6, 1)
        layout.addWidget(button1, 7, 1)
                    
        self.setMinimumSize(600,400)       # Mindestgröße des Fensters
        
        center = QWidget()                ## Zentrierung der Widgets
        center.setLayout(layout)
        self.setCentralWidget(center)     

        self.show()                         ## Fenster anzeigen

        button1.clicked.connect(self.menu_save)  # Wenn Button 1 geklickt wird, dann wird die Funktion menu_save aufgerufen (selbe soll auch bei speichern oben links passieren)


    def menu_save(self):                 # Funktion, die aufgerufen wird, wenn "save" geklickt wird
   
        name1 = self.nameLine1.text()
        name2 = self.nameLine2.text()
        geburtsdatum = self.geburtsdatumLine.text()
        adresse = self.adressLine.text()
        plz = self.postleitzahlLine.text()
        ort = self.ortLine.text()
        land = self.landlabel2.currentText()
   
        zeile = f"{name1},{name2},{geburtsdatum},{adresse},{plz},{ort},{land}\n"
   
        with open("output.txt", "w", encoding="utf-8") as datei:
            datei.write(zeile)
        print("Daten gespeichert")                          # Ausgabe in der Konsole

    def menu_quit(self):           
        self.close()                            # Fenster schließen 


def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()