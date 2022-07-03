# https://www.codewars.com/kata/5815f7e789063238b30001aa

from statistics import mean

def redistribute_wealth(wealth):
    avg_value = mean(wealth)
    counter = 0
    while counter < len(wealth):
        wealth[counter] = avg_value
        counter += 1
    return wealth
