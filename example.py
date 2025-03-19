
class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self._x = x
        self._y = y
        self._z = z   
    
    def setX(self, x):
        self._x = x
    
    def getX(self):
        return self._x
    
    def setY(self, y):
        self._y = y
    
    def getY(self):
        return self._y
    
    def setZ(self, z):
        self._z = z
    
    def getZ(self):
        return self._z
    
    
    def __str__(self):
        return f"x:{self.x} y:{self.y} z:{self.z}"
    
    def __add__(self, addVector):
        return Vector3(self.x + addVector.x, self.y + addVector.y, self.z + addVector.z)
    
    def __mul__(self, multiplicator):
        return Vector3(self.x * multiplicator, self.y * multiplicator, self.z * multiplicator)
    
    def __iadd__(self, addVector):
        return self.__add__(addVector)
    
    def addition(self, addVector):
        return self.__add__(addVector)
    
    def __invert__(self):
        return self * -1
    
    x = property(getX, setX)
    y = property(getY, setY)
    z = property(getZ, setZ)
    
    
v0 = Vector3(1, 2, 1)
v1 = Vector3(2,0,0)

# __add__
v3 = v0 + v1

# addition
v3_1 = v0.addition(v1)

# __iadd__
v3_2 = v0
v3_2 += v1

v4 = v0 * v1
print(v4)


class Plane:
    def __init__(self, v0, normal):
        self._v0 = v0
        self._normal = normal
    
    def setV0(self, v0):
        self._v0 = v0
        
    def getV0(self):
        return self._v0
    
    def setNormal(self, normal):
        self._normal = normal
        
    def getNormal(self):
        return self._normal
    
    
    v0 = property(getV0, setV0)
    normal = property(getNormal, setNormal)
    
v0 = Vector3(1,0,0)
norm = Vector3(1,1,0)
    
p0 = Plane(v0, norm)
