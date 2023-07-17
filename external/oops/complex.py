class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def display(self):
        print("Real: ", self.r, "Imaginary: ", self.i)

    def __add__(self,others):
        rnet=self.r+others.r
        inet=self.i+others.i

        return Complex(rnet,inet)

c1=Complex(1,2)
c2=Complex(2,3)
c3=c1+c2
c3.display()