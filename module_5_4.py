class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        if len(args) > 0:
            cls.houses_history.append(args[0])
        instance = super().__new__(cls)
        return instance
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __str__(self):
        return f'Name: {self.name}, number of floors: {self.number_of_floors}.'
    def __del__(self):
        print(f'{self.name} demolished, but it will remain in history')
h1 = House('SHK Elbrus', 30)
print(House.houses_history)
h2 = House('SHK Acacia', 15)
print(House.houses_history)
h3 = House('SHK Matryoshka', 20)
print(House.houses_history)
del h2
del h3
print(House.houses_history)