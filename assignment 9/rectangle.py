class Rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def perimeter(self):
        print("Perimeter of rectangle: ",2*(self.height+self.width))
    def area(self):
        print("Area: ",self.height*self.width)

h=int(input("Enter the height: "))
w=int(input("Enter the width: "))

r=Rectangle(h,w)
r.area()
r.perimeter()

