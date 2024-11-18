#  creating class for two employees for their details

class Emp:

    def __init__(self):
        self.salary = 20000
        self.age = 26

e1 = Emp()
e2 = Emp()
print(f" e1 has same as salary {e1.salary} e2 {e2.salary} ")
print(e1.__dict__)
