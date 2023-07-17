from math import pi,pow

class Circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        return pi*pow(self.radius,2)
    def __ge__(self,others):
        return self.area()>=others.area()

class Circum(Circle):
    def circum(self):
        return 2*pi*self.radius
    
c1=Circle(2)
c2=Circle(3)
c3=Circum(4)
print(c1.area())
print(c2.area())
print("circumference: ",c3.circum())

if c1>=c2:
    print("c1 is greater..")
else:
    print("C2 is greater")
