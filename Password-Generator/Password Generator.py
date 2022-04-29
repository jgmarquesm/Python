import string
import random

def init():
    print()
    print("Wellcome to the Password Generator!")
    print("_______________________________________________________________________________")
    print()
    print("1 - Numeric Password.")
    print("2 - Alphanumeric Password without requeriments.")
    print("3 - Alphanumeric Password with requirements (At least 4 characters).")
    print("Enter stop anytime to close.")
    print("_______________________________________________________________________________")

def password1(size):
    all_char = string.digits
    pw = ""
    for car in range(size):
        rand_char = random.choice(all_char)
        pw += rand_char
    return pw

def password2(size):
    all_char = string.ascii_letters + string.digits + string.punctuation
    pw = ""
    for char in range(size):
        rand_char = random.choice(all_char)
        pw += rand_char
    return pw

def password3(size):
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

def result(pw):
    print()
    print("The generated password is:", pw)
    print("_______________________________________________________________________________")

def except_():
    print("_______________________________________________________________________________")
    print()
    print("Invalid Data! To start, enter an integer number.")
    print("To close the program, write stop.")
    print("_______________________________________________________________________________")

condition = True
    
while condition:
    try:
        init()
        print()
        case = input("Please, enter the kind of password yout want to get: ")
        case = case.lower()
        if case == "stop":
            quit()
        i = 0
        case = int(case)
        if case == 1:
            print()
            m = input("How many passwords you want to? ")
            if m == "stop":
                quit()
            n = int(m)
            while i < n:
                print()
                size_in = input("How many characters do you need in this password? ")
                size_in = size_in.lower()
                if size_in == "stop":
                    quit()
                print()
                pw_size = int(size_in)
                password = password1(pw_size)
                result(password)
                i += 1
        elif case == 2:
            print()
            m = input("How many passwords you want to? ")
            if m == "stop":
                quit()
            n = int(m)
            while i < n:
                print()
                size_in = input("How many characters do you need in this password? ")
                size_in = size_in.lower()
                if size_in == "stop":
                    quit()
                print()
                pw_size = int(size_in)
                password = password2(pw_size)
                result(password)
                i += 1
        elif case == 3:
            print()
            m = input("How many passwords you want to? ")
            if m == "stop":
                quit()
            n = int(m)
            while i < n:
                print()
                size_in = input("How many characters do you need in this password? ")
                size_in = size_in.lower()
                if size_in == "stop":
                    quit()
                print()
                pw_size = int(size_in)
                if pw_size < 4:
                    print()
                    print("You need to enter at least 4 in this case.")
                    print("_______________________________________________________________________________")
                else:
                    password = password3(pw_size)
                    result(password)                
                    i += 1
        else:
            print()
            print("Please, enter a valid case.")
            print("_______________________________________________________________________________")
        print()
        print("If  you enter a invalid entry here, it will be assumed you want to stop.")
        cont = input("[Y/N] Do you want to execute one more time? ")
        cont = cont.lower()
        if cont == "y":
            condition = True
        elif cont == "n":
            condition = False
            print()
            print("Thank you for using this application!")
            print("_______________________________________________________________________________")
        else:
            condition = False
    except:
        except_()
