#  it should contain iterable object like list
#  it re counter the values

#  what is use Enumerate function
#  while using loopings
import json

sports = ["Cricket", "Volleyball", "Hockey", "Kabaddi"]

# enum_obj = enumerate(sports, start=1)
# print(enum_obj)
# print(type(enum_obj))
# print(list(enum_obj))
#  using enumerate  in loop print position and element

# for pos, ele in enumerate(sports , start=1):  # it will in execute like [pos , ele]
#     # print(pos , ele)
#     print(f"{pos}:{ele}") #

# conversion to dictionary
dic_obj1 = dict(list(enumerate(sports,1)))
print(dic_obj1)

# convert to json file
f=open('data.json','w')
json.dump(dic_obj1 ,f)
f.close()