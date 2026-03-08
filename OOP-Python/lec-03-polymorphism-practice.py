class FreeUser:
    def get_limit(self):
        print("Max 3 PDF merges allowed per day")
class PremiumUser:
    def get_limit(self):
        print("Unlimited PDF merges allowed per day")
obj1 = FreeUser()
obj2 = PremiumUser()
users = [obj1, obj2]

for user in users:
    user.get_limit()