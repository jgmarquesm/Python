import math  #just if you need to use
import numpy #just if you need to use

# Defining ANY Function
def f(x):
    f = pow(x,3) - 5*x - 9 # This is just an example
    return f 
# Defining derivative of the function defined above
def df(x):
    df = 3*pow(x,2) - 5 # This is just an example
    return df 
    
# Implementing 1D Newton Raphson Method
def newtonRaphson(x0,e,n):
    i = 1
    flag = 1
    condition = True
    while condition:
        if df(x0) == 0: #Here I verify if the derivative is equal to zero, and if it is
# it will print a error msg to user. So, this is a way (But not the unique way. You can use 
# algebric or numerical method to proceed here.), to solve the derivative problem.
            print('Divide by zero error!')
            break
        x1 = x0 - f(x0)/df(x0)
        print('Iteration-%d, x = %0.12f and f(x) = %0.12f' % (i, x1, f(x1)))
        x0 = x1
        i += 1
        if i > n:
            flag = 0
            break
        condition = abs(f(x1)) > e
    if flag == 1:
        print('\nThe root is: %0.12f' % x1)
    else:
        print('\nNot Convergent. Maybe You can try a bigger number of interactions.')
# Input Section
x0 = float(input('Enter Guess: '))
e = float(input('Tolerable Error: '))
n = int(input('Maximum Step: '))

# Starting Newton Raphson Method
newtonRaphson(x0,e,n)
