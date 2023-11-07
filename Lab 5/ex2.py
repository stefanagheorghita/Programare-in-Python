class Account:
    def __init__(self, account_number, balance):
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            if self.balance - amount < 0:
                print("Insufficient funds")
            else:
                self.balance -= amount

    def calculate_interest(self):
        pass

    def get_balance(self):
        print("Balance:", self.balance)


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100


class CheckingAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def get_account_number(self):
        print("Account number:", self.account_number)

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            if self.balance - amount < 0:
                print("Insufficient funds")
            else:
                print("Funds before withdrawal:", self.balance)
                self.balance -= amount
                print("Funds after withdrawal:", self.balance)


saving = SavingsAccount(123, 5000, 10)
saving.deposit(1000)
print("Interest:", saving.calculate_interest())
print("Balance:", saving.balance)
saving.withdraw(2000)
print("Balance:", saving.balance)
checking = CheckingAccount(123, 5000)
checking.deposit(1000)
print("Balance:", checking.balance)
checking.withdraw(2000)
print("Balance:", checking.balance)
