# Create an Employee class by using Abstraction Concept

from abc import ABC , abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self , stipend):
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend   
        

class FullTimeEmployee(Employee):
    def __init__(self , monthly_salary):
        self.monthly_salary = monthly_salary
    
    def calculate_salary(self):
        return self.monthly_salary

class ContractEmployee(Employee):
    def __init__(self , hours_worked , rate_per_hour):
        self.hours_worked = hours_worked
        self.rate_per_hour = rate_per_hour

    def calculate_salary(self):
        return self.hours_worked * self.rate_per_hour    
        


int1 = Intern(50000)
print(int1.calculate_salary())

fte1 =  FullTimeEmployee(60000)
print(fte1.calculate_salary())
     
conemp1 = ContractEmployee(100 , 500)
print(conemp1.calculate_salary())