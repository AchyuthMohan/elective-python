class Student:
    def __init__(self,rollno,name):
        self.name=name
        self.rollno=rollno
    
    def display(self):
        print("Name: ",self.name)
        print("Roll No: ",self.rollno)

    def setAge(self):
        age=int(input("Enter the age of student: "))
        self.age=age

    def setMarks(self):
        mark=float(input("Enter the test marks: "))
        self.mark=mark
    
s=Student(3,"Achyuth Mohan")
s.display()
s.setAge()
s.setMarks()

