class File:
    def __init__(self, name):
        self.name = name
    
    def open_file(self):
        print(f"{self.name} Opening......")
class PDFFile(File):
    def merge(self, other_pdf):
        print(f"{self.name} Merging with {other_pdf.name} pdf")
my_pdf = PDFFile("document.pdf")  
my_pdf.open_file()
#my_pdf.merge()
math_pdf = PDFFile("Math.pdf")
math_pdf.open_file()
my_pdf.merge(math_pdf)