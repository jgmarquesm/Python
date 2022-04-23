def isnarcissistic(n):
    i = n
    narc = 0
    digits = []
    primes = []
    div = primes
    while i > 0:
        last_digit = i % 10
        digits.append(last_digit)
        i = i // 10
    digits.reverse()
    for j in range(2,n): 
        if (n % j == 0):
            continue
            primes.append(j)
    for k in range(1,n+1):
        if n % k == 0:
            div.append(k)
    for base in div:
        for l in range(0,len(digits)):
            narc += pow(base,digits[l])
            print(narc) # apenas para debug
            if narc == n:
                break
        print(base, "^", digits, "=", narc, div)                
    return #narc == n
x = isnarcissistic(111)
print(x)
	
