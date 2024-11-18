#  what is decorator --> functions which takes other functions as input , add additional functionalities and return if
#   it is a callable python object which modifies other functions/ class

def decor(func):
    def inner():
        func()
        print("Welcome guru")
    return inner
@decor
def printers():
    print("welcome hello")
    print("welcome hello")

printers()
