#  syntax 3 : if there are nested if  present [expression for variable in iterable if cond if cond]
# example 3 : if given list is divisible by both 2 and 3 there square

nums = [3, 6, 9, 12, 15, 18]
sq = []
for num in nums:
    if num%2==0:
        if num%3==0:
            sq.append(num*num)
print(sq)
print("**************")
# using list comprehension
print([num*num for num in nums if num%2==0 if num%3==0])

#  syntax4: for if-else condition - [expression if cond else expression for variable in iterable ]
# example4 : in the given list if it is even number is there then square those number and for odd number qube it
print("Below output for expression four")
num_nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
results=[]
for num in num_nums:
    if num%2==0:
        results.append(num*num)
    else:
        results.append(num*num*num)

print(results)
# using list comprehension
print("this below output originated using list comprehension")
print([num*num if num%2==0 else num*num*num for num in num_nums ])
