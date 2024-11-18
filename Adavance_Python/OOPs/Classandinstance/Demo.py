# instance variable & method and class variable and method

class Student:

    college_name = "GES"  # class variable
    def __init__(self, nm , m):
        self.name = nm  # instance variable
        self.marks = m

    def display(self):  # instance method
        print(self.name , self.marks)
    @classmethod
    def get_college_name(cls):
        cls.college_name = "UVCE"
        print("Colloge name is ", cls.college_name)
    @staticmethod
    def details(stad,section):
        Student.college_name ="golbal infocity"
        print(f"the student is {stad} and {section} Section and studying in this {Student.college_name} college ")

std1 =Student("Ashu",90)
print(std1.__dict__)
print(std1.name)
print(std1.marks)
std1.display()
print(Student.college_name)
Student.college_name= "SVCE"
print(Student.college_name)
Student.get_college_name()

stad=int(input("Enter the standard of this guy:" ))
section = input("enter the section : ")

Student.details(stad,section)
