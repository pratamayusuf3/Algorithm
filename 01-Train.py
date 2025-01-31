# 3SumClosest - DONE
# ContainerMostWater - DONE
# LongestSubString - 
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

# BinaryDepth - DONE
# LongestPalindromSubstring - DONE
# RemoveNthNode -
# ThreeSum - DONE
# ZigZag - DONE



def solution(height):
    left = 0
    right = len(height) - 1
    max_cal = 0
    
    while left < right:
        cur_cal = (right - left) * min(height[left], height[right])
        max_cal = max(cur_cal,max_cal) 
        
        if height[left] < height[right]:
            left += 1
        else :
            right -= 1
            
    return max_cal

# input
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# output 
result = solution(height)
print("Hasil : ",result)
