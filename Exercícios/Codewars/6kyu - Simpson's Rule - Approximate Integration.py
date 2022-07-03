# https://www.codewars.com/kata/565abd876ed46506d600000d

import math

# f(x) = 3/2 sin**3(x)
# [0, pi]

def simpson(n):

    integral = 0
    i = 1
    
    while i <= n/2:
        integral += 3*math.sin((2*i-1)*math.pi/n)**3 + (3/2)*math.sin(2*i*math.pi/n)**3
        i += 1
    integral = (math.pi/(3*n))*(2*integral)
    
    return integral
