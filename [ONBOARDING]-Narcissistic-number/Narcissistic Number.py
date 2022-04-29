# Powered by JOão Gabriel to return if a input number is a narcissistic number.
while True:
    print(" ")
    n_in = input("Enter a number to verify if it is a narcissistic number: ")
    print("_______________________________________________________________________________")
    n_in = n_in.lower()
    if n_in == "stop":
        quit()
    def is_narcissistic(n):
        i = n
        digits = []
        while i > 0:
            last_digit = i % 10
            digits.append(last_digit)
            i = i // 10
        j = 0
        narc = 0
        pow = len(digits)
        while j < pow:
            narc += digits[j]**pow
            j += 1
        return narc == n
    try:
        n_iin = int(n_in)
        x = is_narcissistic(n_iin)
        if x == True:
            print(" ")
            print("Yeah! You got it.")
            print("_______________________________________________________________________________")
        else:
            print(" ")
            print("That number is not a narcissistic number.")
            print("_______________________________________________________________________________")
    except:
        print(" ")
        print("Invalid Data! To start, enter an integer number. To close the programa, write stop.")
        print("_______________________________________________________________________________")
