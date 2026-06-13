# Using meyhod Overlloding

class Person:

    def __init__(self , name , age = None , address = None):
        self.name = name
        self.age = age
        self.address = address
        
    def display(self):
        print(f"Name is {self.name}")

        if self.age is not None:
            print(f"Age is {self.age}")  

        if self.address is not None:
            print(f"Address is {self.address}")      

        print("-" * 20)
p1 = Person("Ubaid")
p2 = Person("Ubaid" , 20)
p3 = Person("Ubaid" , 20 , "Tando Adam")

p1.display()
p2.display()
p3.display()

