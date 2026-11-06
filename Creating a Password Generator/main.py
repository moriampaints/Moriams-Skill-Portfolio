import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
rand_letters = random.sample(letters, k=nr_letters)
nr_symbols = int(input("How many symbols would you like?\n"))
rand_symbol = random.sample(symbols, k=nr_symbols)
nr_numbers = int(input("How many numbers would you like?\n"))
rand_numbers = random.sample(numbers, k=nr_numbers)

password_list = rand_letters + rand_symbol + rand_numbers
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Here is your password: {password}")