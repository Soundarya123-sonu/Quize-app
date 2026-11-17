
import random
import string

print("*******************************")
print("     PASSWORD GENERATOR")
print("******************************")

length = int(input("Enter password length: "))

if length < 4:
    print("Password length must be at least 4!")

else:
    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation

   
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(numbers),
        random.choice(symbols)
    ]

    
    all_characters = uppercase + lowercase + numbers + symbols

    
    for i in range(length - 4):
        password.append(random.choice(all_characters))

    
    random.shuffle(password)


    
    final_password = "".join(password)

    print("\nGenerated Password:", final_password)
    print("Password Length:", length)
    print("Password Generated Successfully!")


