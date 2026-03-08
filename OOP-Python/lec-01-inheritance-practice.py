class User:
    def __init__(self, username):
        self.username = username
    def login(self):
        print(f"{self.username} Log in successfully")
class PremiumUser(User):
    def unlock_features(self):
        print(f"Features unlock for {self.username}")

users = PremiumUser("Hasan")
users.login()
users.unlock_features()