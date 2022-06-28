def likes(names):
    n = len(names) - 2
    n_str = str(n)
    if n + 2 == 0:
        y = "no one likes this"
    elif n + 2 == 1:
        y = names[0] + " likes this"
    elif n + 2 == 2:
        y = names[0] + " and " + names[1] + " like this"
    elif n + 2 == 3:
        y = names[0] + ", " + names[1] + " and " + names[2] + " like this"
    else:
        y = names[0] + ", " + names[1] + " and " + n_str + " others like this"
    return y