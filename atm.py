# creating a new class
# read on principles of OOP
# class name must start with uppercase

class Bank:
    name="equity"

class Atmcard(Bank):

    #this is a property
#a class variable/data member
    # a class variable is shared among all instances of class
   color="brown"
   balance=0

# actions are called methods
# methods are just functions only that they are inside a class
# a constructor is a special method that runs everytime you instantiate
 #in python
   def __init__(self,balance):
       self.balance=balance

   def deposit(self,amount):
      self.balance+=amount

   def withdraw(self,amount):
        if self.balance<=amount:
            print("sorry, insufficient funds")
        else:
           self.balance-=amount
           print("transaction complete{}".format(amount))






