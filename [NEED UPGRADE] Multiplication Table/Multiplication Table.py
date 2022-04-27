n_iin = input("Do you want multiplication table of? ")
m_iin = input("... until? ")
n_in = float(n_iin)
m_in = int(m_iin)

def multiplication_table(n,m):
    i = 1
    while i <= m:
        print(i, "*", n, "= ", i*n)
        i += 1 

multiplication_table(n_in,m_in)
input() # This 'input' is only to keep the result on screen until press enter button 