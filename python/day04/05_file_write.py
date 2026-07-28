# Write to hello.txt
file = open("hello.txt", "w")

file.write("Hello Python!")

file.close()

# Write to student.txt
file = open("student.txt", "w")

file.write("Kim\n")
file.write("Lee\n")
file.write("Park\n")

file.close()

# Write to message.txt
file = open("message.txt", "w")

file.write("Python\n")
file.write("is\n")
file.write("awesome!")

file.close()