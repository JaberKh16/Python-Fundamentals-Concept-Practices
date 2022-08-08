# defining the class
class BankAccount:

    bank_name = 'ABC bank, XYZ Street, New Delhi'

    def __init__(self, name, balance=0, bank=bank_name):
        self.name = name
        self.balance = balance
        self.bank = bank

    def display(self):
        print(self.name, self.balance, self.bank)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

# creating instances    
account_1 = BankAccount('Mike', 200, 'PQR Bank Delhi')
account_2 = BankAccount('Tom')

# accessing class instance methods
account_1.display()
account_2.display()