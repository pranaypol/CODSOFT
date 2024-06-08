import random
import string


def generate_password(length):
    letters = string.ascii_letters
    special_chars = "&*!@#$%"
    numbers = string.digits

    chars = letters + special_chars + numbers
    password = "".join(random.choice(chars)for i in range(length))

    return password


length = int(input("Enter password length: "))
password = generate_password(length)
print(password)
