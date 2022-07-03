# https://www.codewars.com/kata/5a2f83daee1aae4f1c00007e

isMultiple = lambda a, b, n: (int((a / b + 0.05) * 10) % 10) > 0 and (int((a / b + 0.05) * 10) % 10) % n == 0
