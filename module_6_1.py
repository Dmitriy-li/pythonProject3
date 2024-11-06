class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} ate {food.name}")
                self.fed = True
            else:
                print(f"{self.name} didn't eat {food.name}")
                self.alive = False
        else:
            print(f"{self.name} can't eat {food}")
class Plant:
    edible = False
    def __init__(self, name):
        self.name = name
class Mammal(Animal):
    pass
class Predator(Animal):
    pass
class Flower(Plant):
    pass
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True
a1 = Predator('The Wolf of Wall Street')
a2 = Mammal('Hachiko')
p1 = Flower('The flower is seven-colored')
p2 = Fruit('A clockwork orange')
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)