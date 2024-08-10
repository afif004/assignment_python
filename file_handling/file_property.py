import os

filename = 'file_handling/example.txt'

# Get the status of the file
file_stat = os.stat(filename)

# Displaying file properties
print(f"File: {filename}")
print(f"Size: {file_stat.st_size} bytes")
print(f"File type: {'Directory' if os.path.isdir(filename) else 'File'}")
print(f"Permissions: {oct(file_stat.st_mode)}")
print(f"Last accessed: {file_stat.st_atime}")
print(f"Last modified: {file_stat.st_mtime}")
print(f"Creation time: {file_stat.st_ctime}")
