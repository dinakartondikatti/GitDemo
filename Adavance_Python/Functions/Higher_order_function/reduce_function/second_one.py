# find the max number in the given list
import functools
nums = [23, 56, 7, 89, 100, 405, 250, 78]
def max1(a , b):
    if a > b:
        return a
    else:
        return b
print(functools.reduce(max1,nums))

