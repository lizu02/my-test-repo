
import math

class Vector3:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


    def __str__(self):
        return "Vektor: ("+str(self.x)+","+str(self.y)+","+str(self.z)+")"


    def __add__(self, other):
        return Vector3(self.x+other.x, self.y+other.y, + self.z+other.z)

    def __sub__(self,other):
        return Vector3(self.x-other.x, slef.y-other.y, self.z-other.z)





v1 = Vector3(1,2,3)
v2 = Vector3(1,2,3)
print(v1)
print(v2)

