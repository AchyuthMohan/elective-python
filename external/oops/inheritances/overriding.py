class Shape:
    def display(self):
        print("Shape..")


class Rectangle(Shape):
    def display(self):
        print("Rectangle")


s = Shape()
r = Rectangle()

s.display()
r.display()
