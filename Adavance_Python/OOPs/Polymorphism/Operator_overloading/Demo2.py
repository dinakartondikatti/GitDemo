# overloading comparison operator

class Hotel:

    def __init__(self, name , fare):
        self.name = name
        self.fare  = fare

    def __gt__(self, other):
        return self.fare > other.fare

h1 = Hotel("taja Hotel ", 20000)
h2 = Hotel("Udupi hotel " , 2000000)

print(h1>h2)