# example 1

name = "Subhas_chandra_bose"

character = input("enter the character or subset : \n")

if character in name:
    print(f"{character} is present in the {name}")
else:
    print(f"{character} this character and subset not present in {name}")

print("*************")

#example 2

num1 = [1,2,3]

print(num1 in num1)