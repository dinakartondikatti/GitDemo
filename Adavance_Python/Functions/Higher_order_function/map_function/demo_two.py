#  using map function find the square of the given numbers
num = [1, 2, 4, 5, 6, 7, 9, 8]
# def square(n):
#     return n**2
# mapped_obj1=map(lambda n:n**2,num)
def square(n):
    if n%2!=0:
        return n**2
    else:
        False
mapped_obj1 = map(square, num)
print(list(mapped_obj1))

# print only odd number square
