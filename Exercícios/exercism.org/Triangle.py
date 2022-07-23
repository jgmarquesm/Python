def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return a + b >= c and b + c >= a and a + c >= b and a == b == c and all(sides) > 0


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return a + b >= c and b + c >= a and a + c >= b and (a == b or a == c or b == c) and all(sides) > 0


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return a + b >= c and b + c >= a and a + c >= b and a != b and a != c and b != c and all(sides) > 0