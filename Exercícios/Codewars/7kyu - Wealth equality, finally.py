from statistics import mean

def redistribute_wealth(wealth):
    avg_value = mean(wealth)
    counter = 0
    while counter < len(wealth):
        wealth[counter] = avg_value
        counter += 1
    return wealth