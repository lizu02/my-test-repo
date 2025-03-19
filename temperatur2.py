class Temperatur2:
    def __init__(self, t):
        self.temp = t

    def __str__(self):
        return f"{self.temp} C"
    
    def __int__(self):
        return int(self.temp)
    
    def __float__(self):
        return float(self.temp)
    
    def __gt__(self, other):
        return self.temp > other.temp
    
    def __lt__(self, other):
        return self.temp < other.temp
    
    def __eq__(self, other):
        return self.temp == other.temp
    
    def __ne__(self, other):
        return self.temp != other.temp

    

t = Temperatur2(7.5)
print(int(t))
print(float(t))

t_heute = Temperatur2(7)
t_gestern = Temperatur2(6)

if t_heute < t_gestern:
    print("heute ist es kälter als gestern")
elif t_heute > t_gestern:
    print("heute ist es wärmer als gestern")
else:
    print("heute ist es gleich warm wie gestern")

if t_heute != t_gestern:
    print("gestern und heute ist es unterschiedlich warm")