#  filter the even number in the given list
#  filer syntax :  filter_obj = filter(function_name , iterable) # only one iterable it will accept
#  here function_name -  is we need create function for sequence(iterable) or logic is true or not ,
#  if it is true then it will select and save in filtered_obj or not
#  and iterable - is collection like list , set , tuple , string
#   only one time we can use the filtered_obj
# data = [23, 24, 67, 83, 98, 100, 62]

# creating function(logic) for given sequence
# def even(num):
#     return  num%2 == 0
# converting this into lambda --> lambda num:num%2 == 0
    # if num%2 == 0:
    #     return True
    # else:                      it is optional  if is didn't use else then only if condition work
    # , if condition was not true then the value is not return then it will return none --> it means FLase
    #     return False
# print(filtered_obj) # provide  obj address
# print(type(filtered_obj)) # type of filtered obj

#  if you want print the filtered_obj then use for loop or typecasting into collection (list, tuple, set)

# for ele in filtered_obj:
#     print(ele)
# filtered_obj = filter(lambda num:num%2 == 0,data)
# print(list(filtered_obj))

# writing above one into complex format
print(list(filter(lambda num:num%2!= 0,[23, 24, 67, 83, 98, 100, 62]))) #  in itertable we can use input function -->