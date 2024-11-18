# uses lambda function , sort the given list usng sorted fuction

data = ["sharma rohit", "koli virat", "tendulkar sachin", "gill subhaman", "kissan ishan"]
# sort the given list using secod name length
print(sorted(data,key=lambda nm:nm.split()[1]))
print(sorted(data,key=lambda nm:nm.split()[0]))

# def name(nm):
#     names = nm.split() # ["sharma" , "rohit"]
#     first_name = names[1]
#     return first_name
