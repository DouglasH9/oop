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
        print(self.balance)

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
        self.account = {
            "checking" : BankAccount(.02, 0),
            "savings" : BankAccount(.05, 0)
        }
        
    def make_deposit(self, amount, acctType):
        self.account[acctType].deposit(amount)
        return self
        
    def make_withdrawal(self, amount, acctType):
        self.account[acctType].withdrawal(amount)
        return self

    def give_interest(self, acctType):
        self.account[acctType].yield_interest()
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Checking acct balance: {self.account['checking'].balance}")
        print(f"User: {self.name}, Savings acct balance: {self.account['savings'].balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        return self


doug = User("doug", "douglash9882@gmail.com")
doug.make_deposit(50, 'savings').give_interest('savings').make_deposit(2000, 'checking')
doug.display_user_balance()
