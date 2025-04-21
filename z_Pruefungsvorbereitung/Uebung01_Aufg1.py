
import math

class Vector3:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    
    def len(self):
        laenge = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        print(f"Der Vektor hat eine Länge von: {round(laenge,4)}.")
         
        

vektor = Vector3(3,3,3)
vektor.len()
