#  lambda function

add = lambda x, y: x + y
add_one=add(25,79)
print(add_one)

#  we cannot do multiple expression in lambda, but we can use tuple to make one expression for example see below

var_one=lambda a,b :(a+b,a-b)
add,sub=(var_one(10 , 20))
print(add)
print(sub)

"""
Example of lambda functions.
-incrementing numebr :- lambda n = n+1
-finding power of numebr :- lambda n:n**2
-convert string to Uppercase :- lambda str1:str1.upper()
- celcius to fahrenheit :- lambda c : c*9/5+32
"""
