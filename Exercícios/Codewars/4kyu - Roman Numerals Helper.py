# https://www.codewars.com/kata/51b66044bce5799a7f000003

class RomanNumerals:
    
    def to_roman(val):
        roman_num = [0, 0, 0, 0, 0, 0, 0, 0]
        symbol = ("M", "D", "C", "L", "X", "V", "I")
                  
        while val > 0:
            
            if val >= 1000:
                roman_num[0] = val // 1000 
                val -= 1000*roman_num[0]
                
            elif val in range(500, 1000):
                roman_num[1] = val // 500
                val -= 500*roman_num[1]
            
            elif val in range(100, 500):
                roman_num[2] = val // 100
                val -= 100*roman_num[2]
            
            elif val in range(50, 100):
                roman_num[3] = val // 50
                val -= 50*roman_num[3]
            
            elif val in range(10, 50):
                roman_num[4] = val // 10
                val -= 10*roman_num[4]
            
            elif val in range(5, 10):
                roman_num[5] = val // 5
                val -= 5*roman_num[5]
            
            elif val in range(1, 5):
                roman_num[6] = val
                val = 0
                
        roman = [roman_num[i]*symbol[i] for i in range(0, 7)]
        return " ".join(roman).replace(" ", "").replace("DCCCC", "CM").replace("CCCC", "CD").replace("LXXXX", "XC").replace("XXXX", "XL").replace("VIIII", "IX").replace("IIII", "IV")

    def from_roman(roman_num):
        
        i = 0
        num = 0
        
        def value(symbol):
            if symbol == "I": return 1
            elif symbol == "V": return 5
            elif symbol == "X": return 10
            elif symbol == "L": return 50
            elif symbol == "C": return 100
            elif symbol == "D": return 500
            elif symbol == "M": return 1000
            else: return -1

        while i < len(roman_num):
            
            s1 = value(roman_num[i])

            if i + 1 < len(roman_num):
                s2 = value(roman_num[i + 1])

                if s1 >= s2:
                    num += s1
                    i += 1
                    
                else:
                    num += s2 - s1
                    i += 2
                    
            else:
                num += s1
                i += 1

        return num
