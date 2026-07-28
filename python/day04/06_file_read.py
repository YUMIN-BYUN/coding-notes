# Read the entire file
file = open("message.txt", "r")

content = file.read()

print("=== read() ===")
print(content)

file.close()

print()

# Read one line at a time
file = open("message.txt", "r")

print("=== readline() ===")
print(file.readline().strip())
print(file.readline().strip())
print(file.readline().strip())

file.close()

print()

# Read all lines as a list
file = open("message.txt", "r")

lines = file.readlines()

print("=== readlines() ===")
print(lines)

file.close()

print()

# Iterate through the list
file = open("student.txt", "r")

lines = file.readlines()

print("=== Student List ===")
for line in lines:
    print(line.strip())

file.close()