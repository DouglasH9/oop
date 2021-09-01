class BankAccount:
    population = 0

    def __init__(self, int_rate, balance):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.population += 1

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance {self.balance}")

    def yield_interest(self):
        self.balance /= self.int_rate
        return self

    @classmethod
    def print_pop (cls):
        print(f"There are {cls.population} accounts")
        

account_one = BankAccount(.9, 100)
account_two = BankAccount(.7, 200)

account_one.deposit(100).deposit(100).deposit(100).withdraw(50)
account_one.display_account_info()

account_two.deposit(100).deposit(100).withdraw(10).withdraw(10).withdraw(10).withdraw(10).yield_interest()
account_two.display_account_info()

BankAccount.print_pop()