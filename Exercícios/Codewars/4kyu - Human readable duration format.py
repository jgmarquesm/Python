# https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(seconds = 0):
    
    if seconds == 0:
        return "now"
    
    y = seconds // 31536000
    seconds %= 31536000
    d = seconds // 86400
    seconds %= 86400
    h = seconds // 3600
    seconds %= 3600
    m = seconds // 60
    s = seconds % 60
    
    time = [y, d, h, m, s]
    format = [0, 0, 0, 0, 0]            
    list = []    
    str = ""
    time_type = (
        ["year", "years"], 
        ["day", "days"], 
        ["hour", "hours"], 
        ["minute", "minutes"], 
        ["second", "seconds"]
    )
    
    for i in range(0, len(time)): 
        if time[i] == 1:
            format[i] = time_type[i][0]
        elif time[i] > 1:
            format[i] = time_type[i][1]
            
    for j in range(0, len(time)):
        if time[j] != 0:
            item = f"{time[j]} {format[j]}"
            list.append(item)
    
    for k in range(0, len(list)):
        if len(list) == 1:
            str = list[0]
        elif list[k] is not list[-1] and list[k] is not list[-2]:
            str += f"{list[k]}, "
        elif list[k] is list[-2]:
            str += f"{list[k]} "
        elif list[k] is list[-1]:
            str += f"and {list[k]}"
            
    return str
