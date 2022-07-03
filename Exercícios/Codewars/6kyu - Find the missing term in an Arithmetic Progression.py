# https://www.codewars.com/kata/52de553ebb55d1fca3000371

find_missing = lambda sequence: ((len(sequence)+1)*(sequence[0] + sequence[-1]))/2 - sum(sequence)
