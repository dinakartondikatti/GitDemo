# using decorator

def addition_thrid(addition):
    def inner():
        result = addition()
        num3 = float(input("Enter the thrid number : "))
        result = result + num3
        return result

    return inner


@addition_thrid
def addition():
    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number : "))
    result = num1 + num2
    return result


print(addition())
