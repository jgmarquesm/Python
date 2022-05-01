from datetime import datetime
import string
import random
import os

symbols = "!$%&()*+,-./:;<=>?@[\]^_`{|}~"

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
    all_char = string.ascii_letters + string.digits + symbols
    pw = ""
    for char in range(size):
        rand_char = random.choice(all_char)
        pw += rand_char
    return pw

def password3(size):
    all_char = string.ascii_letters + string.digits + symbols
    pw = ""
    pw += random.choice(string.ascii_uppercase)
    pw += random.choice(string.ascii_lowercase)
    pw += random.choice(string.digits)
    pw += random.choice(symbols)
    for char in range(size-4):
        rand_char = random.choice(all_char)
        pw += rand_char
    return pw

def result(pw):
    print()
    print("The generated password is:", pw)
    print("Your password has been saved in a txt file.")
    print("_______________________________________________________________________________")

def print_(x):
    print()
    print(x)
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
            kind = "Numeric"
            print()
            size_in = input("How many characters do you need in this password? ")
            size_in = size_in.lower()
            if size_in == "stop":
                quit()
            print()
            pw_size = int(size_in)
            password = password1(pw_size)
            result(password)
        elif case == 2:
            kind = "Alphanumeric without reqs"
            print()
            size_in = input("How many characters do you need in this password? ")
            size_in = size_in.lower()
            if size_in == "stop":
                quit()
            print()
            pw_size = int(size_in)
            password = password2(pw_size)
            result(password)
        elif case == 3:
            kind = "Alphanumeric with reqs"
            print()
            size_in = input("How many characters do you need in this password? ")
            size_in = size_in.lower()
            if size_in == "stop":
                quit()
            pw_size = int(size_in)
            if pw_size < 4:
                print_("You need to enter at least 4 in this case.")
                print()
                pw_size = int(input("How many characters do you need in this password? "))
                size_in = size_in.lower()
                if size_in == "stop":     
                    quit()
                password = password3(pw_size)
                result(password)
            else:   
                password = password3(pw_size)
                result(password)                
        else:
            print_("Please, enter a valid case.")
            break
        print()
        now = datetime.now()
        date  = now.strftime("%d-%m-%Y %H:%M:%S")
        print("If  you enter a invalid entry here, it will be assumed you want to stop.")
        customize = input("[Y/N] Do you want to customize the file name? ")
        customize = customize.lower()

        if customize == "y":
            passw = input("Enter the name you want to save it: ")
            passw += ".txt"
        elif customize == "n":
            passw = kind + " Password " + date + ".txt"
        else:
            quit()
        pw_file = open(passw,'w')
        pw_file.write("Your Password is: "+password)
        pw_file.close()
        print("_______________________________________________________________________________")
        print()
        print("If  you enter a invalid entry here, it will be assumed you want to stop.")
        cont = input("[Y/N] Do you want to execute one more time? ")
        cont = cont.lower() 
        if cont == "y":
            condition = True
            os.system("clear")
        else:
            condition = False
            print_("Thank you for using this application!")            
    except:
        except_()
