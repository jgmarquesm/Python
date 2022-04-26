import string
import random

print(" ")
n = int(input("How many passwords you want to? "))
print("_______________________________________________________________________________")
i = 0
while i < n:
    print(" ")
    size_in = input("How many characters do you need in this password? ")
    print(" ")
    size_in = size_in.lower()
    if size_in == "stop":
        quit()
    def password(size):
        all_char = string.ascii_letters + string.digits + string.punctuation
        pw = ""
        pw += random.choice(string.ascii_uppercase)
        pw += random.choice(string.ascii_lowercase)
        pw += random.choice(string.digits)
        pw += random.choice(string.punctuation)
        for char in range(size-4):
            rand_char = random.choice(all_char)
            pw += rand_char
        return pw
    try:
        pw_size = int(size_in)
        password = password(pw_size)
        print("The generated password is:", password)
        print("_______________________________________________________________________________")
    except:
        print(" ")
        print("Invalid Data! To start, enter an integer number.")
        print("To close the program, write stop.")
        print("_______________________________________________________________________________")
    i += 1
print("Thank you for using this application!")

