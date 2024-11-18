#  Encapsulation is achieved by declaring datas as private ( __ ) double underscore is private access modifier

class Finance:

    def __init__(self):
        self.__revenue = 100000 # private
        self.__sales = 114
    # how to make private method
    def __display(self):
        print(f"the company revenue is{self.__revenue} and total sales is {self.__sales} ")

f1 = Finance()
print(f1._Finance__revenue ) # name mangling so python is not pure encapsulation it only restricts the  direct access
print(f1.__dict__)



# class Hr:
#
#     def __init__(self):
#         self.num_of_employes= 32
#         print(f1.__revenue)
#
#
# hr = Hr()
# print(f1.__dict__)


