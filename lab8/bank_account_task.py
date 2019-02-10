class BankAccount():
  def __init__(self, name, balance):
    self.name = name
    self.__balance = balance

  def set_balance(self, amount):
    print(f'The balance of {self.name} is changed!')
    self.__balance = amount

  def __str__(self):
    return f"{self.name} balance is {self.__balance}"

maria_account = BankAccount("Maria", 1_300)

print(maria_account)
print(maria_account.__dir__())


print(maria_account.__sizeof__())


