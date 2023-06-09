class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError(
                "Unsupported operand type for +: 'Point' and '{}'".format(type(other)))

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        else:
            raise TypeError(
                "Unsupported operand type for -: 'Point' and '{}'".format(type(other)))

    def __lt__(self, other):
        if isinstance(other, Point):
            return self.x < other.x and self.y < other.y
        else:
            raise TypeError(
                "Unsupported operand type for <: 'Point' and '{}'".format(type(other)))
        
p1 = Point(2, 3)
p2 = Point(4, 5)
print(p1)
print(p2)
p3=p1+p2
print(p3)
p4=p1-p2
print(p4)
print(p1<p2)
