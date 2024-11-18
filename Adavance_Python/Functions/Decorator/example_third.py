#  using multiple decorator in single function
#  first decorator make the string into uppercase
#  second decorator make into split

#decorator1
def upper_case(full_name):
    def inner():
        return full_name().upper()
    return inner

# decorator 2
def split_name(full_name):
    def inner():
        return full_name().split()
    return inner
@split_name
@upper_case
def full_name():
    first_name=input("Enter the first_name : ")
    last_name=input("Enter the last_name : ")
    name = first_name+" "+last_name
    return name


# full_name=split_name(upper_case(full_name))
print(full_name())