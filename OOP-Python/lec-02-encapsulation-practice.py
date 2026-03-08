class UserWallet:
    def __init__(self, username, balance):
        self.username = username
        self.__balance = balance
    def add_money(self, amount):
        if amount > 0:
            self.__balance+=amount
            print(f"Money added. New balance is {self.__balance}")
        else:
            print("Invalid amount")
user_wallet = UserWallet("Shuvon", 500) 
user_wallet.add_money(1000)         