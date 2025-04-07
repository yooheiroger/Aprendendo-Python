import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
# underscore is a disposable variable when you need just to execute the block of code use _

for _ in range(nr_letters): #in range takes only the lenght
        random_letter = random.choice(letters)
        password_list.append(random_letter)

for _ in range(nr_symbols):
        random_symbols = random.choice(symbols)
        password_list.append(random_symbols)

for _ in range(nr_numbers):
        random_number = random.choice(numbers)
        password_list.append(random_number)

random.shuffle(password_list)# altera a lista de forma inplace, altera a lista original

# for password in password_list:
#     print(password , end='')


print()

password1 = ''
for password in password_list:
    password1 += password

print(password1)


