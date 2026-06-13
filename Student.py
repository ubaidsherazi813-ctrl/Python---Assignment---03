# Create a Student class With Private Attributes

class Student:

    def __init__(self , name , roll_no , marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    def set_name(self , name):
        if self.__name <" ":
            print(name)

    def get_name(self):
        return self.name 
    
    def set_roll_no(self , roll_no):
        if self.__roll_no < 100:
            print(f"{roll_no}")
        else:
            print("Invalid Rollno")    

    def get_roll_no(self):
        return self.__roll_no

    def set_marks(self , marks):
        if self.__marks > 0:
            print(f"{marks}")
        else:
            print("Invalid Marks")    

    def get_marks(self):
        return self.__marks

s1 = Student("Ubaid" , 22 , 90)

print(s1.get_name())

