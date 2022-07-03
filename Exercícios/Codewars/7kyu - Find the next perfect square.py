# https://www.codewars.com/kata/56269eb78ad2e4ced1000013

find_next_square = lambda sq: (int(sq**(0.5)) + 1)**2 if int(sq**(0.5))**2 == sq else -1
