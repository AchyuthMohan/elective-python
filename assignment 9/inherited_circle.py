import math
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return self.area*self.area

class Circle1(Circle):
    def circum(self):
        return 2*math.pi*self.radius
    
c=Circle1(23)
print("Area of circle: ",c.area())
print("Circumfference of circle: ",c.circum())


