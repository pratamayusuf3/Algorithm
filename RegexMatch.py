def main():
    
    # Input
    s = "ab"
    p = ".*"
    
    
    # Fungsi Hasil
    result = solution(s,p)
    
    # Print Result
    print("Hasil : ", result)
    
    
def solution(s, p):
    
    # Memanfaatkan rekursi dengan bantuanb indeks untuk setiap karakter di 's' dan 'p'
    return is_match_helper(s, p, 0, 0)


def is_match_helper(s, p, i, j):
    
    # Jika mencapai akhir p, hanya cocok jika mencapai hasil s
    if j == len(p):
        return i == len(s)
    
    # Memeriksa kecocokan karakter saat ini dari 's' dan 'p'
    match = i < len(s) and (s[i] == p[j] or p[j] == '.') 
    
    # Jika karakter berikutnya adalah '*', maka akan ada 2 pilihan
    if j + 1 < len(p) and p[j + 1] == '*':
        # Abaikan karakter '*' atau gunakan '*' untuk mencocokan karakter saat ini di 's'
        return is_match_helper(s, p, i, j+2) or (match and is_match_helper(s, p, i + 1, j))
    else:
        # Lanjutkan pencocokan ke karakter berikut nya
        return match and is_match_helper(s, p, i+1, j+1)
    

# Menjalankan fungsi utama 
if __name__ == "__main__":
    main()