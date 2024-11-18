#  map function it is also  higher order function it is also worked as filer
#  syntax of map function is --> mapped_obj = map(function_name , iterable) # it will accept n number of iterables
# function_name --> function with logic for mapping
# iterables --> lke sequences set, string , list , tuple etc

sport_names = ['cricket', 'football', 'hockey', 'volleyball', 'baseball', 'chess' ]

def sport_length(names):
    return names ,len(names)
mapped_obj =map(sport_length,sport_names)
# print(mapped_obj)
# print(type(mapped_obj))
# print(list(mapped_obj))
for ele in mapped_obj:
    print(ele[0],"----->",ele[1])

