class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print(self.fname," ",self.lname)

class Student(Person):
    def __init__(self,fname,lname,gyear=None):
        self.fname=fname
        self.lname=lname
        self.gyear=gyear
    
    def display(self):
        print(self.fname,self.lname)
        if self.gyear is not None:
            print("G year: ",self.gyear)

s=Student("achyuth","mohan",2024)
s.display()
