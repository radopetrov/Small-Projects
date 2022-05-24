import random as ran

password_length = int(input("Please enter password length (at least 10 symbols)\n >>> "))
while password_length < 10:
    print("You password is too short, please enter longer password length")
    password_length = int(input(">>> "))
symbols = range(33, 48) and range(58, 65) and range(91, 96) and range(123, 126)
exclusive_nums = [34, 39, 44]
while True:
    password = ""
    uppercase_counter = 0
    lowercase_counter = 0
    symbol_counter = 0
    number_counter = 0
    while len(password) < password_length:
        num = ran.randint(33, 125)
        if num in exclusive_nums or chr(num) in password:
            continue
        password += chr(num)
        if chr(num).isupper():
            uppercase_counter += 1
        elif chr(num).islower():
            lowercase_counter += 1
        elif num in symbols:
            symbol_counter += 1
        elif chr(num).isnumeric():
            number_counter += 1
    if uppercase_counter == 0 or \
            lowercase_counter == 0 or \
            symbol_counter == 0 or \
            number_counter == 0:
        continue
    else:
        break
print(f"You password is:\n{password}")
