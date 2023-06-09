from abc import ABC, abstractmethod
from math import pi
class Shape:
    @abstractmethod
    def area(self):
        pass
    def circumference(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return self.radius*self.radius
    
    def circumference(self):
        return 2*pi*self.radius
    
class Recatngle(Shape):
    def __init__(self,l,b):
        self.length=l
        self.breadth=b

    def area(self):
        return self.length*self.breadth
    
    def circumference(self):
        return 2*(self.length+self.breadth)
    
r=Recatngle(1,2)
c=Circle(3)

print("Area of circle: ",c.area())
print("Area of rectangle: ",r.area())
print("Circumference of circle: ",c.circumference())
print("Circumference of rectangle: ",r.circumference())