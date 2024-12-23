'''

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
 
Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

'''


def fourSum(nums, target):
    
    nums.sort() # Sort the array first
    n = len(nums)
    result = []
    
    # Iterate over the first two number
    for i in range(n-3):
        
        # Early exit if the smallest sum exceeds the target
        if nums[i] + nums[i+1] + nums[i+2] + nums [i+3] > target:
            break
        
        # Skip duplicates for their first number
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # Early exit if the largest possible sum is less than the target ?? kok code nya continue bukan break ??
        if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
            continue
        
        for j in range(i+1, n-2):
            # Skip duplicates for the second number
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            
            # Early exit for the second number
            if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                break
            
            if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                continue
            
            # Now use two pointers for the remaining two numbers
            left, right = j+1, n-1 
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for the third number
                    while left < right and nums[left] == nums[left -1]:
                        left += 1
                        
                    # Skip duplicates for the fourth number
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                        
                elif total < target:
                    left += 1
                else:
                    right -= 1
                    
    return result
    
    
if __name__ == "__main__":
    
    #nums = [2,4,1,3,2,6,5,8,7]
    #target = 10
    
    nums = [1,0,-1,0,-2,2]
    target = 0
    
    result = fourSum(nums, target)
    
    print("Hasil : ", result)