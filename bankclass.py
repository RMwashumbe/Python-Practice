class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds")

    def display_balance(self):
        print(f"Account Number:{self.account_number}")
        print(f"Holders Name:{self.holder_name}")
        print(f"Balance:{self.balance}")


my_account = BankAccount("3938309", "Robert", 1000000000)
my_account.display_balance()
my_account.deposit(800000)
my_account.display_balance()
my_account.withdraw(15000000000)
my_account.display_balance()
