import math

print("Wellcome! This is the Fibonacci series generator.")
print("To start, write a number.")
print("In case of the number being negative, it will be converted into a positive number.")
print("TO close the program, write stop any time.")
print("_______________________________________________________________________________")
print(" ")

while True:
    print(" ")
    n_in = input("How many elements you want? ")
    n_in = n_in.lower()
    if n_in == "stop":
        quit()
    else:
        try:
            n_float = abs(float(n_in))
            n = int(n_float)
            i = 0
            fib = [0,1]
            if n == 0:
                print(" ")
                print("Oops! It is empty.")
                print("_______________________________________________________________________________")
            elif n == 1:
                print(" ")
                print(fib[0])
                print("_______________________________________________________________________________")
            elif n == 2:
                print(" ")
                print(fib)
                print("_______________________________________________________________________________")
            else:
                while i + 2 < n:
                    fib_new = fib[i] + fib[i+1]
                    fib.append(fib_new)
                    i += 1
                print(" ")
                print(fib)
                print("_______________________________________________________________________________")
        except:
            print(" ")
            print("Invalid Data! To start, enter a number. To close the program, write stop.")
            print("_______________________________________________________________________________")
