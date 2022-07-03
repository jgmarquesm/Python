# https://www.codewars.com/kata/55c45be3b2079eccff00010f

def order(sentence):
    
    words = sentence.split()
    order = []
    
    for i in range(1, len(words)+1):
        for item in words:
            if str(i) in item:
                 order.append(item)

    return " ".join(order)
