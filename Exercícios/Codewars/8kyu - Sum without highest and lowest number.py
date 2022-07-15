# https://www.codewars.com/kata/576b93db1129fcf2200001e6

def sum_array(arr):
    if not arr is None:
        arr = sorted(arr)
        return sum(arr[1:len(arr)-1])
    return 0
