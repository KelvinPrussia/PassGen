import random
import string


def gen_pwds(num_pwds, pwd_len):
    passwords = []

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

    return passwords
