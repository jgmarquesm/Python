# https://www.codewars.com/kata/58249d08b81f70a2fc0001a4

closest_multiple_10 = lambda i: i if i % 10 == 0 else (i - i % 10 if i % 10 < 5 else i + 10 - i % 10)
