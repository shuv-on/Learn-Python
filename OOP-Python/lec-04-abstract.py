from abc import ABC, abstractmethod

# এটি একটি Abstract Class বা রুলবুক (এর কোনো অবজেক্ট বানানো যাবে না)
class PDFTool(ABC):
    
    @abstractmethod
    def run_tool(self):
        pass # pass মানে এখানে কোনো কোড নেই, শুধু নিয়ম দেওয়া হলো

# Child Class
class SplitTool(PDFTool):
    # প্যারেন্ট ক্লাসের নিয়ম অনুযায়ী run_tool মেথডটা এখানে রাখতেই হবে, না হলে Error দেবে।
    def run_tool(self):
        print("পিডিএফ স্প্লিট করার জটিল কোড রান হচ্ছে...")

# my_tool = PDFTool() # এটা করলে পাইথন Error দেবে! Abstract ক্লাসের অবজেক্ট হয় না।

# চাইল্ড ক্লাসের অবজেক্ট তৈরি এবং মেথড কল
my_split_tool = SplitTool()
my_split_tool.run_tool()