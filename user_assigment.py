class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.account_balance)
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
    

doug = User('doug')

tony = User('tony')

kirby = User('kirby')

doug.make_deposit(300)
doug.make_deposit(200)
doug.make_withdrawal(100)

tony.make_deposit(100)
tony.make_deposit(100)
tony.display_user_balance

kirby.make_deposit(500)
kirby.make_withdrawal(100)
kirby.make_withdrawal(50)
kirby.make_withdrawal(20)
kirby.display_user_balance()
doug.display_user_balance()
kirby.transfer_money(doug, 50)
doug.display_user_balance()
kirby.display_user_balance()
