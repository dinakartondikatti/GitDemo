#  how to achieve operator overloading

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __add__(self, other):
        total = self.pages +other.pages
        return  Book("total pages ", total)

    def __str__(self):
         return str(self.pages)


b1 = Book("Game of thrones ", 900)
b2 = Book("Harry potter ", 1500)
b3 = Book("Kannada kaligalu ", 5000)
b4 = Book("indian rupee and it's problesm " , 2600)

print("Total number of pages : ", b1+b2+b3+b4)
