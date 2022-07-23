def square_of_sum(number: int) -> int:
    sum = 0
    for n in range(1, number+1):
        sum += n
    return sum**2


def sum_of_squares(number: int) -> int:
    sum = 0
    for n in range(1, number+1):
        sum += n**2
    return sum


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)