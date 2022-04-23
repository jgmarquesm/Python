import math
print("Wellcome! This application calculate the value of pi given an error tolerance.")
print("To start, enter with the error tolerance that you desire.")
print("To close the program, write stop any time.")
print("_______________________________________________________________________________")
while True:
    print(" ")
    m_in = input("Error tolerance? ")
    m_in = m_in.lower()
    if m_in == "stop":
        quit()
    else:
        try:
            m = float(m_in)
            def iter_pi(tol):
                approx_pi = 0
                i = 0
                while abs(math.pi - approx_pi) > tol:
                    approx_pi += 4*(pow(-1,i)/(2*i + 1))
                    i += 1
                    pi = float('{:.10f}'.format(approx_pi))
                return [i, pi]      
            p = iter_pi(m)
            print(" ")
            print(p)
            print("_______________________________________________________________________________")
        except:
            print(" ")
            print("Invalid Data! To start, enter a valid entry. To close the programa, write stop.")
            print("_______________________________________________________________________________")




