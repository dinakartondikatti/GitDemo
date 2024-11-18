# write  a nested function using lambda

quabe_root= lambda num:num**3

modify_qube = lambda func:lambda num:func(num)+num
print(modify_qube(quabe_root)(int(input("Enter the queeb numebr :"))))

# using if else in lambda function

max = lambda n1 , n2: n1 if n1>=n2 else n2
print(max(20 , 30))
