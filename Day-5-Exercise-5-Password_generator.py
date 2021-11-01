#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
for letter in range (0,nr_letters):
  next_letter = letters[random.randint(0, 52)]
  #next_letter = random.choice(letters) **as per trainer
  password += next_letter
  #Refactoring: password += random.choice(letters)

for symbol in range (0,nr_symbols):
  next_symbol = symbols[random.randint(0, 8)]
  password  += next_symbol

for number in range (0,nr_letters):
  next_number = numbers[random.randint(0, 9)]
  password  += next_number

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for letter in range (0,nr_letters):
  password_list.append(random.choice(letters))

for symbol in range (0,nr_symbols):
  password_list.append(random.choice(symbols))

for number in range (0,nr_letters):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)

final_password = ""
for char in password_list:
  final_password += char

print(final_password)