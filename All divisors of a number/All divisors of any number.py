while True:
    print(" ")
    n_in = input("Enter with a integer number: ")
    print(" ")
    n_in = n_in.lower()
    if n_in == "stop":
        quit()
    def all_divisors(n):
        div = []
        for j in range(1,n+1):
            if n % j == 0:
                div.append(j)
        if len(div) == 2:
            prime = "That's a Prime number!"
            return prime
        else:
            not_prime = "That's not a Prime number. There are more than two integer divisors."
            return not_prime
    def show_all_divisors(n):
        div = []
        for j in range(1,n+1):
            if n % j == 0:
                div.append(j)
        return div
    try:
        n_float = float(n_in)
        n_iin = int(n_float)
        x = all_divisors(n_iin)
        print(x)
        print("_______________________________________________________________________________")
        print(" ")
        print("Enter N to quit or Y to view.")
        print("_______________________________________________________________________________")
        print(" ")
        yes_not = input("Do you want to see the list with all divisors of the input number? ")
        yes_not = yes_not.lower()
        if yes_not == "y":
            print(" ")
            divs = show_all_divisors(n_iin)
            print(divs)
            print("_______________________________________________________________________________")
        elif yes_not == "n":
            quit()
    except:
        print(" ")
        print("Invalid Data! To start, enter an integer number.To see the divisors, enter Y.")
        print("To close the program, write stop or N.")
        print("_______________________________________________________________________________")


