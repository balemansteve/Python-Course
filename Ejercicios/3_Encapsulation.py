class BankAccount:
  def __init__(self):
    self.__balance = 0

  def deposit(self, amount):
    if amount > 0:
      self.__balance += amount
      print(f"Deposited: {amount}")
    else:
      print(f"Invalid deposit amount")

  def withdraw(self, amount):
    if 0 < amount < self.__balance:
      self.__balance -= amount
      print(f"Withdraw: {amount}")
    else:
      print(f"Insufficient founds")
  
  def get_balance(self):
    print(f"Balance: {self.__balance}")

account = BankAccount()

account.deposit(100)
account.withdraw(30)
account.get_balance()
