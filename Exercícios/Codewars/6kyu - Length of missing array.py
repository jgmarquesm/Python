# https://www.codewars.com/kata/57b6f5aadb5b3d0ae3000611

def get_length_of_missing_array(a):
    if a is None or len(a) == 0:
        return 0
    else:
        lens = [len(a[i]) if a[i] is not None else 0 for i in range(0, len(a))]
        lens.sort()
        missing = (len(lens)+1)*(lens[0] + lens[-1])/2 - sum(lens)
        return missing if missing > 0 else 0
