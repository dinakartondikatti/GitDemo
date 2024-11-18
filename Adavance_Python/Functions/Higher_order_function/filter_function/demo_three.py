#  using filter function in dictionary
#  example 1 : filter students having marks greater than or equal to 90

data = {"notesh":78, "raju":90, "dina":95, "guru":76, "krishna":89 }
# print(data["notesh"]>=90) using  this logic
def topper(student):
    return data[student]>=90

filtered_obj = filter(topper, data)
print(list(filtered_obj))