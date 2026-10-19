
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def display_balance(self):
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        interest = self.balance * 0.05
        print("Interest:", interest)


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")


savings = SavingsAccount(10000)
current = CurrentAccount(5000)

savings.display_balance()
savings.calculate_interest()

current.withdraw(1000)
current.display_balance()
