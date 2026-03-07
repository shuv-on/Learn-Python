def check_pdf_extesnsion(file_name):
    """ if file_name.endswith(".pdf"):
        return True
    else:
        return False """
    return file_name.endswith(".pdf")
    
file1 = check_pdf_extesnsion("routine.pdf")
print("Output: ", file1)
file2 = check_pdf_extesnsion("song.mp3")
print("Output: ", file2)
    