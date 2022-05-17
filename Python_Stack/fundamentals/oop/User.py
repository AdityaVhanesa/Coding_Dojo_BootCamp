from Bank_Account import BankAccount


class user:
    users = {

    }

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.account = {"checking": BankAccount(int_rate=2, balance=0),
                        "saving": BankAccount(int_rate=3, balance=500), }

        self.is_reward_member = False
        self.is_reward_member = False
        self.gold_card_points = 0

        user.users[f"{self.first_name} {self.last_name}"] = self

    def display_info(self):
        print("**************** User Information ****************")
        print("First Name --> {}".format(self.first_name))
        print("Last Nmae  --> {}".format(self.last_name))
        print("Email      --> {}".format(self.email))
        print("Age        --> {}".format(self.age))
        return self

    def enroll(self):
        if self.is_reward_member:
            print("User already a member")
            return self

        self.is_reward_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("Not enough points for spend")
            return self
        self.gold_card_points -= amount
        return self

    def make_deposit(self, amount, account_name):
        self.account[account_name].deposit(amount)
        return self

    def make_withdrawal(self, amount, account_name):
        self.account[account_name].withdraw(amount)
        return self

    def dispaly_user_balance(self, account_name):
        self.account[account_name].display_account_info()
        return self

    def create_new_account(self, account_name, intrest_rate, initial_balance):
        if account_name not in self.account:
            print("Account name already exist, Please Choose different account.")
        else:
            self.account[account_name] = BankAccount(int_rate=intrest_rate, balance=initial_balance)

        return self

    def transfer_money(self, ammount, other_user):
        if other_user not in user.users:
            print(f"{other_user} does not exist in the system.")
            return self
        if ammount > self.account["checking"].balance:
            print(f"Insufficient funds in the checking account for transfer")
            return self

        self.make_withdrawal(amount=ammount, account_name="checking")
        user.users[other_user].make_deposit(ammount, "checking")
        return self


# --> Creating User 1
user_1 = user("Aditya", "Vhanesa", "adityaVha@gmail.com", "23")
user_1.display_info().enroll().spend_points(50).display_info()
# --> Calling Chaining of methods on user_1.


# --> Creating two more users.
user_2 = user("Neel", "Vhanesa", "NeelVha@gmail.com", "13")
user_3 = user("Shreeja", "Vhanesa", "SeejaVha@gmail.com", "33")

user_2.enroll().spend_points(80).display_info()
# --> Enrolling user 2 in Membership program and calling chaining of methods.

user_3.display_info().spend_points(40).display_info()
# --> Calling Chain of methods on user_3.

user_1.make_deposit(50000, "checking").dispaly_user_balance("checking")
user_1.transfer_money(5000, "Neel Vhanesa").dispaly_user_balance("checking")
user_2.dispaly_user_balance("checking")

