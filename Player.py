# Using Class And instance attribute

class Player:

    player_count = 0

    def __init__(self , name , level):
        self.name = name
        self.level = level

        Player.player_count += 1

    def display(self):
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")   
        print("-" * 25)

p1 = Player("Ubaid" , 20)
p2 = Player("Ali" , 10)
p3 = Player("Ahmed" , 12)

p1.display()
p2.display()
p3.display()

print("Total Player is playing: " , Player.player_count)