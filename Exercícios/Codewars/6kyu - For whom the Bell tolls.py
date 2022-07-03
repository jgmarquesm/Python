# https://www.codewars.com/kata/62665d43e67fbaf7b37212d2

def bell(n):
    if n % 2 == 0:
        lista_par = []
        counter1 = 0
        while counter1 < int(n/2):
            item = (counter1 + 1)*(n-counter1)
            lista_par.append(item)
            counter1 += 1
        counter2 = int(n/2)
        while 0 < counter2:
            item = (counter2)*(n-(counter2-1))
            lista_par.append(item)
            counter2 -= 1
        return lista_par
    elif n % 2 == 1:
        lista_impar = []
        counter1 = 0
        while counter1 < int(n/2):
            item = (counter1 + 1)*(n-counter1)
            lista_impar.append(item)
            counter1 += 1
        item_central = (n//2 + 1)*(n - n//2)
        lista_impar.insert((n//2 + 1), item_central)
        counter2 = int(n/2)
        while 0 < counter2:
            item = (counter2)*(n-(counter2-1))
            lista_impar.append(item)
            counter2 -= 1
        return lista_impar
    else: return False
    
