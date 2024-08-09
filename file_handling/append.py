file_name = "file_handling\\" + input("File Name: ") + ".txt"
apnd = input("Append: ")
with open(file_name, "a") as file:
    file.write("\n" + apnd)