class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.balance}")

# Test the BankAccount class
account = BankAccount("Patrick", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(200)
