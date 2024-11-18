#  in python there is no method overloading concept but we can achieve through some logic of programing

class Cal:

    def add(self,num1=None, num2 =None, num3=None ):

        if num1!=None and num2!= None and num3!=None:
            print("Addition is ", num1+num2+num3)

        elif num1!=None and num2!=None:
            print("Addition is ", num1 + num2)

        else:
            print("Invalid parameters ")


c1 = Cal()
c1.add(10,20)
c1.add(90, 30, 50)