# polymorphism inheritance

class Veh:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def get_details(self):
        print("Vehicle name is : ", self.name)
        print("Vehicle color is : ", self.color)
        print("Vehicle price is : ", self.price)

    def max_speed(self):
        print("Max speed is 100")

    def gear(self):
        print("Gear change is 6")

# v1 = Veh("Toyota", "Red" , 2000000)
# v1.get_details()


class Car(Veh):
    def max_speed(self):
        print("Max speed is 180")

    def gear(self):
        print("Gear change is 7")


v1 = Veh("Toyota", "Red", 2000000)
c1 =Car("TATA", "Blue", 1800000)
v1.get_details()
v1.max_speed()
v1.gear()
print("-----------------------")
c1.get_details()
c1.max_speed()
c1.gear()