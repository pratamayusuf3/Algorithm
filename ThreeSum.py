def three_sum(nums):
    # Hasil Test
    result = []
    nums.sort()     # Menghindari duplikasi dengan sorting
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue    # Skip duplikasi
        
        left = i + 1
        right = len(nums) - 1 
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                
                # Menghindari duplikasi triplet
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                    
            elif total < 0:
                left += 1
                
            else :
                right -= 1
                
    return result

# Input 
nums = [-1, 0, 1, 2, -1, -4]

# Panggil fungsi
result = three_sum(nums)

# Cetak Hasil
print("Hasil : ", result)