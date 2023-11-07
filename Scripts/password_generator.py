import random
import string


def gen_pwds(num_pwds, pwd_len):
    passwords = []

    # print("Hello!")
    # while True:
    #     try:
    #         numPasswords = int(input("How many passwords would you like to generate?\n"))
    #         break
    #     except ValueError:
    #         print("Please enter a whole number")
    #
    # while True:
    #     try:
    #         passwordLength = int(input("What length should the passwords be? (between 6 and 15)\n"))
    #         if 5 < passwordLength < 16:
    #             break
    #         else:
    #             print("Length must be greater than 5 and less than 16")
    #             continue
    #     except ValueError:
    #         print("Please enter a whole number")
    #
    # print(f"{str(numPasswords)} passwords that are {str(passwordLength)} characters long? Coming right up!")

    for x in range(num_pwds):
        password = ""
        for y in range(pwd_len - 4):
            rand = random.randint(1, 4)
            match rand:
                case 1:
                    char = random.choice(string.ascii_lowercase)
                case 2:
                    char = random.choice(string.ascii_uppercase)
                case 3:
                    char = random.choice(string.digits)
                case 4:
                    char = random.choice(string.punctuation)

            password += char

        guaranteed_chars = [random.choice(string.ascii_lowercase), random.choice(string.ascii_uppercase),
                           random.choice(string.digits), random.choice(string.punctuation)]

        for char in guaranteed_chars:
            index = random.randint(0, len(password))
            password = password[:index] + char + password[index:]

        passwords.append(password)

    # return passwords
    print(passwords)
