#  Multi - level inheritance

class Grand_father():

    def __init__(self , land):
        self.property = land
        print("grand father class called")
class Father(Grand_father):

    def __init__(self ,land , house ):
        super().__init__(land)
        self.house = house
        print("Father class called ")
    

class Son(Father):

    def __init__(self,land, house ,car):
        super().__init__(house,land)
        self.car = car
        print("son class called")

land = input("Enter your land propertires : ")
house = input("Enter the house : ")
car = input("Enter your car : ")
s = Son(land ,house,car )
print(s.__dict__)