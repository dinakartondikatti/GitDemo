# a function calls another function which then calls the first function again

def num(n):
    if n<=0:
        return
    print(n, end=" ")
    num1(n-1)
def num1(n):
    print(n,end= " ")
    num(n-1)
print(num1(10))
