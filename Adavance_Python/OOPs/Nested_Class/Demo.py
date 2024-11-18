#  nested class

class Outer:

    def __init__(self):
        print("Outer class constructor called ")

    def display(self):
        print("This is display method ")

    class Inner:

        def __init__(self):
            print("Inner class constructor called")

        def show(self):
            print("This is show method")


obj1 = Outer()

inj1 = obj1.Inner()

inj1.show()