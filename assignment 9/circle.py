from math import pi
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return pi*self.radius*self.radius
    
c1=Circle(3)
c2=Circle(6)

if(c1.area()>c2.area()):
    print("c1 has more area than c2")
elif(c1.area()<c2.area()):
    print("c2 has more area than c1")
else:
    print("both has equal area..")


