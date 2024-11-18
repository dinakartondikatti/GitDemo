# Nested lambda function  syntax lambda x:lambda y:x+y
add = lambda x: lambda y: x + y
var_add=add(10)
print(var_add(90))
print("*******************")
square = lambda n:n**2

modify=lambda func:lambda num:func(num)+num
print(modify(square)(int(input("Enter your number : "))))
# power_number = modify(square)
# print(power_number(int(input("Enter your number : "))))
