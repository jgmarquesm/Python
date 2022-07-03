# https://www.codewars.com/kata/526dbd6c8c0eb53254000110

import re
def alphanumeric(password):
    result = True if re.search('^[a-zA-Z0-9]*$', password) is not None else False
    if len(password) is 0:
        result = False
    return result 
