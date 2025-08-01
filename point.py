class Point:
    x: int
    y: int
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    


p1 = Point(1, 2)
p2 = Point(2, 1)

print(p1, p2)

print(p1 == p2)

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p1 = Point(3, 2)
p2 = Point(2, 4)

print(p1, p2)

print(p1 == p2)