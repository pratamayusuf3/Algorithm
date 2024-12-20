def solution(s):
    if not s or len(s) == 0:
        return 0
    
    i = 0
    sign = 1
    
    # abaikan spasi
    while i < len(s) and s[i] == ' ':
        i += 1
        
    # cek tanda
    if i < len(s) and (s[i] == '+' or s[i] == '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1
        
    # Abaikan angka nol di depan
    while i < len(s) and s[i] == '0':
        i += 1

    # Konversi karakter ke integer
    result = 0
    while i < len(s) and s[i].isdigit():
        result = result * 10 + (ord(s[i]) - ord('0'))

        # Handle overflow
        if sign * result > 2**31 - 1:
            return 2**31 - 1
        if sign * result < -2**31:
            return -2**31

        i += 1

    return sign * result


# Input
k = "1337c0d3"

# Output
result = solution(k)

# Print result
print("Hasil:", result)