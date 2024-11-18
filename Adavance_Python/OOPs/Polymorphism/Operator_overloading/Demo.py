# step 1 --> check datatype of left operand
# Step 2 --> go in that class
# step 3 --> call __add__() function

num1 = 20
num2 = 30
print(num1+num2)
print(num1.__add__(num2))
print(int.__add__(num1, num2))
print("------------")
print(dir(int))

str1 = "hello"
str2 = "world"
print(str1+str2)
print(str1.__add__(str2))
print(str.__add__(str1, str2))
