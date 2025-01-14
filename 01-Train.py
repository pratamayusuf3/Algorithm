# 3SumClosest - DONE
# ContainerMostWater - DONE
# LongestSubString - DONE
# ReverseInteger - DONE
# Turing1 - DONE

# 4Sum - DONE
# IntToRoman - DONE
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

# BinaryDepth -




    

def solution(nums, target):
    
    i = 0    
    repo = {}
    
    while i < len(nums):
        diff = target - nums[i]
        
        if diff in repo:
            return [repo[diff], i]
        
        repo[nums[i]] = i
        
        i += 1
    
    return []
    

# Input data test
nums = [3, 2, 4]
target = 6

# Memanggil fungsi two_sum
result = solution(nums, target)

if len(result) == 2:
    print("Posisi : ", result[0], result[1])
else:
    print("Tidak ada pasangan yang sesuai")