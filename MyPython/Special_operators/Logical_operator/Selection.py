# conditions for selecting candidate in an interview
# 1. Must know python language
# 2. Must have more than 60%
# 3. Must be know basic manual

py_lang = input("Do you know python language:(y/n)")
marks = int(input("Enter your % of marks in degree"))
testing_manual = input("Do you basic concepts of manual:(y/n)")

if (py_lang =='y' and marks >= 60 and testing_manual=='y'):
    print("your selected for interview")
elif(py_lang=='n' and marks>= 60 and testing_manual=="y"):
    print("You are on hold")
else:
    print("your not selected")