def solution(s):
    # Peta karakter Romawi ke nilai Integer
    roman_to_int = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
    
    ans = 0
    
    for i in range(len(s)):
        print(f"s[{i}] : {s[i]}")
        
        # Cek apakah nilai simbol sekarang lebih kecil dari nilai simbol berikut nya
        if i < len(s)-1 and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
            ans -= roman_to_int[s[i]]
        else:
            ans += roman_to_int[s[i]]
            
        print(f"ans : {ans}")
        
    return ans


# Input 
k = "MMDXLIX"

# Fungsi Hasil
result = solution(k)

# Output Hasil
print("Hasil : ",result)