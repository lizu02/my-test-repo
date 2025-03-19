

import math

class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def len(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

# Testen ob funktioniert
Vektor = Vector3(10, 10, 10)
print("Vektorlänge:", Vektor.len())



