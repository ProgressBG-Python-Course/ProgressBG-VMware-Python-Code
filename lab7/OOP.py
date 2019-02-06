#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# the OOP way to present a user account information
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class UserAccount:
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance

  def withdraw(self, amount):
    self.balance -= amount

user1 = UserAccount('Maria', 100)
user2 = UserAccount('Pesho', 10)

user1.withdraw(5)
user2.withdraw(5)

print("{0.name}'s balance is {0.balance}".format(user1))
print("{0.name}'s balance is {0.balance}".format(user2))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# the dictionary way to present a user account information:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# user1 = {
#   'name': 'Maria',
#   'balance': 100
# }
# user2 = {
#   'name': 'Pesho',
#   'balance': 10
# }

# def withdraw(user,amount):
#   user['balance'] -= amount

# withdraw(user1, 5)
# withdraw(user2, 5)

# print("{name}'s balance is {balance}".format(**user1))
# print("{name}'s balance is {balance}".format(**user2))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# the variable's way to to present a user account information:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# user1_name = 'Maria'
# user1_balance = 100
# user2_name = 'Pesho'
# user2_balance = 10

# def withdraw(balance, amount):
#   return balance - amount

# user1_balance = withdraw(user1_balance, 5)
# user2_balance = withdraw(user2_balance, 5)

# print("{}'s balance is {}".format(user1_name, user1_balance))
# print("{}'s balance is {}".format(user2_name, user2_balance))



