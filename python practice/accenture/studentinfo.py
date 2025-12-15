class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, regno, percentage):
        super().__init__(name, age)
        self.regno = regno
        self.percentage = percentage

    def display(self):
        print("Name:" + self.name)
        print("Age:" + str(self.age))
        print("Rollno:" + str(self.regno))
        print("Percentage:" + str(self.percentage))

name = input("Enter the student name:\n")
age = int(input("Enter the student age:\n"))
regno = int(input("Enter the student rollno:\n"))
percentage = float(input("Enter the student percentage:\n"))

student_obj = Student(name, age, regno, percentage)
student_obj.display()
