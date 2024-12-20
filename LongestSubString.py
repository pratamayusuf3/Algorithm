def solution(s):
    n = len(s)
    max_len = 0
    char_set = set() # set untuk menyimpan karakter unik
    left = 0 # Pointer kiri (window)
    
    for right in range(n):
        # jika karakter right belum ada di dalam set, tambahkan
        if s[right] not in char_set:
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1) # update panjang max substring
        else:
            # jika karakter sudah ada, geser pointer kiri (left) sampai karakter tersebut dihapus semua
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
                
            char_set.add(s[right]) # tambahkan karakter baru ke dalam set
            
    return max_len


# Test Case
test_str = "abcbcbb"
result = solution(test_str)

# Menampilkan Hasil
print("Hasil : ", result)
    