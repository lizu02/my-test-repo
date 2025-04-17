

import sys
import csv
import urllib.parse
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()



    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("Main Window")
        ### LAYOUT WÄHLEN:
        layout = QGridLayout()


        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")  # Menüleiste (oben) erstellen
        viewmenu = menubar.addMenu("View")
        ladenmenu = menubar.addMenu("Laden")
        
        speichern = QAction("save", self)          # Aktion "save" erstellen für das menu
        verlassen = QAction("Quit", self)       # Aktion "quit" erstellen für das menu
        Karte_anzeigen = QAction("Karte", self)
        Laden = QAction("Laden", self)

        speichern.triggered.connect(self.menu_save)  #wenn es 'getriggert' wird, also ausgelöst wird, dann wird die Funktion menu_save aufgerufen
        verlassen.triggered.connect(self.menu_quit)  #wenn es 'getriggert' wird, also ausgelöst wird, dann wird die Funktion menu_quit aufgerufen
        Karte_anzeigen.triggered.connect(self.menu_Karte_anzeigen)
        Laden.triggered.connect(self.menu_laden)

        filemenu.addAction(speichern)  # Aktion "speichern" dem Menü "File" hinzufügen
        filemenu.addAction(verlassen)  # Aktion "verlassen" dem Menü "File" hinzufügen
        viewmenu.addAction(Karte_anzeigen)
        ladenmenu.addAction(Laden)




        button3 = QPushButton("Save")           # knopf ganz unten erstellen
        button1 = QPushButton("Auf Karte anzeigen")
        button2 = QPushButton("Laden")

        # alle abfragemasken bzw. felder zum ausfüllen erstellen. jeweils immer ein Label(='Titel') und ein Eingabefeld
        self.nameLabel1 = QLabel("Vorname:")
        self.nameLine1 = QLineEdit()
        self.nameLabel2 = QLabel("Nachname:")
        self.nameLine2 = QLineEdit()
        self.geburtsdatumLabel = QLabel("Geburtsdatum:")       
        self.geburtsdatumLine = QDateEdit()                 #QDateEdit für Formatiertes Datum
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
        layout.addWidget(self.geburtsdatumLabel, 2, 0)              #AddWidget für z.B. Gitterlayout
        layout.addWidget(self.geburtsdatumLine, 2, 1)               #AddRow für normales QFormLayout (führt unterhalb neues Objekt ein)
        layout.addWidget(self.adressLabel, 3, 0)
        layout.addWidget(self.adressLine, 3, 1)
        layout.addWidget(self.postleitzahlLabel, 4, 0)
        layout.addWidget(self.postleitzahlLine, 4, 1)
        layout.addWidget(self.ortLabel, 5, 0)
        layout.addWidget(self.ortLine, 5, 1)
        layout.addWidget(self.landlabel, 6, 0)
        layout.addWidget(self.landlabel2, 6, 1)
        layout.addWidget(button1, 7, 1)
        layout.addWidget(button2, 8, 1)
        layout.addWidget(button3, 9, 1)
                    


        self.setMinimumSize(600,400)       # Mindestgröße des Fensters
        

        ## Zentrierung der Widgets
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        
      

        ## Fenster anzeigen
        self.show()


        button1.clicked.connect(self.menu_Karte_anzeigen)
        button2.clicked.connect(self.menu_laden)
        button3.clicked.connect(self.menu_save)  
        




    def menu_save(self):  # Funktion, die aufgerufen wird, wenn "save" geklickt wird
   
        name1 = self.nameLine1.text()
        name2 = self.nameLine2.text()
        geburtsdatum = self.geburtsdatumLine.text()
        adresse = self.adressLine.text()
        plz = self.postleitzahlLine.text()
        ort = self.ortLine.text()
        land = self.landlabel2.currentText()

    
        zeile = f"{name1},{name2},{geburtsdatum},{adresse},{plz},{ort},{land}\n"

        dateipfad, _ = QFileDialog.getSaveFileName(self, "Datei speichern", "","Textdateien (*.txt)")

        if dateipfad:
            with open(dateipfad, "w", encoding="utf-8") as datei:
                datei.write(zeile)

            print("Daten gespeichert in:", dateipfad)  # Ausgabe in der Konsole


    
    def menu_Karte_anzeigen(self):
        adresse = self.adressLine.text()
        PLZ = self.postleitzahlLine.text()
        ort = self.ortLine.text()
        Land = self.landlabel2.currentText()

        ganze_Adresse = f"{adresse},{PLZ},{ort},{Land}"
        adresse_als_code = urllib.parse.quote(ganze_Adresse)

        link = f"https://www.google.com/maps/search/{adresse_als_code}"
        Karte = QDesktopServices.openUrl(QUrl(link)) 


    def menu_laden(self):
        
        dateipfad, _ = QFileDialog.getOpenFileName(self, "Datei laden", "","Textdateien (*.txt)")

        if dateipfad:
            with open(dateipfad, "r", encoding="utf-8") as datei:
                inhalt1 = datei.readline()
                print ("zeile gelesen;", inhalt1)
                
                inhalt = inhalt1.strip().split(",")

                if len(inhalt) == 7:
                    self.nameLine1.setText(inhalt[0])
                    self.nameLine2.setText(inhalt[1])

                    dformat = QLocale().dateFormat(QLocale.FormatType.ShortFormat)
                    self.geburtsdatumLine.setDate(QDate.fromString(inhalt[2], dformat))

                    self.adressLine.setText(inhalt[3])
                    self.postleitzahlLine.setText(inhalt[4])
                    self.ortLine.setText(inhalt[5])
                    self.landlabel2.setCurrentText(inhalt[6])


            print("Daten geladen:", dateipfad)  # Ausgabe in der Konsole




    def menu_quit(self):
            
        self.close()  # Fenster schließen 


   




def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()