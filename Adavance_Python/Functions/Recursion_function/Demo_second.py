#  factorial of n numbers
'''def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)
factorial= fact(int(input("Enter the number for factorial :")))
print(f"the factorial of the given numebr is : {factorial}")'''

# finding the prime number

def prime(n , i):
    if i == 1:
        return 1
    if n%i==0:
        return 0
    return prime(n, i-1)
n = int(input("Enter the number to find it prime or not : "))
prime_num = prime(n, n-1)
if prime_num ==1:
    print(f"The given value {n} is prime number ")
if prime_num ==0:
    print(f"The given value {n} is not prime number ")