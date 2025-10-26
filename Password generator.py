# Password Generator

import random # For random numbers etc.

password = list("abcdefghijklmnopqrstuvwxyz")

upper_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

nums = list("0123456789")

symbols = list("!@#$%^&*()-_=+[]{}|;:,.<>?/")


print("Welcome to Password Generator")
while True:
    try:
        user_pass_length = int(input("How long do you want the password to be?: "))
        break
    except ValueError:
        print("Please give numeric lenght!")

while True:
    user_pass_caps = input("Do you want to include uppercase letters? (yes/no): ").lower()
    if user_pass_caps.lower() in ["yes" , "no"]:
        break
    else:
        print("Please enter 'yes' or 'no'.")
        
while True:
    user_pass_nums = input("Do you want to include numbers? (yes/no): ").lower()
    if user_pass_nums.lower() in ["yes" , "no"]:
        break
    else:
        print("Please enter 'yes' or 'no'.")
        
while True:
    user_pass_symbols = input("Do you want to include symbols? (yes/no): ").lower()
    if user_pass_symbols.lower() in ["yes" , "no"]:
        break
    else:
        print("Please enter 'yes' or 'no'.")

if user_pass_caps.lower() == "yes":
    password.extend(upper_letters)
if user_pass_nums.lower() == "yes":
    password.extend(nums)
if user_pass_symbols.lower() == "yes":
    password.extend(symbols)
    
user_password = random.choices(password, k=user_pass_length)

password_string = "".join(user_password)

print(password_string)
