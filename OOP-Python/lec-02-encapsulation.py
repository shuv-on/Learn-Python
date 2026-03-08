class PDFLock:
    def __init__(self, filename, password):
        self.filename = filename         # Public (সবাই দেখতে পারবে)
        self.__password = password       # Private (লুকানো)

    # প্রাইভেট ডেটা এক্সেস করার জন্য ক্লাসের ভেতরের মেথড
    def verify_password(self, input_pass):
        if self.__password == input_pass:
            print(f"{self.filename} আনলক হয়েছে!")
        else:
            print("ভুল পাসওয়ার্ড!")

# অবজেক্ট তৈরি
my_locked_file = PDFLock("secret_diary.pdf", "12345")

# Public ডেটা সরাসরি এক্সেস করা যায়
print(my_locked_file.filename) 

# Private ডেটা সরাসরি এক্সেস করতে গেলে Error দেবে
# print(my_locked_file.__password) # এই লাইনটা রান করলে পাইথন বকা দেবে!

# প্রাইভেট ডেটা চেক করার সঠিক উপায় (মেথডের মাধ্যমে)
my_locked_file.verify_password("12345")