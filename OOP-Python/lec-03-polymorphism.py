class PDFFile:
    def open(self):
        print("PDF রিডার ইঞ্জিন দিয়ে ফাইল ওপেন হচ্ছে...")

class TextFile:
    def open(self):
        print("সাধারণ নোটপ্যাড স্টাইলে ফাইল ওপেন হচ্ছে...")

# পলিমরফিজম প্রয়োগ
file1 = PDFFile()
file2 = TextFile()

# আমরা একটি লিস্টে দুটো ভিন্ন ক্লাসের অবজেক্ট রাখলাম
my_files = [file1, file2]

# লুপ চালিয়ে একই নামের মেথড কল করছি, কিন্তু আউটপুট আসবে ভিন্ন!
for file in my_files:
    file.open()