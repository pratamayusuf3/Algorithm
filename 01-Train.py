# 3SumClosest - DONE
# ContainerMostWater - DONE
# LongestSubString - DONE
# ReverseInteger - DONE
# Turing1 - DONE
# 4Sum - DONE
# IntToRoman - 


def fourSum(nums, target):
    
    nums.sort()
    n = len(nums)
    result = []
    
    for i in range(n-3):
        
        if (nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target):
            break
        
        if (nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target):
            continue
        
        if (i > 0 and nums[i] == nums[i-1]) :
            continue
        
        for j in range(i+1, n-2):
            
            if (nums[i] + nums[j] + nums[j+1] + nums[j+2] > target):
                break
            
            if (nums[i] + nums[j] + nums[n-1] + nums[n-2] < target):
                continue
            
            if (j > i + 1 and nums[j] == nums[j-1]) :
                continue
            
            left = j + 1
            right = n - 1
            
            while left < right :
                
                total = nums[i] + nums[j] + nums[left] + nums[right]
                
                if (total == target):
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    if left < right and nums[left] == nums[left-1]:
                        left += 1
                        
                    if left < right and nums[right] == nums[right+1]:
                        right -= 1
                        
                elif total < target :
                    left += 1
                else :
                    right -= 1
                    
    return result
                    
                


if __name__ == "__main__":
    
    #nums = [2,4,1,3,2,6,5,8,7]
    #target = 10
    
    nums = [1,0,-1,0,-2,2]
    target = 0
    
    result = fourSum(nums, target)
    
    print("Hasil : ", result)