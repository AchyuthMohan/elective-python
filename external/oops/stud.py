class Student:
    def __init__(self, name, rollno):
        self.rollno = rollno
        self.name = name
        self.age=None
        self.marks=None

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.rollno)
        if self.age is not None:
            print("Age: ", self.age)
        if self.marks is not None:
            print("Marks: ", self.marks)

    def setAge(self):
        age = int(input("Enter the age: "))
        self.age = age

    def setTestMarks(self):
        marks = float(input("Enter the test marks: "))
        self.marks = marks


name = input("Enter the name: ")
rollno = int(input("Enter the rollno: "))
s = Student(name, rollno)
s.display()
s.setAge()
s.setTestMarks()
s.display()
