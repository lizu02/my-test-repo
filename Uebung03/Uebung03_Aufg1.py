
class Figur: 
    def __init__(self,name):
        self.name = name
        

    def Umfang(self): 
        return 0 
    def __str__(self): 
        return self.name



class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"x:{self.x} y:{self.y}"


class Dreieck(Figur):
    def __init__(self, seitea, seiteb, seitec):
        super().__init__("Dreieck")
        self.seitea = seitea
        self.seiteb = seiteb
        self.seitec = seitec
    
    def Umfang(self): 
        return self.seitea + self.seiteb + self.seitec
    
    def __str__(self):
        return f"Dreieck mit Seitenlängen {self.seitea}, {self.seiteb} und {self.seitec}"


class Rechteck(Figur):
    def __init__(self, a, b):
        super().__init__("Rechteck")
        self.a = a
        self.b = b

    def Umfang(self):
        return 2 * (self.a + self.b)
    
    def __str__(self): 
        return f"Rechteck mit Seitenlängen {self.a} und {self.b}"
        


class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.mittelpunkt = mittelpunkt
        self.radius = radius

    def Umfang(self):
        return 2 * 3.14159 * self.radius
    
    def __str__(self): 
        return f"Kreis mit Radius {self.radius} und Mittelpunkt {self.mittelpunkt}"



class Polygon(Figur):
    def __init__(self, *punkte):
        super().__init__("Polygon")
        self.punkte = list(punkte)

    def __str__(self):
        return f"Polygon mit {len(self.punkte)} Punkten"




p1 = Punkt(0,0)
p2 = Punkt(10,15)
p3 = Punkt(20,0)
p4 = Punkt(15,10)

d = Dreieck(3,4,5)
r = Rechteck(3,4)
k = Kreis(p1, 5)
p = Polygon(p1,p2,p3,p4)   


