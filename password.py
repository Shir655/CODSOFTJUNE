import random 
import math

def generate_password(length):
    password = ""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    for i in range(length):
        new= math.floor(random.random() * len(characters))
        password += characters[new]
    return password

password_length = int(input("Enter password length: "))
generated_password = generate_password(password_length)
print("Your password is:", generated_password)