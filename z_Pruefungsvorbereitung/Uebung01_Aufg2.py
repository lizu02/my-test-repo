


class WGS84Coord:

    def __init__(self, _longitude=0, _latitude=0):
        self.set_longitude(_longitude)
        self.set_latitude(_latitude)

    
    def set_longitude(self,wert):
        if wert <-180:
            print("Ungültiger Longitude-Wert! (muss grösser als -180 sein) > wird auf 0 korrigiert!")
            self._longitude = 0
        elif wert >180:
            print("Ungültiger Longitude-Wert! (muss kleiner als 180 sein) > wird auf 0 korrigiert!")
            self._longitude = 0
        else:
            self._longitude = wert

    def get_longitude(self):
        return self._longitude 



    def set_latitude(self,wert):
        if wert < -90:
            print ("Ungültiger Latitude-Wert! (muss grösser als -90 sein) > wird auf 0 korrigiert!")
            self._latitude = 0
        elif wert >90:
            print("ngültiger Longitude-Wert! (muss kleiner als 90 sein) > wird auf 0 korrigiert!")
            self._latitude = 0
        else:
            self._latitude = wert

    def get_latitude(self):
        return self._latitude


Koordinaten = WGS84Coord(77,88)
print ("Longitude:" , Koordinaten.get_longitude())
print ("Latitude: " , Koordinaten.get_latitude())




''' Mit Property anstelle setter und Getter-Methoden (set und get wird "versteckt" und das handling funktioniert wie bei einem
normalen attribut, jedoch wird die prüfungsfunktion im hintergrund trotzdem ausgeführt!)'''



class WGS84Coord:

    def __init__(self, longitude=0, latitude=0):
        self.longitude = longitude  # → ruft setter auf!
        self.latitude = latitude    # → ruft setter auf!

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, wert):
        if wert < -180:
            print("Ungültiger Longitude-Wert! (muss grösser als -180 sein) > wird auf 0 korrigiert!")
            self._longitude = 0
        elif wert > 180:
            print("Ungültiger Longitude-Wert! (muss kleiner als 180 sein) > wird auf 0 korrigiert!")
            self._longitude = 0
        else:
            self._longitude = wert

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, wert):
        if wert < -90:
            print("Ungültiger Latitude-Wert! (muss grösser als -90 sein) > wird auf 0 korrigiert!")
            self._latitude = 0
        elif wert > 90:
            print("Ungültiger Latitude-Wert! (muss kleiner als 90 sein) > wird auf 0 korrigiert!")
            self._latitude = 0
        else:
            self._latitude = wert


k = WGS84Coord(180, 90) 
print("Longitude:", k.longitude)
print("Latitude:", k.latitude)



