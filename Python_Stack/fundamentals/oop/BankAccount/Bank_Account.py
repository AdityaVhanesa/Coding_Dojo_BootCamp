class BankAccount:
    # don't forget to add some default values for these parameters!
    allBankAccounts = []

    def __init__(self, int_rate, balance):
        self.intrestRate = int_rate
        self.balance = balance
        BankAccount.allBankAccounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount

        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.intrestRate
        return self

    @classmethod
    def print_all_accounts_info(cls):
        for account in cls.allBankAccounts:
            account.display_account_info()


account_1 = BankAccount(1.5, 5000)
account_2 = BankAccount(2.5, 10000)

account_1.deposit(100).deposit(200).deposit(1000).withdraw(743).yield_interest().display_account_info()
account_2.deposit(5893).deposit(190).withdraw(12000).withdraw(500).withdraw(2250).withdraw(
    790).yield_interest().display_account_info()

BankAccount.print_all_accounts_info()

