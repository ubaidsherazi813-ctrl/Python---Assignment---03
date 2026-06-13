# Create a class Vehicle and subclass bike and car with different attributes

class Vehicle:

    def __init__(self , model , brand):
        
        self.model = model
        self.brand = brand

class Bike(Vehicle):

    def __init__(self, model, brand , engine):
        super().__init__(model, brand)
        self.engine = engine  

class Car(Vehicle):

    def __init__(self, model, brand , seats):
        super().__init__(model, brand)
        self.seats = seats
     
    

b1 = Bike("125" , "Honda" , "150cc")

print(b1.model , b1.brand , b1.engine)

c1 = Car("2025" , "BMW" , 5)

print(c1.brand , c1.model , c1.seats)
