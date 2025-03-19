
class WGS84Coord:
    def __init__(self, longitude=0, latitude=0):
        self.set_longitude(longitude)
        self.set_latitude(latitude)

    def set_longitude(self,wert):
        if wert < -180:
            print("Ungültiger Wert")
            self.longitude = 0
        elif wert > 180:
            print("Ungültiger Wert")
            self.longitude = 0
        else:
           self._longitude = wert
    

    def get_longitude(self):
        return self._longitude
    
    def set_latitude(self, wert):
        if wert < -90:
            print("Ungültiger Wert")
            self.latitude = 0
        elif wert > 90:
            print("Ungültiger Wert")
            self.latitude = 0
        else:
            self._latitude = wert

    def get_latitude(self):
        return self._latitude
    

Koord = WGS84Coord(200,30)
print("Longitude:", Koord.get_longitude())
print("Latitude:", Koord.get_latitude())
