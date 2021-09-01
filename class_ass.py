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
        self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def print_pop (cls):
        print(f"There are {cls.population} accounts")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(.02, 0)
        
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
        
    def make_withdrawal(self, amount):
        self.account.withdrawal(amount)
        return self

    def give_interest(self):
        self.account.yield_interest()
        return self

    def display_user_balance(self):
        self.account.display_account_info()

    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        return self


doug = User("doug", "douglash9882@gmail.com")
doug.make_deposit(50).give_interest()
doug.display_user_balance()
