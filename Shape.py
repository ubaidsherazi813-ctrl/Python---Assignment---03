# Create Shape class and same method name Area for different classes

class Shape:

    def Area(self):
        print("Area of Sahpe")

class Circle(Shape):
        
    def Area(self , r):
        self.r = r
        print(f"Area of Circle is {3.14 * r * r}")

class Rectangle(Shape):

    def Area(self , l , w):
        self.l = l
        self.w = w

        print(f"Area of Rectangle is {l*w}")

class Triangle(Shape):

    def Area(self , b , h):
        self.b = b
        self.h = h

        print(f"Area of Triangle is {1/2 *(b * h)}")

c1 = Circle()
c1.Area(7)

r1 = Rectangle()
r1.Area(4 , 3)

t1 = Triangle()
t1.Area(5 , 6)







        

