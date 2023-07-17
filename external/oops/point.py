class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __add__(self, others):
        xnet = self.x+others.x
        ynet = self.y+others.y
        return Point(xnet, ynet)

    def __sub__(self, others):
        xnet = self.x-others.x
        ynet = self.y-others.y
        return Point(xnet, ynet)

    def __lt__(self, others):
        return self.x < others.x and self.y < others.y


p1 = Point(1, 2)
p2 = Point(2, 3)

p3 = p1-p2
print(p3)
if p1 < p2:
    print("p1 is less")
else:
    print("p2 is less")
