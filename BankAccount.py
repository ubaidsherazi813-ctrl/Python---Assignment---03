# Create a bankaccount with attributes and method

class Bankaccount:

    def __init__(self , owner , accnum , balance):
        self.owner = owner
        self.accnum = accnum
        self.balance = balance

    def deposit(self , amount):
        amount>self.balance
        self.balance+=amount
        

    def withdraw(self , amount):
        amount<self.balance
        self.balance-=amount        

acc1 = Bankaccount("Ubaid" , 123 , 50000)
acc2 = Bankaccount("Ali" , 789 , 70000)

acc1.deposit(5000)
acc1.withdraw(10000)

acc2.withdraw(20000)

print(acc1.owner , acc1.balance , acc1.accnum)
print(acc2.owner , acc2.balance , acc2.accnum)



        
