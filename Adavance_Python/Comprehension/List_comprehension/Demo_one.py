#  syntax 1 :[expression for variable in iterable]
#  example 1

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sq = []
sq_even =[]
for num in number_list:
    sq.append(num*num)
print(sq)
print("*******************8")
#  using list comprehension 
print([num * num for num in number_list])
print("&&&&&&&&&&&&&&&&")
# syntax 2 : if there is condition  [[expression for variable in iterable if cond]
# example2 : only even number square

for nums in number_list:
    if nums%2 ==0:
        sq_even.append(nums*nums)
print(sq_even)
print('****************')
# using list comprehension
print([nums*nums for nums in number_list if nums%2==0])