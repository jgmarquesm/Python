# https://www.codewars.com/kata/56606694ec01347ce800001b
def is_triangle(a, b, c):
    p = 0.5*(a + b + c)
    area = (p*(p-a)*(p-b)*(p-c))**(0.5)
    
    if a < 0 or b < 0 or c < 0:
        return False
    
    elif (isinstance(area, float) or isinstance(area, int)) and area > 0:
        return True
    
    return False
