import random
import string

print("Hello!")
while True:
    try:
        numPasswords = int(input("How many passwords would you like to generate?\n"))
        break
    except:
        print("Please enter a whole number")

while True:
    try:
        passwordLength = int(input("What length should the passwords be? (between 6 or 12)\n"))
        break
    except:
        print("Please enter a whole number")


print(str(numPasswords) + " password that are " + str(passwordLength) + " characters long? Coming right up!")

for x in range(numPasswords):
    password = ""
    for y in range(passwordLength):
        rand = random.randint(1,4)
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

    print(password)