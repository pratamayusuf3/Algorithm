# 3SumClosest - DONE
# ContainerMostWater - DONE
# LongestSubString - DONE
# ReverseInteger - DONE
# Turing1 - DONE

# 4Sum - DONE
# IntToRoman - DONE
# MedianTwoSortedArrays - DONE
# ReverseLetterOnly - 
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


def solution(nums1, nums2):
    comb_nums = nums1 + nums2
    comb_nums.sort()
    
    if len(comb_nums) % 2 == 1:
        return comb_nums[len(comb_nums) // 2]
    else:
        var1 = comb_nums[len(comb_nums) // 2]
        var2 = comb_nums[(len(comb_nums) // 2) - 1]
        return (var1 + var2) / 2.0

# Main Program
nums1 = [1,3,4]
nums2 = [2,5]

result = solution(nums1,nums2)
print("Hasil : ",result)
