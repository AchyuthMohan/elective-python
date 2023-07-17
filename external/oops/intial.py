from math import pi, pow


class Cirlce:
    def __init__(self, radius):
        self.radius = radius

    def display_area(self):
        return pi*pow(self.radius, 2)


class Student:
    def __init__(self, age=21):
        self.age = age

    def get_name(self):
        name = input("Enter the name: ")
        self.name = name

    def display_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)


r = int(input("Enter the radius: "))
c = Cirlce(r)
print(c.display_area())
age = int(input("Enter the age: "))
s = Student(age)
s.get_name()
s.display_details()
