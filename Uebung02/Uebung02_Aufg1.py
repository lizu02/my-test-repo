
import math

class vektor3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z   
    
    

def __str__(self):
    return f"x:{self.x} y:{self.y} z:{self.z}"


def __add__(self, other):
        if type(other) == int or type(other) == float:
            return vektor3(self.x + other, self.y + other, self.z + other)
        else:
            return vektor3(self.x + other, self.y + other, self.z + other)
 

def __sub__(self, other):
    return vektor3(self.x - other.x, self.y - other.y, self.z - other.z)



def __mul__(self, other):
    return vektor3(self.x*other.x, self.y*other.y, self.z*other.z)




def dot(self, other):
    return (self.x * other.x + self.y * other.y + self.z * other.z) 
    
def cross(self, other):
    return vektor3(
        self.y * other.z - self.z * other.y,
        self.z * other.x - self.x * other.z,
        self.x * other.y - self.y * other.x
    )
    
def normalize(self):
    betrag = math.sqrt(self.x**2 + self.y**2 + self.z**2)
    if betrag == 0:
        return vektor3(0, 0, 0) # Verhindert Division durch Null
    return vektor3(self.x / betrag, self.y / betrag, self.z / betrag)





v1 = vektor3(3,4,2)
v2 = vektor3(2,1,0)


v3 = v1+v2
print("Addition:",v3)

v4 = v1-v2
print("Subtraktion:",v4)

v5 = v1*v2
print("Multiplikation:",v5)

v6 = dot(v1,v2)
print("Skalarprodukt:", v6)

v7 = cross(v1,v2)
print("Kreuzprodukt:", v7)

v8 = normalize(v1)
print("Normalisierter Vektor:", v8)









