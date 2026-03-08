# 01. create class
class PDFFile:
    #02. Create Object
    def __init__(self, file_name):
        self.name = file_name
        print(f"Add new file: {self.name}")
        
    # 03. Create a method
    def show_name(self):
        print(f"Name is: {self.name}")
# 04. Create Object
my_first_file = PDFFile("math.pdf")
my_second_file = PDFFile("ict.pdf")

my_first_file.show_name()
my_second_file.show_name()