# 3SumClosest - DONE
# ContainerMostWater - DONE
# LongestSubString - DONE
# ReverseInteger - DONE
# Turing1 - DONE

# 4Sum - DONE
# IntToRoman - 
# MedianTwoSortedArrays - DONE
# ReverseLetterOnly - DONE
# Turing2 - DONE

# AddLinkedList - DONE
# LetterComboOfPhone - DONE
# PalindromeNumber - DONE
# RomanToInt - DONE
# Turing3 - DONE

# BalanceDigit - DONE
# LongestComPrefix - DONE
# RegexMatch - DONE
# StrToInt - DONE
# TwoSum - DONE

# BinaryDepth - DONE
# LongestPalindromSubstring - DONE
# RemoveNthNode -
# ThreeSum - DONE
# ZigZag - DONE


def fourSum(nums, target):
    
    nums.sort()
    result = []
    
    for i in range (len(nums)-3):
        
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        for j in range (i+1, len(nums) - 2):
            
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            
            left = j + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    if left < right and nums[left] == nums[left-1]:
                        left += 1
                    if left < right and nums[right] == nums[right-1]:
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
