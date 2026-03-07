merged_files = []
for value in range(1, 4):
    pdf_name = input()
    merged_files.append(pdf_name)
print(merged_files)

current_file_status = {
    "total_files" : len(merged_files),
    "status" : "Ready to merge"
}
print(current_file_status)
print(current_file_status["total_files"])