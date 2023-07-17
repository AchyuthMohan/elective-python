class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def get_info(self):         #accessor
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Marks: ", self.marks)

    def set_name(self):         #mutator
        name = input("Enter the new name: ")
        self.name = name


s = Student("Achyuth", 21, 100)
s.get_info()
s.set_name()
s.get_info()
