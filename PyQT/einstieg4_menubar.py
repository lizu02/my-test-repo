import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()

        menubar = self.menuBar()  # Menüleiste erstellen
        filemenu = menubar.addMenu("Datei")  # Dem Menü den Punkt "Datei" hinzufügen
        editmenu = menubar.addMenu("Bearbeiten")  # Dem Menü den Punkt "Bearbeiten" hinzufügen -- edit wegen bearbeiten
        viewmenu = menubar.addMenu("Ansicht") # Dem Menü den Punkt "Ansicht" hinzufügen -- view wegen ansicht


        open = QAction("Öffnen", self)          # Aktion "Öffnen" erstellen
        open.triggered.connect(self.menu_open)  #wenn es getriggert wird, also ausgelöst wird, dann wird die Funktion menu_open aufgerufen
        save = QAction("Speichern", self)       # Aktion "Speichern" erstellen
        save.triggered.connect(self.menu_save)  #wenn es getriggert wird, also ausgelöst wird, dann wird die Funktion menu_save aufgerufen
        quit = QAction("Beenden", self)         # Aktion "Beenden" erstellen
        quit.triggered.connect(self.menu_quit)  #wenn es getriggert wird, also ausgelöst wird, dann wird die Funktion menu_quit aufgerufen

        #quit.setMenuRole(QAction.QuitRole) # Damit das wieder richtig schliesst (nur für MACOS wichtig)


        filemenu.addAction(open)  # Aktion "Öffnen" dem Menü "Datei" hinzufügen
        filemenu.addAction(save)  # Aktion "Speichern" dem Menü "Datei" hinzufügen  
        filemenu.addAction(quit)  # Aktion "Beenden" dem Menü "Datei" hinzufügen

    
    def menu_open(self):  # Funktion die aufgerufen wird, wenn "Öffnen" geklickt wird
        pass            # es tut einfach nichts


    def menu_save(self):  # Funktion die aufgerufen wird, wenn "Speichern" geklickt wird
        pass            # es tut einfach nichts


    def menu_quit(self):  # Funktion die aufgerufen wird, wenn "Beenden" geklickt wird
        print ("Beenden wurde geklickt")  # Ausgabe in der Konsole
        self.close()     # Fenster schliessen


        


      
        




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