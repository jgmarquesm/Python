from zxcvbn import zxcvbn as se
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
    print("Your password has been saved in a .txt file.")
    print("_______________________________________________________________________________")

def print_(x):
    print()
    print(x)
    print("_______________________________________________________________________________")

def strengthVerification(pw):
    strength_estimator = se(pw)
    score = strength_estimator["score"]
    if score == 0:
        print_("Score 0: Your password is terrible!")
    elif score == 1:
        print_("Score 1: Your password is not good and not safe!")
    elif score == 2:
        print_("Score 2: Your password is good, but not safe enough!")
    elif score == 3:
        print_("Score 3: Your password is in a good way to stay safe!")
    elif score == 4:
        print_("Score 4: Your password is the best forever! And safer too!")

def except_():
    print("_______________________________________________________________________________")
    print()
    print("Invalid Data!")
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
            break
        i = 0
        case = int(case)
        
        if case == 1:
            kind = "Numeric"
            print()
            size_in = input("How many characters do you need in this password? ")
            size_in = size_in.lower()
            if size_in == "stop":
                break
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
                break
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
                break
            pw_size = int(size_in)
            if pw_size < 4:
                print_("You need to enter at least 4 in this case.")
                print()
                pw_size = int(input("How many characters do you need in this password? "))
                size_in = size_in.lower()
                if size_in == "stop":     
                    break
                password = password3(pw_size)
                result(password)
            else:   
                password = password3(pw_size)
                result(password)
        
        else:
            print_("Please, enter a valid case.")
            os.system("clear")
            continue

        strengthVerification(password)
        
        print()
        now = datetime.now()
        date  = now.strftime("%d-%m-%Y %H:%M:%S")
        print("If  you enter a invalid entry here, it will be assumed you want to stop.")
        customize = input("[Y/N] Do you want to customize the file name? ")
        customize = customize.lower()

        if customize == "y" or customize == "yes":
            passw = input("Enter the name you want to save it: ")
            passw += ".txt"
        elif customize == "n" or customize == "no" or customize == "not":
            passw = kind + " Password " + date + ".txt"
        else:
            break
        
        try:
            path_ = "/home/notebook/Área de Trabalho/Github/Projetos/Python/Password-Generator/output/"
            os.mkdir(path_)
            complete_path_ = os.path.join(path_, passw)
        except:
            path_ = "/home/notebook/Área de Trabalho/Github/Projetos/Python/Password-Generator/output/"
            complete_path_ = os.path.join(path_, passw)
            
        pw_file = open(complete_path_,"w")
        pw_file.write("Your Password is: {}".format(password))
        pw_file.close()
       

        print("_______________________________________________________________________________")
        print()
        print("If  you enter a invalid entry here, it will be assumed you want to stop.")
        cont = input("[Y/N] Do you want to execute one more time? ")
        cont = cont.lower()
        if cont == "y" or cont == "yes":
            condition = True
            os.system("clear")
        else:
            condition = False
            print_("Thank you for using this application!")            
    except:
        except_()
