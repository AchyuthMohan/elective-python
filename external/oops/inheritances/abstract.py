from abc import ABC
class Polygon(ABC):
    def no_of_side(self):
        pass
class Rectangle(Polygon):
    def __init__(self):
        self.sides=4
    def no_of_side(self):
        print(self.sides)
    
# r=Polygon() not possible
r=Rectangle()
r.no_of_side()
