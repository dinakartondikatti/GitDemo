
class Employe:

    def __init__(self, salary, age):
        self.salary = salary
        self.age = age

    def dispaly(self):
        print(f"salary is {self.salary}and age is {self.age}")

emp1 = Employe(20000,24)
print(emp1.salary)
emp2 = Employe(34000, 55)
emp2.dispaly()