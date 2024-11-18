# using one decorator on multiple function\
# apart from first any parameter is zero then execute this --> "cannot divisible by zero"

def decora(func):
    def inner(*args):
        for num in args[1:]:
            if num ==0:
                return "cannot divide by zero"
        return func(*args)
    return inner


@decora
def div(a, b):
    return a/b
@decora
def div2(a, b, c):
    return a/b/c

print(div(10,5))
print(div2(10,0, 5))
print(div(20, 0))
print(div2(10, 5 ,0))
print(div2(100, 10,5))


