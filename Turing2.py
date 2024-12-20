def main():
    # Input
    k = [1,2,2,1,5,3,4,3,4]
    
    result = 0
    
    # Fungsi Hasil
    result =  solution(k)
    
    # Print result
    print("Hasil : ", result)
    
    
def solution(k):
    # Sort untuk mengelompokkan nilai yang berpasangan
    k.sort()
    
    # Validasi jika panjang array kurang dari 3
    if len(k) < 3:
        return -1
    
    # Mencari kartu spesial
    i = 0
    while i < len(k):
        # Jika kartu spesial ada di posisi terakhir
        if i == len(k) - 1:
            return k[i]
        # Periksa pasangan
        elif k[i] != k[i+1]:
            return k[i]
        # Lewati pasangan
        i += 2
        
    return -1


if __name__ == "__main__":
    main()