file_size = float(input("Enter your file size: "))
if file_size <= 10:
    print("File accepted")
elif 10< file_size <= 50:
    print("Warning! Large file")
else:
    print("Error! file is too large")