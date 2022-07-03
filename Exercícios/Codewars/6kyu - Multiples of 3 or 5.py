# https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):
    list = []
    m3or5 = []
    n = int(number)
    i = 0
    if n < 0:
        return 0
    while i < n:
        list.append(i)
        i += 1 
    for list_element in list:
        if list_element % 3 == 0 or list_element % 5 == 0:
            m3or5.append(list_element)
    return sum(m3or5)
