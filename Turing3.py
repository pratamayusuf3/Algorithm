def solution(k):
    
    # jumlah total selisih absolut antara digit angka-angka pada semua pasangan elemen array
    
    result = 0
    
    for i in range (1,len(k)):
        for j in range (0,i):
            temp1 = k[i]
            temp2 = k[j]
            while temp1 > 0 and temp2 > 0:
                # ambil digit paling kanan
                digit1 = temp1 % 10
                digit2 = temp2 % 10
                if digit1 > digit2:
                    diff = digit1 - digit2
                else:
                    diff = digit2 - digit1
                # jumlahkan selisih
                result += diff
                # maju ke digit selanjut nya
                temp1 = temp1 // 10
                temp2 = temp2 // 10
    return result
                

# Input
k = [23, 13, 14]

# Output 
result = solution(k)

# Print result
print("Hasil : ",result)