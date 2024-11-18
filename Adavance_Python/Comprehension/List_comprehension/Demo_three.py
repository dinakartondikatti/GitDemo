#  syntax 5 : if there are nested for loop present  - [expression if cond else expression for var in iterable]

#  example 5:

lst = []
for i in range (3, 6):
    for j in range (5 , 7):
        lst.append(i*j)

print(lst)
print("using list comprehension ")
print([i*j for i in range (3, 6) for j in range (5 , 7)])

# for if-elif-else using chain code .

checkup_fee =[]
ages = [16, 17 , 18, 25, 67, 13, 0, 8, 77]
for age in ages:
    if age<=18:
        checkup_fee.append(100.0)
    elif age < 30 and age>=18:
        checkup_fee.append((500.0))
    elif age <50 and age >=30:
        checkup_fee.append(400)
    else:
        checkup_fee.append(150.0)

print(checkup_fee)
print("-"* 50)
print([100.0 if age<=18 else 500 if (age < 30 and age>=18) else 400.0 if (age<50 and age>=30) else 150.0 for age in ages])