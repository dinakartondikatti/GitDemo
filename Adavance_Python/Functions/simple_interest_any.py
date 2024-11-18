#  write a program for simple interest

def simple_interest():
    print("WELCOME!")
    p = int(input("Enter the principle amount: "))
    n = int(input("Enter the number of years: "))
    i = int(input("Enter the rate of interest on  amount: "))
    si = (p * n * i) / 100
    print("the interest money si :", si)


simple_interest()
