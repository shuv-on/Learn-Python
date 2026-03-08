class UserWallet:
    def __init__(self, username, balance):
        self.username = username
        self.__balance = balance
    def add_money(self, amount):
        if amount > 0:
            amount+=self.__balance
            print(f"Money added. New balance is {amount}")
        else:
            print("Invalid amount")
user_wallet = UserWallet("Shuvon", 500) 
user_wallet.add_money(1000)         