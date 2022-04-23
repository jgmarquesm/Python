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
                pi_list = []
                n = int(pow(10,-math.log10(tol)))
                n_r = n % 10
                error = abs(math.pi - approx_pi)
                j = 0
                if n_r == 0:
                    while error >= tol:
                        while j < n:
                            approx_pi = 4*(pow(-1,j)/(2*j + 1))
                            pi_list.append(approx_pi)
                            j += 1
                        approx_pi = sum(pi_list)
                        error = abs(math.pi - approx_pi)
                        pi = float('{:.10f}'.format(approx_pi))
                        return [j, pi]    
                elif n_r == 1:
                    while error >= tol:
                        while j < n:
                            approx_pi = 4*(pow(-1,j)/(2*j + 1))
                            pi_list.append(approx_pi)
                            j += 1
                        approx_pi = sum(pi_list)
                        error = abs(math.pi - approx_pi)
                        pi = float('{:.10f}'.format(approx_pi))
                        return [j, pi]
                else:
                    while error > tol:
                        while j <= n:
                            approx_pi = 4*(pow(-1,j)/(2*j + 1))
                            pi_list.append(approx_pi)
                            j += 1
                        approx_pi = sum(pi_list)
                        error = abs(math.pi - approx_pi)
                        pi = float('{:.10f}'.format(approx_pi))
                        return [j, pi]      
            p = iter_pi(m)
            print(" ")
            print(p)
            print("_______________________________________________________________________________")
        except:
            print(" ")
            print("Invalid Data! To start, enter a valid entry. To close the programa, write stop.")
            print("_______________________________________________________________________________")


