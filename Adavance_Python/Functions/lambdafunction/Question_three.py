# using list comprehension in lambda

nums =[1, 2, 3, 4, 5, 6]
# for i in nums:
#     square =i*i
square = lambda data:[i*i*i for i in nums]
print(square(nums))