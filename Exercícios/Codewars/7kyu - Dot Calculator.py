# https://www.codewars.com/kata/6071ef9cbe6ec400228d9531

def calculator(txt):
    sep_txt = txt.split()
    n1, n2 = len(sep_txt[0]), len(sep_txt[2])
    if sep_txt[1] == "+": return (n1 + n2)*"."
    elif sep_txt[1] == "-": return (n1 - n2)*"."
    elif sep_txt[1] == "*": return (n1 * n2)*"."
    elif sep_txt[1] == "/": return (n1 / n2)*"."
    elif sep_txt[1] == "//": return (n1 // n2)*"."
