#  using super class

class Computer:

    def __init__(self, ram,storage):
        self.ram = ram
        self.storage = storage
        print("Computer class constructor called")

    def dispaly(self):
        print("display instant method called")

class Mobile(Computer):

    def __init__(self ,ram , storage  ):
        super().__init__(ram , storage)
        super().dispaly()
        self.mobile = "Samsung"
        print("Mobile class constructor called ")


ram = input("Enter the ram value : ")
storage = input("Enter the storage value : ")
samsung = Mobile(ram, storage)
print(samsung.__dict__)