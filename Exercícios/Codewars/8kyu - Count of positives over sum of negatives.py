# https://www.codewars.com/kata/576bb71bbbcf0951d5000044

def count_positives_sum_negatives(arr):
    count = 0
    sum = 0
    for i in arr:
        if int(i) > 0:
            count += 1
        elif int(i) < 0:
            sum += i
    if len(arr) == 0:
        return []
    return [count, sum]
