

class Person:
    def __init__(self,name,age):
        self.name = name       #das was nach dem punkt steht ist erstmal leer und das ist wie wenn ich ein attribut erstelle
        self.age = age
        self.getname()
        print("Objekt:",self.name)  

    def getname(self):
        print("My Name is :", self.name) 
     

p1 = Person("Hans", 20)
p2 = Person("Peter", 30)


