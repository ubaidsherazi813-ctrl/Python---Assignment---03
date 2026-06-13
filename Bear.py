# Using Multiple Inheritance

class herbivore:

    def __init__(self , eat_plants):
        self.eat_plants = eat_plants

class carnivore:

    def __init__(self , eat_meat):
        self.eat_meat = eat_meat

class omnivore:

    def __init__(self , eat_both_food):
        self.eat_both_food = eat_both_food
        
class Bear(herbivore , carnivore , omnivore):

    def __init__(self, name , eat_plants , eat_meat , eat_both_food):

        self.name = name

        herbivore.__init__(self , eat_plants)       
        carnivore.__init__(self , eat_meat)
        omnivore.__init__(self , eat_both_food)

    def display(self):
        print(f"Name: {self.name}")
        print("-" * 20)
        print(f"Eating Plants: {self.eat_plants}")
        print(f"Eating Meat: {self.eat_meat}")
        print(f"Eating both food: {self.eat_both_food}")
        print("-" * 20)

b1 = Bear("Bablo", "Berries", "Fish", "Berries + Fish")

b1.display()
         