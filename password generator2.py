import random
print("WELCOME TO THE RANDOM PASSWORD GENERATOR BASED ON YOUR CHARACTER SELECTION")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '@', '*', '+']
#now we select no. of letter we want to form a password
no_of_letters = int(input("How many letters you need in your password\n"))
no_of_numbers = int(input("How many numbers you need in your password\n"))
no_of_symbols = int(input("How many symbols you need in your password\n"))
length_of_password = no_of_letters + no_of_numbers + no_of_symbols
print(f"so your password lenght will be: {length_of_password}\n")
password = []
new_password = ""
for let in range(0, no_of_letters):
    password.append(random.choice(letters))
for num in range(0, no_of_numbers):
    password.append(random.choice(numbers))
for sym in range(0, no_of_symbols):
    password.append(random.choice(symbols))
random.shuffle(password)
for char in password:
    new_password += char
print(f"Your randomly generated secured password is\n'{new_password}'")
