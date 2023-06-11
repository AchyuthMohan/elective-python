class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2

    def __gt__(self, other):
        return self.area() > other.area()

C1 = Circle(5)
C2 = Circle(3)

if C1 > C2:
    print("Area of C1 is greater than C2")
else:
    print("Area of C2 is greater than or equal to C1")

