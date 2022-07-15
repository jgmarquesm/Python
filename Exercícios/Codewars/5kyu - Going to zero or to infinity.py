# https://www.codewars.com/kata/55a29405bc7d2efaff00007c

def going(n):
    res = 0
    for i in range(1, n+1):
        res = res/i + 1
    return int(1e6*res)/1e6
