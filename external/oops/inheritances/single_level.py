class Father:
    def __init__(self, fname):
        self.fname = fname

    def father(self):
        print(self.fname)


class Mother:
    def __init__(self, mname):
        self.mname = mname

    def mother(self):
        print(self.mname)


class Student(Mother, Father):  # multiple
    def __init__(self, name, fname, mname):
        self.name = name
        self.fname = fname
        self.mname = mname

    def display(self):
        print("Name: ", self.name)
        if self.fname is not None:
            print("Father name: ", self.fname)
        if self.mname is not None:
            print("Mother name: ", self.mname)


class Person(Mother):           #single level
    def __init__(self, mname):
        self.mname = mname

    def display(self):
        print(self.mname)

class Son(Student):                 #multilevel
    def __init__(self,name,sonname):
        self.sonname=sonname
        self.name=name
    def __str__(self):
        return f"son name: {self.name} son name: {self.sonname}"

s = Student("Achyuth", "Mohan", "Kavitha")
s.display()
