class Calculation:
    def add(self,a,b,c=0):
        return a+b+c
    
c=Calculation()
print(c.add(1,2))
print(c.add(1,2,4))