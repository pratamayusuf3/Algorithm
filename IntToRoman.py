def solution(num):
    normal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    i = 0
    roman_str = ""
    
    # proses terus sampai nilai nya 0
    while num > 0:
        # bila nilai num masih diatas nilai karakter saat ini
        if num >= normal[i]:
            num -= normal[i]
            roman_str += roman[i]
        else :
            # pindah ke karakter lain
            i += 1
            
    return roman_str


def solution2(num):
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thousands = ["", "M", "MM", "MMM"]
    
    roman = (thousands[num // 1000] +
             hundreds[(num % 1000) // 100] +
             tens[(num % 100) // 10] +
             ones[num % 10])
    
    return roman


# input
k = 2549

# output
result = solution(k)
result2 = solution2(k)

# print result
print("Hasil   :", result)
print("Hasil 2 :", result2)
    