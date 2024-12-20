def solution (nums1, nums2):
    
    # Gabungkan kedua array
    merge_array = nums1 + nums2
    
    # Urutkan array gabungan
    merge_array.sort()
    
    length = len(merge_array)
    
    # Jika panjang array ganjil
    if length % 2 == 1:
        return merge_array[length // 2]
    # Jika panjang array genap
    else:
        mid1 = merge_array[(length // 2) - 1]
        mid2 = merge_array[length // 2]
        return (mid1 + mid2) / 2.0
    

# Main Program
nums1 = [1,3,4]
nums2 = [2]

result = solution(nums1,nums2)
print("Hasil : ",result)