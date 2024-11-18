#  partial functions allow us to fix a certain number of arguments of a function and generate a new function
#  partial function present in functools -->higher order function
# syntax --> partial(function , arg1, arg2, ....argn)
from functools import partial
def add(n1,n2,n3,n4):
    return n1+n2+n3+n4

add = partial(add, 2,4)

print(add(10,20))


