s = str(input())

def romanToInteger(s):
    roman_dict = {"I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000}
    
    x = 0
    s = s.replace("IV","IIII")
    s = s.replace("IX","VIIII")
    s = s.replace("XL","XXXX")
    s = s.replace("LC","LXXXX")
    s = s.replace("CD","CCCC")
    s = s.replace("CM","DCCCC")
    for i in s:
        x += roman_dict[i]
    return x

print(romanToInteger(s))