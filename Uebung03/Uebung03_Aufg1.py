
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
        return f"Dreieck mit Seitenlängen {self.seitea}, {self.seiteb} und {self.seitec} und Umfang {self.Umfang():.2f}" #:.2f gibt 2 Nachkommastellen an


class Rechteck(Figur):
    def __init__(self, a, b):
        super().__init__("Rechteck")
        self.a = a
        self.b = b

    def Umfang(self):
        return 2 * (self.a + self.b)
    
    def __str__(self): 
        return f"Rechteck mit Seitenlängen {self.a} und {self.b} und Umfang {self.Umfang():.2f}"
        


class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.mittelpunkt = mittelpunkt
        self.radius = radius

    def Umfang(self):
        return 2 * 3.14159 * self.radius
    
    def __str__(self): 
        return f"Kreis mit Radius {self.radius} und Mittelpunkt {self.mittelpunkt} und Umfang {self.Umfang():.2f}"



class Polygon(Figur):
    def __init__(self, *punkt):
        super().__init__("Polygon")
        self.punkte = list(punkt)

    def Umfang(self):
        umfang = 0
        for i in range(len(self.punkte) - 1):  
            dx = self.punkte[i + 1].x - self.punkte[i].x
            dy = self.punkte[i + 1].y - self.punkte[i].y
            umfang += (dx**2 + dy**2) ** 0.5  # Euklidische Distanz
        if len(self.punkte) > 2:  # Letzte Verbindung zurück zum Startpunkt
            dx = self.punkte[-1].x - self.punkte[0].x
            dy = self.punkte[-1].y - self.punkte[0].y
            umfang += (dx**2 + dy**2) ** 0.5
        return umfang
   
    def __str__(self):
        return f"Polygon mit {len(self.punkte)} Punkten und Umfang {self.Umfang():.2f}"




p1 = Punkt(0,0)
p2 = Punkt(10,15)
p3 = Punkt(20,0)
p4 = Punkt(15,10)

d = Dreieck(3,4,5)
r = Rechteck(3,4)
k = Kreis(p3, 5)
p = Polygon(p1,p2,p3,p4)   


print(d)
print(r)
print(k)
print(p)


