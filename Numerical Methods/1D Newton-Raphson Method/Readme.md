1D Newton-Raphson Method.
This method find roots of equations doing f(x) = 0.
So, x_{i+1} = x_{i} - \frac{f(x_{i})}{f'(x_{i})}.
Thus, we need to verify (analytically) if the function f is differentiable, and find a way to solve the denominator problem (f'(x_{i}) = 0) when it happens. 
Luckly, solve the second one condition using a code is easy (+/- lol).
In the code, writed by me, you need to excute the program and make  a guess about the root, set the tolerance parameter and the maximum interactions, respectively.