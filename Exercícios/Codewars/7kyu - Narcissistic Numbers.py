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
