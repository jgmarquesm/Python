def square(number: int) -> int:
    if number <= 0 or number >= 65:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)


def total() -> int:
    sum = 0
    for n in range(0, 65):
        sum += 2**(n-1)
    return round(sum)-1