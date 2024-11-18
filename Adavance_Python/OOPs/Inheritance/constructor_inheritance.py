
class Father:
    def __init__(self):
        self.vehicle ="scotter"
        print("the father class called")

class Son(Father):
    def __init__(self):
        print("the son class called ")
        self.vehicle = "BMW"

s = Son()
print(s.vehicle)
