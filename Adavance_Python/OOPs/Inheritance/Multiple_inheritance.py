#  NMultiple inheritance

class Country:

    def __init__(self):
        super().__init__()
        print("Country class constructor is called")
        self.office = "Delhi"


class State:

    def __init__(self):
        super().__init__()
        print("State class constructor is called")
        self.office = "Bengaluru"

class Mini:

    def __init__(self):
        print("Mini class constructor is called ")
        self.office = "mini"

class District(State, Country ,Mini):

    def __init__(self):
        super().__init__()
        print("District class constructor is called")
        self.office = "Belagavi"


d = District()
print(d.__dict__)
