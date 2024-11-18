class Student :

    def __init__(self, name , roll,dd, mm, yy):
        self.name = name
        self.roll =roll
        self.obj = self.DOB(dd,mm,yy)

    def display(self):
        print(f"Name is {self.name} and roll number is {self.roll}")
        self.obj.display()

    class DOB:

        def __init__(self, dd, mm, yy):
            self.dd = dd
            self.mm = mm
            self.yy = yy

        def display(self):

            print(f"Date of birth is : {self.dd}/{self.mm}/{self.yy}")

S1 = Student("Dinu", "1VE15ME018", 21, 6, 1997)
S1.display()