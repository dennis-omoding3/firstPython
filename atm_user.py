from atm import Atmcard

dennisCard=Atmcard(20000)
kevinCard=Atmcard(18500)
roseCard=Atmcard(24000)
# print(type(dennisCard))
# print(dennisCard.color)
# print(kevinCard.color)
# roseCard.deposit(1000)
# dennisCard.deposit(2450)
print(roseCard.balance)
print(dennisCard.balance)
print(kevinCard.balance)
print(roseCard.withdraw(100000))
print(dennisCard.withdraw(100))