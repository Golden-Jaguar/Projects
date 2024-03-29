#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# for letter in range(1):
#     array_letter = random.sample(letters, k=nr_letters)
#     #print(array_letter)
# for symbol in range(1):
#     array_symbol = random.sample(symbols, k=nr_symbols)
#     #print(array_symbol)
# for number in range(1):
#     array_number = random.sample(numbers, k=nr_numbers)
#     #print(array_number)
# password = array_number + array_symbol + array_letter
#
# print(f"Here is your password: {''.join(password)}")
#
# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# random.shuffle(password)
# print(f"Here is your password with randomized order: {''.join(password)}")

#Teacher Answer
password = []

for char in range(1, nr_letters + 1):
    password += random.choice(letters)
for num in range(1, nr_numbers + 1):
    password += random.choice(numbers)
for sym in range(1, nr_symbols + 1):
    password += random.choice(symbols)
print(f"Here is your password: {password}")
#password = list(password)
random.shuffle(password)
print(f"Here is your randomized password: {''.join(password)}")