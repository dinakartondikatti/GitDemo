# fubonacci series using recursion
# example fibo(10) --> 0 , 1 , 1, 2, 3, 5,8,13,21,34
def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo(n-2)+fibo(n-1)

n = int(input("Enter the terms : "))
for i in range(1, n+1):
    print(fibo(i))