# https://www.codewars.com/kata/550527b108b86f700000073f

import math
def iter_pi(tol):
    approx_pi = 0
    i = 0
    while abs(math.pi - approx_pi) > tol:
        approx_pi += 4*(pow(-1,i)/(2*i + 1))
        i += 1
        pi = float('{:.10f}'.format(approx_pi))
    return [i, pi]
