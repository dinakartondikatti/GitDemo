# comparision between is operator and == operator

a = 100
b = 100

print(a == b)  # here value is compared
print(a is b)  # here id(a) and id(b) is compared

# Example1
print("********************")

data = [10, 20, 30, 40]
data1 = [10, 20, 30, 40]
print(data == data1)
print(data is data1)
# why is giving flase because both list id is different
# but inside value id  is same how check
print("*****************")
print("""then let find the why id's of 
list is different and values is same
because all values stored memories  
data1 is reference the memory""")

print("id of data :", id(data))
print("id of data1 :", id(data1))
print("id of data[1] :", id(data[1]))
print("id of data1[1] :", id(data[1]))