# over-riding the magica functions

class Cart:
    def __str__(self):
        return "this is over riding  the magic function or in built function"

c1 = Cart()
print(c1)