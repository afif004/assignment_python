# Define the content you want to write to the file
content = input()

# Open a file in write mode
with open("example.txt", "w") as file:
    # Write the content to the file
    file.write(content)

# The file is automatically saved and closed when using 'with' statement
print("File created and saved successfully.")