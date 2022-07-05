# https://www.codewars.com/kata/52685f7382004e774f0001f7

import time

def make_readable(seconds):
    
    x = list(time.gmtime(seconds))
    
    if (seconds // 360) > 1:
        x[3] = int((seconds // 360)//10)
        
    h, m, s = x[3], x[4], x[5]
    
    return "{:02}:{:02}:{:02}".format(h, m, s)
