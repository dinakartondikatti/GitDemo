# polymorphism in functions and objects

class BMW:

    def fuel_type(self):
        print("Diesel")

    def max_speed(self):
        print("Max speed is 200")

class Ferrari:
    def fuel_type(self):
        print("petrol")

    def max_speed(self):
        print("Max speed is 180")


def car_deatils(obj):
    obj.fuel_type()
    obj.max_speed()


bmw = BMW()
ferrari = Ferrari()

car_deatils(bmw)
print("/*****************/")
car_deatils(ferrari)