#  write function program for addition and subtraction with rerun it include globle variable and local variable

a = 500  # global varible
b = 200
def maths_subject():
    # a = 100
    # b = 50  # first preference is always local variable when variable declare inside th function
    add = a + b  # local variable
    sub = a - b
    return add, sub


result1, result2 = maths_subject() # second preference is arguments for function if local variable are not declared
print("addition of a + b :", result1)
print("subtraction of a - b :", result2)
print(a)
