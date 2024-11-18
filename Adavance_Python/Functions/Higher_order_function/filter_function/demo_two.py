#  using string in filter

# str1 = "Dinakareou"
vowel_list = ['a', 'e', 'i', 'o', 'u']
# def vowel(ch):
#     if ch in vowel_list:
#         return True
# converting this into lambda function

filtered_obj = filter(lambda ch:ch in vowel_list, input("Enter the words : "))
print(list(filtered_obj))

