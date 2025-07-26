import random
import string

# Get password length from user
length = int(input("How long should the password be? "))

# Use letters and numbers only (simple)
chars = string.ascii_letters + string.digits

# Generate password
password = ""
for i in range(length):
    password += random.choice(chars)

# Show the password
print("Your password is:", password)