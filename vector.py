class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __len__(self):
        return 2
    
    def len(self):
        return (self.x**2 + self.y**2)**0.5
    
    def __abs__(self):
        return Vector2(abs(self.x), abs(self.y))
    
    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return Vector2(self.x + other, self.y + other)
        else:
            return Vector2(self.x + other.x, self.y + other.y)
        
    def __radd__(self, other):
        return Vector2(self.x + other, self.y + other)
    
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    
# -----------

v1 = Vector2(3,4)
v2 = Vector2(4,5)

#v3 = abs(v2)

v3 = v1 + v2 
print(v3)

v4 = v1 + v2 + v3
print(v4)

print(abs(v1-v2))

v5 = Vector2(7,8)

v6 = v5 + 1
print(v6)

v6 = 1 + v5
print(v6)