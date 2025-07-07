# Create Person class → then inherit Student and Teacher.

name = input("Enter the name: ")
grade = input("Enter the graede: ")

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
        def __init__(self, name, grade):
            super().__init__(name)
            self.grade = grade
        def display(self):
             print(f"{self.name} have grade {self.grade}")

s1 = Student(name, grade)
s1.display()
