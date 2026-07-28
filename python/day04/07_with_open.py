# Read the entire file
print("=== Read Entire File ===")

with open("message.txt", "r") as file:
    content = file.read()

print(content)

print()

# Write to a file
print("=== Write File ===")

with open("practice.txt", "w") as file:
    file.write("Python\n")
    file.write("File IO\n")
    file.write("with open")

print("practice.txt was created.")

print()

# Read a file line by line
print("=== Read Line by Line ===")

with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())