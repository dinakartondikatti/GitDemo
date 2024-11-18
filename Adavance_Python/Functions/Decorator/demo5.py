#  first add two interger and return square of it using decorator

def square(add):
    def inner(*args):
        squa = add(*args)
        return squa*squa
    return inner
@square
def add(a, b):
    return a+b

print(add(2, 8))
