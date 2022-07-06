# https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(list):
    for item in list:
        if item == 0:
            list.pop(list.index(item))
            list.append(item)
    return list
