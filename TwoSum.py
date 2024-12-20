def two_sum(nums, target):
    # Panjang array
    len1 = len(nums)
    
    # Mapping penyimpanan data antara value & posisi
    repo = {}
    
    # Cek sepanjang Looping nums
    for i in range(len1):
        diff = target - nums[i]
        
        # Bila ada nilai selisih yang sama di penyimpanan data
        if diff in repo:
            return [repo[diff], i]
        
        # Bila tidak ada nilai selisih yang sama, masukkan penyimpanan data
        repo[nums[i]] = i
        
    # Bila tidak ada pasangan yang cocok
    return []

# Input data test
nums = [3, 2, 4]
target = 6

# Memanggil fungsi two_sum
result = two_sum(nums, target)

if len(result) == 2:
    print("Posisi : ", result[0], result[1])
else:
    print("Tidak ada pasangan yang sesuai")

