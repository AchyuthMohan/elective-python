from math import pi


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return pi*self.r*self.r

    def __gt__(self, others):
        if self.r > others.r:
            return True


c1 = Circle(3)
c2 = Circle(5)
if c1 > c2:
    print("c1 is greater")
else:
    print("c2 is greater")
